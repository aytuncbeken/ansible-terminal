#!/bin/bash
python -m pip install setuptools wheel bumpversion setupext-janitor
cd ../
rm -rf *.egg-info
rm -rf build
rm -rf dist

python setup.py sdist bdist_wheel
pip install ./dist/*.gz
ansible-ssh
