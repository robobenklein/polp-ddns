#!/bin/bash
source ./venv/bin/activate

uvicorn --reload polp_ddns.main:app --port 5000 $@
