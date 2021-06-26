.PHONY: install
install: build
	pip install --upgrade -e .

.PHONY: build
build:
	coconut setup.coco --strict
	coconut pyprover-source pyprover --strict --jobs sys

.PHONY: upload
upload: clean install
	python3 setup.py sdist bdist_wheel
	pip3 install --upgrade twine
	twine upload dist/*

.PHONY: setup
setup:
	pip install --upgrade setuptools pip
	pip install --upgrade "coconut-develop[watch]"

.PHONY: test
test: install
	python pyprover/tests.py

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: wipe
wipe: clean
	find . -name '*.py' -delete
	rm -rf ./pyprover

.PHONY: watch
watch: install
	coconut pyprover-source pyprover --watch --strict
