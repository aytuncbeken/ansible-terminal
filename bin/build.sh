#!/bin/bash
python -m pip install setuptools wheel
cd ../
python setup.py sdist bdist_wheel
