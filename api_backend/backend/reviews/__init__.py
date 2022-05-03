from flask import Blueprint

reviews = Blueprint(
    "reviews",
    __name__,
    url_prefix="/reviews"
)

from .views import *
