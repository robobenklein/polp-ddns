
from .app import app
from . import db, log, utils

from flask import render_template, g
from flask_security import Security, current_user

app.config['SECURITY_PASSWORD_SALT'] = "07JDW05Kpg1Ika2WTdaxWFWbLgypOy"
app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = ('username','email')
security = Security(app, db.user_datastore)

@app.before_request
def add_user_context():
    if current_user.is_authenticated:
        g.user = db.user_datastore.find_user(username=current_user.username)
    else:
        g.user = None

@app.before_first_request
def add_initial_user():
    usercount = db.User.objects().count()
    log.debug(f"{usercount} users in database")
    if usercount == 0:
        log.warn("Creating initial admin user")
        db.user_datastore.create_user(
            username="admin",
            password="admin"
        )
