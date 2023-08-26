
from fastapi import Depends, FastAPI

from .routers import for_machines

# app = FastAPI(dependencies=[Depends(get_query_token)])
from .app import app


app.include_router(for_machines.router)


@app.get("/")
async def root():
    return {"message": "sup"}
