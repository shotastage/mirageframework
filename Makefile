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
	rm -rf django_mirage.egg-info/
	rm -rf dist/
	rm -rf testing/

pyclean:
	find ./mirageconsole -name '*.pyc' -delete -not -path './mirage/scaffold/static/'
	find ./mirageframework -name '*.pyc' -delete -not -path './mirage/scaffold/static/'


test:
	@echo "Removing recent buildings..."
	rm -rf dist/
	@echo "Building Django Console..."
	python setup.py check
	python setup.py sdist
	pip uninstall django-mirage
	pip install dist/django-mirage-0.1.5.tar.gz
