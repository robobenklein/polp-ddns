
from .. import log

import mongoengine
from mongoengine.errors import DoesNotExist
from flask import (
    Blueprint, g, redirect, request, session, url_for, abort
)

bp = Blueprint('machine', __name__, url_prefix='/machine')

@bp.route('/<machine_id>/update/<token>')
def update_machine_records(machine_id, token):
    pass

    # TODO fetch machine by id

    # TODO auth machine by token

    # TODO update all records assigned to machine
