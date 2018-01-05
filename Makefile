PYTHON?=$(shell which python)

record:
	$(PYTHON) Record.py

play:
	$(PYTHON) Play.py

graph:
	$(PYTHON) ShowGraph.py
