
import secrets

from . import log
from .app import app

log.info("Getting SESSIONKEY...")
try:
    f = open('secrets/sessionkey', 'rb')
    key = f.read() # bytes
    f.close()
    if len(key) <= 8:
        raise ValueError("Not enough bytes in sessionkey")
    app.config["SECRET_KEY"] = key
except FileNotFoundError as e:
    log.warn("Creating new sessionkey")
    key = secrets.token_bytes(16)
    f = open('secrets/sessionkey', 'wb+')
    f.write(key)
    f.close()
    app.config["SECRET_KEY"] = key
except Exception as e:
    log.crit("Failed to get a Flask sessionkey")
    raise e
