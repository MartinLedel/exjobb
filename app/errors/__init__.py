"""
Create errors Blurprint
"""
from flask import Blueprint

bp = Blueprint('errors', __name__)


# pylint: disable=wrong-import-position, cyclic-import
from app.errors import handlers  # noqa: E402, F401
