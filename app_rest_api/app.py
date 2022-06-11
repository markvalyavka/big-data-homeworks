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

    fraud_users = helpers.get_fraud_user_tx(user_uid)
    print(fraud_users, flush=True)
    return json.dumps({
        "result": fraud_users
    }), 200


@app.route("/users_top_tx", methods=["GET"])
def get_user_top_tx():

    request_params = request.get_json()
    user_uid = request_params.get("uid")
    if not user_uid:
        return "BAD REQUEST", 400

    top_tx = helpers.get_top_user_w_tx_amount(user_uid)
    print(top_tx, flush=True)
    return json.dumps({
        "result": top_tx
    }), 200


@app.route("/user_incoming_tx_sum", methods=["GET"])
def get_user_incoming_tx_sum():

    request_params = request.get_json()
    user_uid = request_params.get("uid")
    date_from = request_params.get("date_from")
    date_to = request_params.get("date_to")
    if not (user_uid and date_from and date_to):
        return "BAD REQUEST", 400

    tx_sum = helpers.get_incoming_tx_sum_for_user(user_uid, date_from, date_to)
    print(tx_sum, flush=True)
    return json.dumps({
        "result": tx_sum
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
