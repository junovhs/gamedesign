.PHONY: help editor

help:
	@echo "  make editor     open the Godot editor"
	@echo ""
	@echo "  The sprite editor's commands arrive with TOOL-03, when it becomes"
	@echo "  a TypeScript app. Until then it is a single HTML file: open"
	@echo "  image-to-sprite-editor-liquify-v2.html in a browser."
	@echo ""
	@echo "  What to work on next:  ishoo plan show"

editor:
	@godot --path game --editor
