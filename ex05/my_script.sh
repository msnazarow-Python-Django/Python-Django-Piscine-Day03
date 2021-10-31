#!/bin/sh

python3 -m venv django_venv
. django_venv/bin/activate

pip --version

pip install -r requirement.txt

./manange.py makemigrations
./manange.py migrate
./manange.py runserver