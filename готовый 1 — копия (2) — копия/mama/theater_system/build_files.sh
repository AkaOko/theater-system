#!/bin/bash
cd "$(dirname "$0")"
python manage.py collectstatic --noinput 