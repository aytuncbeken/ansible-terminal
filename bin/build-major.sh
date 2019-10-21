#!/bin/bash -e
python -m pip install setuptools wheel bumpversion
cd ../
bumpversion major --allow-dirty

# shellcheck disable=SC2035
rm -rf *.egg-info
rm -rf build
rm -rf dist

python setup.py sdist bdist_wheel
