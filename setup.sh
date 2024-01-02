#!/bin/bash
mkdir ./configs
python -m venv .venv
source ./.venv/bin/activate
pip install jinja2
deactivate
