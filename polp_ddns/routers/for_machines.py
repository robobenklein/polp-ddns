
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import log, database, models, schemas, crud


router = APIRouter(
    prefix='/machine'
)


@router.post('/{machine_name}/update/{token}')
def update_machine_records(
        machine_name: str,
        token: str,
        # machine_update_options:
        db: Session = Depends(database.get_db),
    ) -> schemas.MachineUpdateReport:
    machine = crud.get_machine_by_name(db, machine_name)

    # TODO fetch machine by id

    # TODO auth machine by token

    # TODO update all records assigned to machine

    return {
        "machine": machine,
        "records": [],
    }
