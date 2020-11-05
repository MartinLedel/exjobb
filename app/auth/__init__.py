"""
Create auth Blurprint
"""
from flask import Blueprint

bp = Blueprint('auth', __name__)


# pylint: disable=wrong-import-position, cyclic-import
from app.auth import routes  # noqa: E402, F401
