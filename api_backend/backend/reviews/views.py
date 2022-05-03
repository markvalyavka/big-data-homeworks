import json
from flask import request

from backend.reviews import reviews, helpers


@reviews.route("/", methods=["POST"])
def get_reviews():

    request_params = request.get_json()
    if not request_params:
        return "BAD REQUEST", 400

    by_filters = request_params.get("by_filters")
    if not by_filters:
        return "BAD REQUEST", 400
    limit = request_params.get("limit")

    reviews_ = helpers.get_reviews(by_filters, limit)
    return json.dumps({
        "result": reviews_
    }), 200

