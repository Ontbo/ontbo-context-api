# Makefile
VENV := .venv
PYTHON := python3
PIP := $(VENV)/bin/pip

.PHONY: init install clean

init:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install build twine pytest

install:
	$(PIP) install -e .

clean:
	rm -rf $(VENV) dist build *.egg-info