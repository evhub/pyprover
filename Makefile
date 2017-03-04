.PHONY: install
install: build
	pip install -e .

.PHONY: build
build:
	coconut setup.coco -s
	coconut pyprover -s -j sys

clean:
	find . -name "*.py" -delete
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: test
test:
	python pyprover/tests.py
