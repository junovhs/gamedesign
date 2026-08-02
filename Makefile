GOXEL_PALETTES := $(HOME)/.config/goxel/palettes

.PHONY: help task list status guides build strict lab editor manifest palette shot check

help:
	@echo "  make task       what to build next, in full"
	@echo "  make list       the whole asset board with status"
	@echo "  make build      verify and export every authored asset to Godot"
	@echo "  make lab        open the scale lab"
	@echo "  make editor     open the Godot editor"
	@echo ""
	@echo "  make guides     regenerate goxel starting files from art/assets.json"
	@echo "  make manifest   republish art/assets.json into the Godot project"
	@echo "  make palette    install the game palette into goxel"
	@echo "  make strict     build, failing on any off-palette colour"
	@echo "  make shot       render the lab to lab.png without opening a window"
	@echo "  make check      guides + manifest + strict build"

task:
	@python3 tools/task.py next

list:
	@python3 tools/task.py list

status:
	@python3 tools/task.py status

guides:
	@python3 tools/make_guides.py

manifest:
	@python3 tools/gen_lab.py

build: manifest
	@python3 tools/build.py

strict: manifest
	@python3 tools/build.py --strict

lab: manifest
	@godot --path game res://scenes/lab/scale_lab.tscn

editor:
	@godot --path game --editor

shot: manifest
	@godot --path game -s res://tools/capture.gd -- res://scenes/lab/scale_lab.tscn lab.png 40

palette:
	@mkdir -p $(GOXEL_PALETTES)
	@cp art/templates/grapeghost.gpl $(GOXEL_PALETTES)/
	@echo "installed -> $(GOXEL_PALETTES)/grapeghost.gpl (restart goxel)"

check: guides manifest strict
