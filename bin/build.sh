#!/bin/bash
python -m pip install setuptools wheel bumpversion
cd ../
python setup.py sdist bdist_wheel
