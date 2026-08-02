@tool
extends Node3D
## The scale lab.
##
## Builds itself from res://assets/manifest.json, which tools/gen_lab.py copies
## out of art/assets.json. Every asset in the manifest gets a station. If its
## .gltf exists the real model is shown; if not, a wireframe box at the declared
## size stands in — so the lab answers "do these sizes read?" before a single
## voxel has been authored.
##
## This scene exists to decide the numbers in docs/SCALE.md and then be deleted.

const MANIFEST := "res://assets/manifest.json"
const MODEL_DIR := "res://assets/models/"

const STATION_PITCH := 3.0    ## metres between station centres
const STATIONS_PER_ROW := 8
const ROW_PITCH := 6.0

## A 1.75 m reference figure stands at every station, so scale is never judged
## in the abstract.
const MANNEQUIN_OFFSET := Vector3(-1.0, 0.0, 0.0)

@onready var _camera: Camera3D = $Camera3D
@onready var _readout: Label = $UI/Readout

var _manifest: Dictionary = {}
var _stations: Array[Dictionary] = []
var _focus := 0
var _overview := false
var _tilt_degrees := 35.0    ## degrees off straight down
var _ortho_size := 6.0


func _ready() -> void:
	_load_manifest()
	_add_ground()
	_build()
	_apply_camera()
	if not Engine.is_editor_hint():
		_update_readout()


func _load_manifest() -> void:
	if not FileAccess.file_exists(MANIFEST):
		push_error("No manifest at %s — run: python3 tools/gen_lab.py" % MANIFEST)
		return
	var text := FileAccess.get_file_as_string(MANIFEST)
	var parsed: Variant = JSON.parse_string(text)
	if typeof(parsed) != TYPE_DICTIONARY:
		push_error("%s is not valid JSON" % MANIFEST)
		return
	_manifest = parsed
	_tilt_degrees = float(_manifest.get("camera_tilt_degrees", 35.0))


# -- construction ----------------------------------------------------------


func _add_ground() -> void:
	## Something for shadows to land on. Assets judged against a void read wrong.
	var existing := get_node_or_null("Ground")
	if existing:
		existing.free()
	var node := MeshInstance3D.new()
	node.name = "Ground"
	var mesh := PlaneMesh.new()
	mesh.size = Vector2(400, 400)
	node.mesh = mesh
	node.position = Vector3(0, -0.005, 0)
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.55, 0.57, 0.52)
	mat.roughness = 1.0
	node.material_override = mat
	add_child(node)
	if Engine.is_editor_hint():
		node.owner = get_tree().edited_scene_root


func _build() -> void:
	var root := $Stations
	for child in root.get_children():
		child.free()
	_stations.clear()

	var assets: Array = _manifest.get("assets", [])
	for i in assets.size():
		var asset: Dictionary = assets[i]
		var pos := _station_position(i)
		var station := Node3D.new()
		station.name = String(asset.get("name", "asset_%d" % i))
		station.position = pos
		root.add_child(station)
		if Engine.is_editor_hint():
			station.owner = get_tree().edited_scene_root

		var size_m: Vector3 = _size_metres(asset)
		var built := _add_model(station, asset)
		if not built:
			_add_ghost_box(station, size_m)
		_add_pad(station, size_m)
		_add_mannequin(station)
		_add_label(station, asset, size_m, built)

		_stations.append({
			"name": String(asset.get("name", "")),
			"title": String(asset.get("title", "")),
			"position": pos,
			"size_m": size_m,
			"built": built,
			"batch": String(asset.get("batch", "")),
		})


func _station_position(i: int) -> Vector3:
	var col := i % STATIONS_PER_ROW
	var row := i / STATIONS_PER_ROW
	return Vector3(col * STATION_PITCH, 0.0, -row * ROW_PITCH)


func _size_metres(asset: Dictionary) -> Vector3:
	var s: Array = asset.get("size", [8, 8, 8])
	var per_m := float(_manifest.get("voxels_per_metre", 8))
	return Vector3(float(s[0]), float(s[2]), float(s[1])) / per_m


func _add_model(station: Node3D, asset: Dictionary) -> bool:
	var path := MODEL_DIR + String(asset.get("name", "")) + ".gltf"
	if not ResourceLoader.exists(path):
		return false
	var packed: PackedScene = load(path)
	if packed == null:
		return false
	var instance := packed.instantiate()
	station.add_child(instance)
	if Engine.is_editor_hint():
		_own_recursive(instance)
	return true


func _own_recursive(node: Node) -> void:
	node.owner = get_tree().edited_scene_root
	for child in node.get_children():
		_own_recursive(child)


func _add_ghost_box(station: Node3D, size_m: Vector3) -> void:
	## The declared bounding box, drawn as translucent volume plus hard edges.
	var box := MeshInstance3D.new()
	box.name = "GhostBox"
	var mesh := BoxMesh.new()
	mesh.size = size_m
	box.mesh = mesh
	# Pivot handling: the box is drawn from the ground up, matching a corner
	# pivot. Centred-pivot assets read the same at this size, so keep it simple.
	box.position = Vector3(0.0, size_m.y * 0.5, 0.0)

	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(1.0, 0.0, 1.0, 0.18)
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	mat.cull_mode = BaseMaterial3D.CULL_DISABLED
	box.material_override = mat
	station.add_child(box)

	var edges := MeshInstance3D.new()
	edges.name = "GhostEdges"
	edges.mesh = _box_wire(size_m)
	var emat := StandardMaterial3D.new()
	emat.albedo_color = Color(1.0, 0.2, 1.0)
	emat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	edges.material_override = emat
	station.add_child(edges)

	if Engine.is_editor_hint():
		box.owner = get_tree().edited_scene_root
		edges.owner = get_tree().edited_scene_root


func _box_wire(size_m: Vector3) -> ArrayMesh:
	var v := PackedVector3Array()
	var c := [
		Vector3(0, 0, 0), Vector3(size_m.x, 0, 0),
		Vector3(size_m.x, 0, -size_m.z), Vector3(0, 0, -size_m.z),
	]
	for i in 4:
		var a: Vector3 = c[i]
		var b: Vector3 = c[(i + 1) % 4]
		var up := Vector3(0, size_m.y, 0)
		v.append_array([a, b, a + up, b + up, a, a + up])
	var arrays := []
	arrays.resize(Mesh.ARRAY_MAX)
	arrays[Mesh.ARRAY_VERTEX] = v
	var mesh := ArrayMesh.new()
	mesh.add_surface_from_arrays(Mesh.PRIMITIVE_LINES, arrays)
	return mesh


func _add_pad(station: Node3D, size_m: Vector3) -> void:
	## A 1 m grid pad under each station, so footprints are readable in metres.
	var w: int = int(ceil(maxf(size_m.x, 1.0))) + 2
	var d: int = int(ceil(maxf(size_m.z, 1.0))) + 2
	var v := PackedVector3Array()
	var y := 0.002
	for x in range(-1, w):
		v.append_array([Vector3(x, y, 1.0), Vector3(x, y, -float(d) + 1.0)])
	for z in range(-1, d):
		v.append_array([Vector3(-1.0, y, -z + 0.0), Vector3(float(w) - 1.0, y, -z + 0.0)])
	var arrays := []
	arrays.resize(Mesh.ARRAY_MAX)
	arrays[Mesh.ARRAY_VERTEX] = v
	var mesh := ArrayMesh.new()
	mesh.add_surface_from_arrays(Mesh.PRIMITIVE_LINES, arrays)

	var node := MeshInstance3D.new()
	node.name = "Pad"
	node.mesh = mesh
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.25, 0.55, 0.6)
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	node.material_override = mat
	station.add_child(node)
	if Engine.is_editor_hint():
		node.owner = get_tree().edited_scene_root


func _add_mannequin(station: Node3D) -> void:
	## 1.75 m tall, 0.625 wide, 0.5 deep — char_civilian_base's declared box.
	var node := MeshInstance3D.new()
	node.name = "Mannequin"
	var mesh := BoxMesh.new()
	mesh.size = Vector3(0.625, 1.75, 0.5)
	node.mesh = mesh
	node.position = MANNEQUIN_OFFSET + Vector3(0.0, 0.875, 0.0)
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.35, 0.85, 0.9)
	node.material_override = mat
	station.add_child(node)
	if Engine.is_editor_hint():
		node.owner = get_tree().edited_scene_root


func _add_label(station: Node3D, asset: Dictionary, size_m: Vector3, built: bool) -> void:
	var label := Label3D.new()
	label.name = "Label"
	var s: Array = asset.get("size", [])
	label.text = "%s\n%dx%dx%d vox  %.2f x %.2f x %.2f m%s" % [
		String(asset.get("name", "")),
		int(s[0]), int(s[1]), int(s[2]),
		size_m.x, size_m.z, size_m.y,
		"" if built else "\n(not built — ghost box)",
	]
	label.font_size = 40
	label.pixel_size = 0.005
	label.outline_size = 14
	label.outline_modulate = Color(0, 0, 0, 0.95)
	label.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	label.modulate = Color(1, 1, 1) if built else Color(1.0, 0.5, 1.0)
	label.position = Vector3(0.0, maxf(size_m.y, 1.75) + 0.6, 0.0)
	label.no_depth_test = true
	station.add_child(label)
	if Engine.is_editor_hint():
		label.owner = get_tree().edited_scene_root


# -- camera ----------------------------------------------------------------


func _apply_camera() -> void:
	if _camera == null:
		return
	_camera.projection = Camera3D.PROJECTION_ORTHOGONAL
	_camera.near = 0.05
	_camera.far = 400.0

	var target := Vector3.ZERO
	if _overview:
		var assets: Array = _manifest.get("assets", [])
		var rows: int = int(ceil(float(assets.size()) / STATIONS_PER_ROW))
		target = Vector3(
			(STATIONS_PER_ROW - 1) * STATION_PITCH * 0.5,
			0.0,
			-(rows - 1) * ROW_PITCH * 0.5,
		)
		_camera.size = maxf(rows * ROW_PITCH + 6.0, 27.0)
	else:
		if _focus >= 0 and _focus < _stations.size():
			# Aim at the middle of the asset's footprint, not at its pivot, so
			# corner-pivoted pieces are not shoved into a corner of the frame.
			var s: Dictionary = _stations[_focus]
			var size_m: Vector3 = s["size_m"]
			target = s["position"] + Vector3(size_m.x * 0.5, 0.0, -size_m.z * 0.5)
		_camera.size = _ortho_size

	# Labels are only legible one at a time; in a dense row they become mush.
	var stations := $Stations.get_children()
	for i in stations.size():
		var label := stations[i].get_node_or_null("Label")
		if label:
			label.visible = not _overview and i == _focus

	var pitch := -(90.0 - _tilt_degrees)
	_camera.rotation_degrees = Vector3(pitch, 0.0, 0.0)
	_camera.position = target + Vector3(0.0, 0.0, 0.0) \
		+ Vector3(0.0, cos(deg_to_rad(_tilt_degrees)), sin(deg_to_rad(_tilt_degrees))) * 100.0


func _unhandled_input(event: InputEvent) -> void:
	if Engine.is_editor_hint() or not event.is_pressed():
		return
	var changed := true
	if event.is_action("lab_tilt_up"):
		_tilt_degrees = minf(_tilt_degrees + 2.5, 45.0)
	elif event.is_action("lab_tilt_down"):
		_tilt_degrees = maxf(_tilt_degrees - 2.5, 0.0)
	elif event.is_action("lab_zoom_in"):
		_ortho_size = maxf(_ortho_size - 1.0, 2.0)
	elif event.is_action("lab_zoom_out"):
		_ortho_size = minf(_ortho_size + 1.0, 60.0)
	elif event.is_action("lab_next"):
		_focus = wrapi(_focus + 1, 0, maxi(_stations.size(), 1))
	elif event.is_action("lab_prev"):
		_focus = wrapi(_focus - 1, 0, maxi(_stations.size(), 1))
	elif event.is_action("lab_toggle_overview"):
		_overview = not _overview
	else:
		changed = false
	if changed:
		_apply_camera()
		_update_readout()
		get_viewport().set_input_as_handled()


func _update_readout() -> void:
	if _readout == null:
		return
	var built := 0
	for s in _stations:
		if s["built"]:
			built += 1
	var focused := "—"
	if not _overview and _focus < _stations.size():
		focused = _stations[_focus]["name"]
	_readout.text = "\n".join([
		"tilt %.1f deg off straight down   [ ]  to change" % _tilt_degrees,
		"ortho size %.0f m   - +  to zoom" % _camera.size,
		"%s   left/right to walk the board   space for overview" % focused,
		"%d of %d assets built" % [built, _stations.size()],
		"cyan block = 1.75 m reference person",
	])
