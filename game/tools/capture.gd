extends SceneTree
## Render a scene to a PNG so changes can be verified without a human at the screen.
##
##   godot --path game -s res://tools/capture.gd -- <scene> <out.png> [frames]
##
## Runs the real main viewport at the project's 640x360 render size, so what it
## captures is what the game actually looks like.

const DEFAULT_FRAMES := 20


func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() < 2:
		push_error("usage: capture.gd -- <scene> <out.png> [frames]")
		quit(2)
		return

	var scene_path: String = args[0]
	var out_path: String = args[1]
	var frames: int = int(args[2]) if args.size() > 2 else DEFAULT_FRAMES

	var packed: PackedScene = load(scene_path)
	if packed == null:
		push_error("could not load %s" % scene_path)
		quit(3)
		return

	root.add_child(packed.instantiate())
	_capture(out_path, frames)


func _capture(out_path: String, frames: int) -> void:
	# Let the scene build, light and settle before grabbing the frame.
	for _i in frames:
		await process_frame
	await RenderingServer.frame_post_draw

	var image := root.get_texture().get_image()
	var err := image.save_png(out_path)
	if err != OK:
		push_error("save_png(%s) failed: %d" % [out_path, err])
		quit(4)
		return
	print("captured %dx%d -> %s" % [image.get_width(), image.get_height(), out_path])
	quit(0)
