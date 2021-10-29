#!/bin/sh
#python3 -m venv local_lib/
#. local_lib/bin/activate
#pip --version
#pip install --log path_install.log --upgrade  git+https://github.com/jaraco/path.py.git
pip install --target local_lib --upgrade --log path_install.log --force-reinstall git+https://github.com/jaraco/path.git && python3 my_program.py
