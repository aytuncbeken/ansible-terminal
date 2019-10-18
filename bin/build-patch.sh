#!/bin/bash
python -m pip install setuptools wheel bumpversion
cd ../
bumpversion patch --allow-dirty
python setup.py sdist bdist_wheel
