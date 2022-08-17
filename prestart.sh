#! /usr/bin/env bash

# add app to pythonpath
export PYTHONPATH="${PWD}/app":$PYTHONPATH

# Let the DB start
python3 ./app/backend_pre_start.py

# if you are not using alembic, uncomment the next line
# python3 ./app/db/init_db.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python3 ./app/initial_data.py
