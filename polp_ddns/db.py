
from . import log
from .app import app

import os
import pymongo
import mongoengine
from mongoengine import Document
from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required

app.config['MONGODB_SETTINGS'] = {
    'connect': False,
    'db': os.environ.get('POLPDDNS_DB', 'polp_ddns'),
    'host': os.environ.get('POLPDDNS_DB_HOST', 'localhost'),
    'port': int(os.environ.get('POLPDDNS_DB_PORT', '27017'))
}

db = MongoEngine(app)

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=255, unique=True)
    description = db.StringField(max_length=2048)
    permissions = db.StringField(default="")

class User(db.Document, UserMixin):
    username = db.StringField(max_length=255, required=True, unique=True)
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=512, required=True)
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])

user_datastore = MongoEngineUserDatastore(db, User, Role)

class Machine(db.Document):
    machine_id = db.StringField(unique=True, required=True)
    owner = db.LazyReferenceField(User)

class DDNSRecord(db.Document):
    user = db.LazyReferenceField(User)
    provider = db.LazyReferenceField('DNSProvider', required=True, passthrough=True)
    machine = db.LazyReferenceField(Machine, passthrough=True)
