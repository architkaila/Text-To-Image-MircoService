setup:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black *.py
	black tests/*.py

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest -vv --cov=main tests/test_main.py

all: setup format lint test