

setup-evnironment:
	python3 -m virtualenv env
	source env/bin/activate; \
	pip install -r starter/requirements.txt; \