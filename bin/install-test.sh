#!/bin/bash -e
pip uninstall -y ansible-ssh
pip install --index-url https://test.pypi.org/simple/ ansible-ssh