#!/bin/sh

# Apply database migrations
python src/manage.py makemigrations
python src/manage.py migrate --fake-initial

# Start the server
exec python src/manage.py "$@"