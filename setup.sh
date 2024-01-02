#!/bin/bash
mkdir ./configs
python -m venv .venv
./.venv/bin/activate
pip install jinja2
deactivate
