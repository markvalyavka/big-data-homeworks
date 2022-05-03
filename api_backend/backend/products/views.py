import json

from flask import request

from backend.products import products
from backend.products import helpers


@products.route("/", methods=["POST"])
def get_products():
    request_params = request.get_json()
    if not request_params:
        return "BAD REQUEST", 400

    by_filters = request_params.get("by_filters")
    if not by_filters:
        return "BAD REQUEST", 400
    limit = request_params.get("limit")

    products_ = helpers.get_products(by_filters, limit)
    return json.dumps({
        "result": products_
    }), 200
