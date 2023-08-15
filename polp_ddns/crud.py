
from sqlalchemy.orm import Session

from . import models, schemas


def get_machine_by_name(db: Session, name: str):
    return db.query(models.Machine).filter(models.Machine.name == name).one()

def create_machine(db: Session, machine: schemas.MachineCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_machine = models.Machine(
        **machine.dict(),
        update_token=hashed_token,
    )
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine
