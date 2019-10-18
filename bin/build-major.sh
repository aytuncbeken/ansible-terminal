#!/bin/bash
python -m pip install setuptools wheel bumpversion
cd ../
bumpversion minor
python setup.py sdist bdist_wheel
