
from . import log
from flask import Flask

app = Flask("polp_ddns")

app.debug = app.config["DEBUG"]

if app.debug:
    log.setLevel(log.DEBUG)
    log.debug("logger set to debug")
