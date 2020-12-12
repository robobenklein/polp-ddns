#!/bin/bash
source ./venv/bin/activate
export FLASK_ENV=prod
export FLASK_DEBUG=0
gunicorn --forwarded-allow-ips='*' "polp_ddns" -c gunicorn-config.py
