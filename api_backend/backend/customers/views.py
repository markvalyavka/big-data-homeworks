import json
from flask import request

from backend.customers import customers, helpers


@customers.route("/", methods=["POST"])
def get_customers():
    request_params = request.get_json()
    if not request_params:
        return "BAD REQUEST", 400

    by_filters = request_params.get("by_filters")
    if not by_filters:
        return "BAD REQUEST", 400
    limit = request_params.get("limit")

    customers_ = helpers.get_customers(by_filters, limit)
    return json.dumps({
        "result": customers_
    }), 200


