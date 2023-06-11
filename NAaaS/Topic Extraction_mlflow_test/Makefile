install:
	pip install	--upgrade pip && pip install -r requirements.txt

format: 
	black *.py
lint:
	pylint --disable=R,C Test.py || true
test:
	python -m pytest --cov=Test.py --cov-report=html
	coverage xml -o coverage.xml
