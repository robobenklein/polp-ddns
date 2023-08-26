
from typing import Annotated
import ipaddress

import sqlalchemy.exc
from sqlalchemy.orm import Session
from fastapi import (
    APIRouter, Depends, HTTPException, Response, Request, status, Header,
)

from .. import log, database, models, schemas, crud
# from ..utils import ip_in_private_range


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
        request: Request,
        response: Response,
        db: Session = Depends(database.get_db),
    ) -> schemas.MachineUpdateReport:
    try:
        machine = crud.get_machine_by_name(db, machine_name)
    except sqlalchemy.exc.NoResultFound as e:
        raise HTTPException(404, "machine not found")

    # TODO move machine token auth to a decorator or dependency?
    if token != machine.update_token:
        raise HTTPException(401, "invalid token")

    if not machine.is_active:
        raise HTTPException(403, "machine not enabled")

    # TODO what if this is a hostname and not IP? or None?
    if not request.client.host:
        raise HTTPException(500, "could not find client address")

    client_ip = ipaddress.ip_address(request.client.host)

    # If the request comes from a private range, look for a forwarded IP header
    is_private_ip = client_ip.is_private
    log.debug(f"Request client: {request.client} (private: {is_private_ip})")

    if is_private_ip:
        if 'X-Forwarded-For' in request.headers:
            forwarded_for = request.headers['X-Forwarded-For']
            log.debug(f"Using X-Forwarded-For header: {forwarded_for}")
            # in most cases should be handled by the ASGI/WSGI
            raise NotImplementedError()
        else:
            log.warn(f"Private IP detected for update request.")
            # client_ip = ipaddress.ip_address(request.client.host)
    # else:
    #     client_ip = ipaddress.ip_address(request.client.host)

    # TODO update all records assigned to machine

    return {
        "machine": machine,
        "records": [],
    }
