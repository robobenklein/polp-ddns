
from polp_ddns import log

reload = True
pidfile = "gunicorn.pid"
bind = ['unix:local-server.sock', '0.0.0.0:5000']
worker_class = "gthread"
workers = 8

def on_reload(server):
    log.info("gunicorn reload")

def when_ready(server):
    log.info("gunicorn ready")

def on_exit(server):
    log.info("gunicorn exit")
