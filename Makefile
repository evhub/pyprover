# Coconut compilation flags: target Python 3.9+, be strict about style, and
#  skip tail call optimization (which isn't needed and slows things down).
COCONUT_FLAGS = --target 3.9 --strict --no-tco --jobs sys

.PHONY: setup
setup:
	python -m pip install --upgrade pip
	python -m pip install --upgrade "coconut-develop==3.2.0.post0.dev19" pytest

.PHONY: build
build:
	coconut pyprover --force $(COCONUT_FLAGS)

.PHONY: install
install: build
	python -m pip install --upgrade -e .

.PHONY: test
test: install
	python -m pytest

# test the committed compiled Python without recompiling
.PHONY: test-installed
test-installed:
	python -m pip install --upgrade .
	python -m pytest

.PHONY: watch
watch:
	coconut pyprover --watch $(COCONUT_FLAGS)

.PHONY: package
package: clean
	python -m pip install --upgrade build
	python -m build

.PHONY: upload
upload: package
	python -m pip install --upgrade twine
	twine upload dist/*

.PHONY: clean
clean:
	rm -rf ./dist ./build ./*.egg-info
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
