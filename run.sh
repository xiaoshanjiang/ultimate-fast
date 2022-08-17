#!/bin/sh

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

# add app to pythonpath
export PYTHONPATH="${PWD}/app":$PYTHONPATH

exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"
