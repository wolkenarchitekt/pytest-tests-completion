VIRTUALENV_DIR = .venv

virtualenv-create:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip install --upgrade pip setuptools && \
		pip install -r requirements.txt && \
		pip install -e .
	echo "Activate virtualenv: \n. $(VIRTUALENV_DIR)/bin/activate"
