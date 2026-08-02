extends Node3D
## The scale-lock test scene from the brief: one assembled corner of the world.
##
## A row of objects cannot answer "do interiors feel right?", "is the doorway
## obvious?" or "do walls hide the activity behind them?". Those need a built
## space. So this assembles a house, a street cross-section and a yard at the
## exact dimensions in docs/SCALE.md.
##
## Anything with a finished model uses it. Everything else is a flat-coloured
## box at its exact specified size, so the scene is useful now and improves as
## assets land rather than waiting on all of them.
##
##   godot --path game -s res://tools/capture.gd -- \
##       res://scenes/lab/test_room.tscn out.png 60 [tilt] [yaw] [roof] [zoom]

const MODEL_DIR := "res://assets/models/"
const PALETTE := "res://assets/palette.json"

const WALL_H := 2.75          ## docs/SCALE.md section 5
const WALL_EXT := 0.25
const WALL_INT := 0.125
const SLAB := 0.25

## House occupies x 0..7, z -12..-3. Street runs along +z from the front yard.
const HOUSE := Rect2(0, -12, 7, 9)
const CORRIDOR_X := 5.25       ## interior wall splitting rooms from the corridor
const SPLIT_Z := -7.5          ## interior wall splitting front room from bedroom

var _palette := {}
var _sun: DirectionalLight3D
var _roof: Node3D


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var tilt: float = float(args[3]) if args.size() > 3 else 35.0
	var yaw: float = float(args[4]) if args.size() > 4 else 0.0
	var roof_on: bool = args.size() > 5 and args[5] == "roof"
	var zoom: float = float(args[6]) if args.size() > 6 else 16.0

	_load_palette()
	_build_ground()
	_build_street()
	_build_house()
	_build_furniture()
	_build_yard()
	_build_destruction_test()
	_place_people()
	_roof.visible = roof_on
	_aim_camera(tilt, yaw, zoom)


func _load_palette() -> void:
	var text := FileAccess.get_file_as_string(PALETTE)
	var doc: Variant = JSON.parse_string(text)
	if typeof(doc) == TYPE_DICTIONARY:
		for name in doc["palette"]:
			_palette[name] = Color(doc["palette"][name])


# -- primitives ------------------------------------------------------------


func _colour(name: String) -> Color:
	return _palette.get(name, Color.MAGENTA)


func _box(parent: Node3D, pos: Vector3, size: Vector3, colour: String) -> MeshInstance3D:
	## pos is the minimum corner; the box grows +x, +y, +z from there.
	var node := MeshInstance3D.new()
	var mesh := BoxMesh.new()
	mesh.size = size
	node.mesh = mesh
	node.position = pos + size * 0.5
	var mat := StandardMaterial3D.new()
	mat.albedo_color = _colour(colour)
	mat.roughness = 0.95
	mat.metallic = 0.0
	node.material_override = mat
	parent.add_child(node)
	return node


func _model(asset_name: String) -> PackedScene:
	var path := MODEL_DIR + asset_name + ".gltf"
	return load(path) if ResourceLoader.exists(path) else null


# -- construction ----------------------------------------------------------


func _build_ground() -> void:
	var root := $Ground
	var grass := _model("ground_grass_1x1m")
	if grass:
		# Real tiles across the lot, so ground is judged as authored art.
		for i in range(-7, 16):
			for j in range(-3, 15):
				var tile := grass.instantiate()
				tile.position = Vector3(i, 0, -j)
				root.add_child(tile)
	else:
		_box(root, Vector3(-6, 0, -14), Vector3(20, SLAB, 17), "grass")


func _build_street() -> void:
	var root := $Street
	# Cross-section from docs/SCALE.md section 7, front yard outward.
	_box(root, Vector3(-6, SLAB, 0.25), Vector3(20, 0.02, 1.5), "concrete")      # sidewalk
	_box(root, Vector3(-6, SLAB, 1.75), Vector3(20, 0.02, 0.25), "concrete_dark") # curb
	_box(root, Vector3(-6, 0.24, 2.0), Vector3(20, 0.02, 6.0), "asphalt")         # road
	_box(root, Vector3(7.5, SLAB, -3.0), Vector3(3.5, 0.02, 5.0), "asphalt_light")# driveway


func _build_house() -> void:
	var root := $House
	var x0: float = HOUSE.position.x
	var z0: float = HOUSE.position.y
	var w: float = HOUSE.size.x
	var d: float = HOUSE.size.y
	var z1 := z0 + d

	# Floor slab.
	_box(root, Vector3(x0, SLAB, z0), Vector3(w, 0.02, d), "wood_light")

	var y := SLAB
	# Back and side exterior walls are solid.
	_box(root, Vector3(x0, y, z0), Vector3(w, WALL_H, WALL_EXT), "bone")
	_box(root, Vector3(x0, y, z0), Vector3(WALL_EXT, WALL_H, d), "bone")
	_box(root, Vector3(x0 + w - WALL_EXT, y, z0), Vector3(WALL_EXT, WALL_H, d), "bone")

	# Front wall, punched for a 1 m doorway into the corridor and a 1 m window.
	# Built as segments because the openings are what the scene exists to test.
	var door_x := 5.5
	var win_x := 1.0
	var fz := z1 - WALL_EXT
	_box(root, Vector3(x0, y, fz), Vector3(win_x, WALL_H, WALL_EXT), "bone")
	_box(root, Vector3(win_x, y, fz), Vector3(1.0, WALL_H, WALL_EXT), "bone")  # under sill
	_box(root, Vector3(win_x + 1.0, y, fz), Vector3(door_x - win_x - 1.0, WALL_H, WALL_EXT), "bone")
	_box(root, Vector3(door_x + 1.0, y, fz), Vector3(x0 + w - door_x - 1.0, WALL_H, WALL_EXT), "bone")
	# Lintel over the doorway, and the glazing + header over the window.
	_box(root, Vector3(door_x, y + 2.0, fz), Vector3(1.0, WALL_H - 2.0, WALL_EXT), "bone")
	_box(root, Vector3(win_x, y + 0.875, fz + 0.08), Vector3(1.0, 1.25, 0.08), "glass")
	_box(root, Vector3(win_x, y + 2.125, fz), Vector3(1.0, WALL_H - 2.125, WALL_EXT), "bone")

	# Interior wall: corridor down the right-hand side, 1.5 m wide.
	_box(root, Vector3(CORRIDOR_X, y, z0 + WALL_EXT), Vector3(WALL_INT, WALL_H, 1.5), "white")
	_box(root, Vector3(CORRIDOR_X, y, -6.0), Vector3(WALL_INT, WALL_H, 3.0), "white")
	_box(root, Vector3(CORRIDOR_X, y + 2.0, -7.0), Vector3(WALL_INT, 0.75, 1.0), "white")

	# Interior wall splitting front room from bedroom, with a 1 m doorway.
	_box(root, Vector3(x0 + WALL_EXT, y, SPLIT_Z), Vector3(1.0, WALL_H, WALL_INT), "white")
	_box(root, Vector3(2.25, y, SPLIT_Z), Vector3(CORRIDOR_X - 2.25, WALL_H, WALL_INT), "white")
	_box(root, Vector3(1.25, y + 2.0, SPLIT_Z), Vector3(1.0, 0.75, WALL_INT), "white")

	# Staircase in the corridor: 11 steps, 0.25 rise, 0.3125 run.
	for step in 11:
		_box(
			$House,
			Vector3(CORRIDOR_X + WALL_INT, SLAB + step * 0.25, -11.5 + step * 0.3125),
			Vector3(1.4, 0.25, 0.3125),
			"wood_mid",
		)

	# Cutaway roof — hidden by default. This is the thing the camera has to
	# solve, so it must be togglable rather than absent.
	_roof = Node3D.new()
	_roof.name = "Roof"
	add_child(_roof)
	_box(_roof, Vector3(x0 - 0.3, y + WALL_H, z0 - 0.3), Vector3(w + 0.6, 0.3, d + 0.6), "brick")


func _build_furniture() -> void:
	var root := $Furniture
	var f := SLAB

	# Front room: dining set and sofa.
	_box(root, Vector3(1.0, f + 0.6, -6.0), Vector3(1.0, 0.15, 1.5), "wood_mid")      # table top
	for leg in [Vector3(1.05, f, -5.95), Vector3(1.85, f, -5.95),
				Vector3(1.05, f, -4.65), Vector3(1.85, f, -4.65)]:
		_box(root, leg, Vector3(0.1, 0.6, 0.1), "wood_dark")
	for seat in [Vector3(0.4, f, -5.6), Vector3(2.1, f, -5.6),
				 Vector3(1.25, f, -6.8), Vector3(1.25, f, -4.3)]:
		_box(root, seat, Vector3(0.5, 0.5, 0.5), "wood_mid")
		_box(root, seat + Vector3(0, 0.5, 0), Vector3(0.5, 0.375, 0.12), "red")
	_box(root, Vector3(3.2, f, -4.0), Vector3(2.0, 0.5, 0.875), "red")                # sofa
	_box(root, Vector3(3.2, f + 0.5, -4.0), Vector3(2.0, 0.375, 0.25), "red")

	# Kitchen counter run along the dividing wall.
	_box(root, Vector3(0.5, f, -7.4), Vector3(3.0, 0.75, 0.625), "grey_dark")
	_box(root, Vector3(0.5, f + 0.75, -7.4), Vector3(3.0, 0.125, 0.625), "bone")

	# Bedroom.
	_box(root, Vector3(0.6, f, -11.0), Vector3(1.0, 0.5, 2.0), "blue")                # bed
	_box(root, Vector3(0.6, f + 0.5, -9.6), Vector3(1.0, 0.125, 0.4), "white")        # pillow
	_box(root, Vector3(3.4, f, -11.6), Vector3(1.0, 2.0, 0.625), "wood_mid")          # wardrobe


func _build_yard() -> void:
	var root := $Yard
	var g := SLAB

	# Fence along the left boundary, 1.25 m — chest height, climbable.
	for i in range(-12, 1):
		_box(root, Vector3(-1.0, g, float(i)), Vector3(0.1, 1.25, 0.9), "wood_light")
	# Hedge along the front boundary, 1.25 m and opaque.
	_box(root, Vector3(0.0, g, -2.6), Vector3(3.5, 1.25, 1.0), "foliage_dark")
	# Tree: trunk plus two canopy masses, never individual leaves.
	_box(root, Vector3(-3.2, g, -6.2), Vector3(0.5, 2.0, 0.5), "wood_dark")
	_box(root, Vector3(-4.2, g + 1.8, -7.2), Vector3(2.5, 1.4, 2.5), "foliage_dark")
	_box(root, Vector3(-3.9, g + 2.9, -6.9), Vector3(1.9, 1.0, 1.9), "foliage_light")
	# Mailbox and a car on the driveway.
	_box(root, Vector3(8.0, g, 0.2), Vector3(0.1, 0.75, 0.1), "wood_dark")
	_box(root, Vector3(7.8, g + 0.75, 0.05), Vector3(0.5, 0.375, 0.4), "red")
	_car(root, Vector3(8.4, g, -2.0))


func _car(root: Node3D, at: Vector3) -> void:
	_box(root, at, Vector3(1.75, 0.55, 4.0), "blue")
	_box(root, at + Vector3(0.1, 0.55, 0.9), Vector3(1.55, 0.5, 2.0), "glass")
	_box(root, at + Vector3(0.1, 1.05, 0.9), Vector3(1.55, 0.1, 2.0), "blue")
	for wheel in [Vector3(-0.05, 0, 0.4), Vector3(1.65, 0, 0.4),
				  Vector3(-0.05, 0, 2.9), Vector3(1.65, 0, 2.9)]:
		_box(root, at + wheel, Vector3(0.15, 0.45, 0.7), "ink")


func _build_destruction_test() -> void:
	## Intact and blown-out wall side by side, at identical footprint — the
	## whole Tier 2/3 mechanic is swapping one for the other.
	var root := $Destruction
	var y := SLAB
	_box(root, Vector3(12.0, y, -6.0), Vector3(1.0, WALL_H, WALL_EXT), "bone")
	_box(root, Vector3(13.5, y, -6.0), Vector3(1.0, 0.9, WALL_EXT), "bone")
	_box(root, Vector3(13.5, y + 0.9, -6.0), Vector3(0.4, 0.5, WALL_EXT), "bone")
	_box(root, Vector3(14.1, y + 0.9, -6.0), Vector3(0.25, 0.25, WALL_EXT), "bone")
	for i in 6:
		_box(
			root,
			Vector3(13.2 + randf() * 1.6, y, -5.6 + randf() * 0.8),
			Vector3(0.2, 0.15, 0.2),
			"grey_dark",
		)


func _place_people() -> void:
	var root := $People
	var packed := _model("char_civilian_base")
	# One indoors, one in the corridor, one on the sidewalk, one at the car —
	# the point is whether walls hide them, so put them behind walls.
	var spots := [
		Vector3(2.6, SLAB, -5.0),
		Vector3(6.0, SLAB, -5.5),
		Vector3(3.0, SLAB, 1.0),
		Vector3(7.6, SLAB, -1.0),
		Vector3(1.4, SLAB, -10.0),
	]
	for spot in spots:
		if packed:
			var node := packed.instantiate()
			node.position = spot
			root.add_child(node)
		else:
			_box(root, spot - Vector3(0.3, 0, 0.2), Vector3(0.625, 1.75, 0.375), "red")


func _aim_camera(tilt: float, yaw: float, zoom: float) -> void:
	var cam: Camera3D = $Camera3D
	var centre := Vector3(4.0, 1.2, -4.5)
	cam.projection = Camera3D.PROJECTION_ORTHOGONAL
	cam.size = zoom
	cam.near = 0.05
	cam.far = 400.0
	cam.rotation_degrees = Vector3(-(90.0 - tilt), yaw, 0.0)

	var t := deg_to_rad(tilt)
	var y := deg_to_rad(yaw)
	var dir := Vector3(sin(t) * sin(y), cos(t), sin(t) * cos(y))
	cam.position = centre + dir * 120.0
