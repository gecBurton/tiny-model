build:
	pip install -r requirements.txt

test:
	pytest tests --cov=core

safe:
	safety check -r requirements.txt