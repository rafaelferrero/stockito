#!/usr/bin/env bash

rm -r stockito/almacenes/migrations
rm -r stockito/documentos/migrations
rm -r stockito/entidades/migrations
rm stockito/db.sqlite3

./stockito/manage.py makemigrations almacenes
./stockito/manage.py makemigrations documentos
./stockito/manage.py makemigrations entidades
./stockito/manage.py migrate

./stockito/manage.py loaddata stockito/statics/user.json
./stockito/manage.py loaddata stockito/statics/proveedor.json
./stockito/manage.py loaddata stockito/statics/articulo.json

./stockito/manage.py runserver



