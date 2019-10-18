#!/bin/bash
python -m pip install setuptools wheel bumpversion
cd ../
bumpversion major
python setup.py sdist bdist_wheel
