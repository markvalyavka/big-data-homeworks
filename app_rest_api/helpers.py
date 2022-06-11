from cassandra_client import cs


FRAUD_USER_TRANSACTIONS_STMT = """
    SELECT * from user_by_is_fraud WHERE nameOrig = %s AND isFraud = 1;
"""


def get_fraud_user_tx(uid):

    fraud_users = cs.session.execute(
        FRAUD_USER_TRANSACTIONS_STMT, [uid]
    ).all()
    return fraud_users
