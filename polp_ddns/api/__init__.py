
from flask import Blueprint

from .machines import bp as v1_machines_bp

__all__ = [
    v1_machines_bp
]
