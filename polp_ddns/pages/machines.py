
from .. import log
from .. import db
from ..utils import force_nocache_response

import re
import traceback
import datetime

import mongoengine
from mongoengine.errors import DoesNotExist
from jinja2.exceptions import (TemplateNotFound, )
from flask_security import login_required, current_user
from flask import (
    Blueprint, flash, g, redirect, render_template, session, url_for, abort
)

bp = Blueprint('machines', __name__, url_prefix='/machines')

@bp.after_request
def add_cache_control_header(response):
    if 'Cache-Control' not in response.headers:
        force_nocache_response(response)
    return response

@bp.route('/')
@login_required
def machine_index():
    user = db.user_datastore.find_user(username=current_user.username)
    all_machines = db.Machine.objects()

    return render_template('machines/list.html', data={
        "machines": all_machines,
    })
