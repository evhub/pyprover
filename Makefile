.PHONY: install
install: build
	pip install -e .

.PHONY: build
build:
	coconut setup.coco -sl
	coconut pyprover-source pyprover -sl -j sys

.PHONY: upload
upload: clean install
	python3 setup.py sdist bdist_wheel
	pip3 install --upgrade twine
	twine upload dist/*

.PHONY: setup
setup:
	pip install coconut-develop

.PHONY: test
test: install
	python pyprover/tests.py

clean:
	rm -rf ./dist ./build
	find . -name '*.py' -delete
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
