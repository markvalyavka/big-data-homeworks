import json

from flask import Flask, request

import helpers
from cassandra_client import cs


app = Flask(__name__)
# load config
app.config.from_object('config.DebugConfig')
# init cassandra
cs.init_app(app)


@app.route("/")
@app.route("/_health")
def health():
    return "OK!"


@app.route("/users_fraud", methods=["GET"])
def get_fraud_user_tx():

    request_params = request.get_json()
    user_uid = request_params.get("uid")
    if not user_uid:
        return "BAD REQUEST", 400

    products_ = helpers.get_fraud_user_tx(user_uid)
    return json.dumps({
        "result": products_
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
