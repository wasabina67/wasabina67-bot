#!/bin/bash

isort src/run.py
black src/run.py
flake8 src/run.py
mypy src/run.py
