#!/bin/bash
source ./venv/bin/activate

export FLASK_ENV=development
export FLASK_APP=polp_ddns
export FLASK_DEBUG=1
echo "running flask built in server..."
flask run $@
