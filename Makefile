# context project makefile

# help
help:
	@echo "Available targets:"
	@echo "  install    Install dependencies"
	@echo "  clean      Clean up"
	@echo "  help       Show this help"

# install dependencies
install:
	uv venv && source .venv/bin/activate
	uv sync
	crawl4ai-setup
	crawl4ai-doctor

# clean
clean:
	rm -rf .venv
	rm -rf .crawl4ai
	rm -rf .cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache

.PHONY: install clean