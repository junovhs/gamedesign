extends Node3D
## Lays one asset out as a field, at the real game camera and resolution.
##
## A ground or wall tile cannot be judged on its own — the questions that matter
## are "does it seam?", "is the colour right in bulk?" and "does a person read
## against it?". Those only have answers at 12 x 12 metres.
##
##   godot --path game -s res://tools/capture.gd -- \
##       res://scenes/lab/tile_field.tscn out.png 40 <asset_name> [tilt_degrees]

const MODEL_DIR := "res://assets/models/"
const FIELD := 12          ## tiles per side, and metres per side at 1 m tiles
const DEFAULT_TILT := 15.0

@onready var _camera: Camera3D = $Camera3D


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var asset_name: String = args[3] if args.size() > 3 else ""
	var tilt: float = float(args[4]) if args.size() > 4 else DEFAULT_TILT

	if asset_name.is_empty():
		push_error("tile_field needs an asset name as the 4th user arg")
		return

	var path := MODEL_DIR + asset_name + ".gltf"
	if not ResourceLoader.exists(path):
		push_error("no model at %s — run tools/build.py first" % path)
		return

	var packed: PackedScene = load(path)
	_lay_field(packed)
	_add_people()
	_aim_camera(tilt)


func _lay_field(packed: PackedScene) -> void:
	# Corner-pivoted tiles occupy x in [i, i+1] and z in [-j-1, -j].
	for i in FIELD:
		for j in FIELD:
			var tile := packed.instantiate()
			tile.position = Vector3(i, 0.0, -j)
			$Field.add_child(tile)


func _add_people() -> void:
	## Three 1.75 m figures, so bulk colour is judged against the thing that has
	## to stay readable on top of it.
	for spot in [Vector3(3.5, 0, -4.5), Vector3(7.5, 0, -7.5), Vector3(9.5, 0, -2.5)]:
		var node := MeshInstance3D.new()
		var mesh := BoxMesh.new()
		mesh.size = Vector3(0.625, 1.75, 0.5)
		node.mesh = mesh
		node.position = spot + Vector3(0, 0.875, 0)
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
