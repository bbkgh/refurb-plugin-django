.PHONY: install ruff mypy black isort test self-test

all: ruff black isort test self-test

install:
	pip install .
	pip install -r dev-requirements.txt

ruff:
	ruff refurb_plugin_django test

mypy:
	mypy -p refurb_plugin_django
	mypy -p test --exclude "test/data/*"

black:
	black refurb_plugin_django test

isort:
	isort . --diff --check

test:
	pytest

self-test:
	refurb refurb_plugin_django
