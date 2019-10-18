#!/bin/bash
python -m pip install --upgrade twine
cd ../
python -m twine upload --username aytuncbeken --repository-url https://test.pypi.org/legacy/ dist/*