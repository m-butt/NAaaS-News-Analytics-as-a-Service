install:
	pip install	--upgrade pip && pip install -r requirements.txt

format: 
	black *.py
lint:
	pylint --disable=R,C Test.py
test:
	python -m pytest  -vv --cov=test Test.py
	coverage xml -o coverage.xml
