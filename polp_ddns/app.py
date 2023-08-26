
from . import log, database, models
from fastapi import FastAPI

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

log.setLevel(log.DEBUG)
log.debug("logger set to debug")
