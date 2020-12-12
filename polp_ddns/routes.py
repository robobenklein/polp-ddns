
from flask import Flask, render_template
from flask_security import auth_required, login_required

from . import log
from .app import app
from . import db

from .pages.machines import bp as machines_bp
from .api import v1_machines_bp

### Views

@app.route('/')
def index():
    return 'Nothing here, move along.'

app.register_blueprint(machines_bp)

### API routes

app.register_blueprint(v1_machines_bp)
