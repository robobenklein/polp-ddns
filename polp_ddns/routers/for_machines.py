
import sqlalchemy.exc
from sqlalchemy.orm import Session
from fastapi import (
    APIRouter, Depends, HTTPException, Response, status,
)

from .. import log, database, models, schemas, crud


router = APIRouter(
    prefix='/machine'
)


@router.post(
    '/{machine_name}/update/{token}',
    responses={
        404: {
            "description": "Machine not found.",
            "model": schemas.HTTPError,
        },
        401: {
            "description": "Invalid token.",
            "model": schemas.HTTPError,
        },
    }
)
def update_machine_records(
        machine_name: str,
        token: str,
        # machine_update_options:
        response: Response,
        db: Session = Depends(database.get_db),
    ) -> schemas.MachineUpdateReport:
    try:
        machine = crud.get_machine_by_name(db, machine_name)
    except sqlalchemy.exc.NoResultFound as e:
        raise HTTPException(404, "machine not found")

    # TODO auth machine by token
    if token != machine.update_token:
        raise HTTPException(401, "invalid token")

    # TODO update all records assigned to machine

    return {
        "machine": machine,
        "records": [],
    }
