
from pprint import pprint
from pathlib import Path

import click

from . import database, models, schemas, crud

db = next(database.get_db())


@click.group()
def main():
    pass

@main.group()
def machine():
    pass

@machine.command(name="list")
def list_machines():
    for m in db.query(models.Machine).all():
        pprint(schemas.Machine.model_validate(m))

@machine.command(name="new")
@click.argument('machine_name')
def new_machine(machine_name: str):
    new_machine = crud.create_machine(
        db,
        schemas.MachineCreate(
            name=machine_name,
        )
    )
    pprint(new_machine)

if __name__ == "__main__":
    main()
