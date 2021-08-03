build:
	pip install -r requirements.txt

test:
	pytest tests --cov=api

safe:
	safety check -r requirements.txt