extends Node3D
## Stages one asset on a ground field, at the real game camera and resolution.
##
## Nothing in this game can be judged in isolation. A ground tile has to be seen
## as a field to know whether it seams or stamps; a character has to be seen
## standing on that ground, next to a known-size reference, to know whether it
## reads. This scene does both.
##
##   godot --path game -s res://tools/capture.gd -- \
##       res://scenes/lab/tile_field.tscn out.png 40 <subject> [tilt] [rotate] [ground]
##
## If <subject> is the ground asset itself, the field alone is rendered.

const MODEL_DIR := "res://assets/models/"
const FIELD := 12          ## metres per side of the ground field
const DEFAULT_TILT := 15.0
const DEFAULT_GROUND := "ground_grass_1x1m"

## Where subject copies stand, in metres from the field's near-left corner.
const SUBJECT_SPOTS := [
	Vector3(4.0, 0.0, -6.0),
	Vector3(6.0, 0.0, -6.0),
	Vector3(8.0, 0.0, -4.0),
]
## A 1.75 x 0.625 x 0.5 m block beside the subjects: the spec's declared human
## volume, so the real asset can be checked against the number it must hit.
const REFERENCE_SPOT := Vector3(2.0, 0.0, -6.0)

@onready var _camera: Camera3D = $Camera3D

var _random_rotation := false


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var subject: String = args[3] if args.size() > 3 else ""
	var tilt: float = float(args[4]) if args.size() > 4 else DEFAULT_TILT
	_random_rotation = args.size() > 5 and args[5] == "rotate"
	var ground: String = args[6] if args.size() > 6 else DEFAULT_GROUND

	if subject.is_empty():
		push_error("tile_field needs a subject asset name as the 4th user arg")
		return

	var ground_scene := _load(ground)
	if ground_scene:
		_lay_field(ground_scene)

	if subject != ground:
		var subject_scene := _load(subject)
		if subject_scene == null:
			push_error("no model for subject %s — run tools/build.py first" % subject)
			return
		for spot in SUBJECT_SPOTS:
			var node := subject_scene.instantiate()
			node.position = spot
			$Field.add_child(node)
		_add_reference()

	_aim_camera(tilt)


func _load(asset_name: String) -> PackedScene:
	var path := MODEL_DIR + asset_name + ".gltf"
	return load(path) if ResourceLoader.exists(path) else null


func _lay_field(packed: PackedScene) -> void:
	# Corner-pivoted tiles occupy x in [i, i+1] and z in [-j-1, -j]. With
	# random_rotation each is spun in 90-degree steps about its own centre,
	# which is how ground actually gets placed in game and the cheapest test of
	# whether a tile's variation reads as texture or as a repeating stamp.
	var rng := RandomNumberGenerator.new()
	rng.seed = 20260802
	for i in FIELD:
		for j in FIELD:
			var holder := Node3D.new()
			holder.position = Vector3(i + 0.5, 0.0, -j - 0.5)
			if _random_rotation:
				holder.rotation_degrees = Vector3(0, 90 * rng.randi_range(0, 3), 0)
			var tile := packed.instantiate()
			tile.position = Vector3(-0.5, 0.0, 0.5)
			holder.add_child(tile)
			$Field.add_child(holder)


func _add_reference() -> void:
	var node := MeshInstance3D.new()
	node.name = "SpecReference"
	var mesh := BoxMesh.new()
	mesh.size = Vector3(0.625, 1.75, 0.5)
	node.mesh = mesh
	node.position = REFERENCE_SPOT + Vector3(0, 0.875, 0)
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.86, 0.24, 0.2)
	node.material_override = mat
	$Field.add_child(node)


func _aim_camera(tilt: float) -> void:
	var centre := Vector3(FIELD * 0.5, 0.0, -FIELD * 0.5)
	_camera.projection = Camera3D.PROJECTION_ORTHOGONAL
	_camera.size = FIELD + 2.0
	_camera.near = 0.05
	_camera.far = 400.0
	_camera.rotation_degrees = Vector3(-(90.0 - tilt), 0.0, 0.0)
	_camera.position = centre + Vector3(
		0.0, cos(deg_to_rad(tilt)), sin(deg_to_rad(tilt))
	) * 100.0
