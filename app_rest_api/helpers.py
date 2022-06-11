from cassandra_client import cs


FRAUD_USER_TRANSACTIONS_STMT = """
    SELECT * from user_by_is_fraud WHERE nameOrig = %s AND isFraud = 1;
"""

TOP_3_BIGGEST_TRANSACTIONS_AMOUNT_STMT = """
    SELECT * from user_by_amount WHERE nameOrig = %s ORDER BY amount DESC LIMIT 3;
"""

ALL_USER_INCOMING_TX_STMT = """
    SELECT * from user_transactions_by_date 
    WHERE nameDest = %s AND transactionDate > %s AND transactionDate < %s ALLOW FILTERING;
"""


def get_fraud_user_tx(uid):
    fraud_users = cs.session.execute(
        FRAUD_USER_TRANSACTIONS_STMT, [uid]
    ).all()

    return [{
        **u._asdict(),
        'transactiondate': u.transactiondate.date().isoformat()
    } for u in fraud_users]


def get_top_user_w_tx_amount(uid):
    top_users_w_tx_amount = cs.session.execute(
        TOP_3_BIGGEST_TRANSACTIONS_AMOUNT_STMT, [uid]
    ).all()

    return [{
        **u._asdict(),
        'transactiondate': u.transactiondate.date().isoformat()
    } for u in top_users_w_tx_amount]


def get_incoming_tx_sum_for_user(uid, date_from, date_to):
    all_incoming_tx = cs.session.execute(
        ALL_USER_INCOMING_TX_STMT, [uid, date_from, date_to]
    )
    total_sum = sum([
        tx._asdict()['amount'] for tx in all_incoming_tx
    ])
    return {
        "user_ud": uid,
        "date_from": date_from,
        "date_to": date_to,
        "total_sum": total_sum,
    }
