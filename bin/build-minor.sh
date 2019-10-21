#!/bin/bash -e
python -m pip install setuptools wheel bumpversion
cd ../
bumpversion minor --allow-dirty
rm -rf *.egg-info
rm -rf build
rm -rf dist

python setup.py sdist bdist_wheel
