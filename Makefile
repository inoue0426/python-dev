.PHONY: install-dev lint type deadcode test coverage check

install-dev:
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

lint:
	ruff check .

type:
	mypy .

deadcode:
	ruff check .
	mypy .
	vulture . vulture_whitelist.py

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report -m

check: lint type deadcode
