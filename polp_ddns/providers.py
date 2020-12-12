
from .db import db

class DNSProvider(db.Document):
    meta = {
        "allow_inheritance": True
    }
    user = db.LazyReferenceField(User)
    identifier = db.StringField(max_length=512, required=True)
    description = db.StringField()

    def update_record(name: str, new_address: str, record_type: str = None):
        raise NotImplementedError()

    def get_record(name: str, type: str):
        raise NotImplementedError()

class CloudflareProvider(DNSProvider):
    cf_auth_token = db.StringField(required=True)
