build_all:
	@echo "Django Console Building Started!"
	python setup.py check
	python setup.py sdist


upload:
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	@echo "Uploading built package..."
	python setup.py sdist upload


clean:
	@echo "Cleaning..."
	rm -rf mirage_framework.egg-info/
	rm -rf dist/

rebuild:
	@echo "Removing recent buildings..."
	rm -rf dist/
	@echo "Building MIRAGE Framework..."
	python setup.py check
	python setup.py sdist
	pip uninstall mirage-framework
	pip install dist/mirage-framework-0.0.1.tar.gz

export-requirements:
	pipenv lock -r > requirements.txt
