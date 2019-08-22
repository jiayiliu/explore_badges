#!/usr/bin/env bash

set -e 

flag=$(python -c 'import platform; major, minor, patch = platform.python_version_tuple();print(major=="3" and minor=="7")')

if [ $flag == "False" ]; then
  exit 0
fi

codecov

cd docs
pandoc ../README.md -o source/README.rst
make html