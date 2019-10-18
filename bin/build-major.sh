#!/bin/bash -e
python -m pip install setuptools wheel bumpversion
cd ../
bumpversion major --allow-dirty
python setup.py sdist bdist_wheel
