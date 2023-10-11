#!/bin/sh

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

# export MODULE_PATH to import modules from anywhere
export PYTHONPATH="${PWD}":$PYTHONPATH

# tell python not to create __pycache__
export PYTHONDONTWRITEBYTECODE=1

exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"
