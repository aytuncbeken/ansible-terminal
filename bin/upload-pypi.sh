#!/bin/bash -e
python -m pip install --upgrade twine
cd ../
python -m twine upload --username aytuncbeken --repository-url https://pypi.org/legacy/ dist/*