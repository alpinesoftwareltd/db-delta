#!/bin/bash

python -m build
# upload to twine. overwrites existing files
twine upload dist/*
