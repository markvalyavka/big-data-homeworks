"""Cassandra client."""
from retry import retry
from cassandra.cluster import NoHostAvailable

# (
#     step bigint,
#     type text,
#     amount float,
#     nameOrig text,
#     oldbalanceOrg float,
#     newbalanceOrig float,
#     nameDest text,
#     oldbalanceDest float,
#     newbalanceDest float,
#     isFraud int,
#     transactionDate date,
#     PRIMARY KEY ((nameOrig), isFraud)
# );

INSERT_USER_BY_IS_FRAUD_STMT = """
INSERT INTO user_by_is_fraud (step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest,
newbalanceDest, isFraud, transactionDate)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

INSERT_USER_BY_AMOUNT_STMT  = """
INSERT INTO user_by_amount (step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest,
newbalanceDest, isFraud, transactionDate)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

INSERT_USER_TRANSACTION_BY_DATE_STMT  = """
INSERT INTO user_transactions_by_date (step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest,
newbalanceDest, isFraud, transactionDate)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


class CassandraClient:
    def __init__(self):
        self._host = None
        self._port = None
        self._keyspace = None
        self._session = None

    @retry(NoHostAvailable, delay=25, tries=4)
    def init_app(self, host, port, keyspace):
        self._host = host
        self._port = port
        self._keyspace = keyspace
        print(self._port, self._host, self._keyspace)
        from cassandra.cluster import Cluster
        cluster = Cluster([self._host], port=self._port)
        self._session = cluster.connect(self._keyspace)
        print("Successfully connected to Cassandra. Session -> ", self._session)

    @property
    def session(self):
        return self._session

    def execute(self, query):
        return self._session.execute(query)

    def close(self):
        self._session.shutdown()


    def insert_into_user_by_is_fraud(self, row):
        try:
            vals = [
                int(row.value['step']), row.value['type'], float(row.value['amount']),
                row.value['nameOrig'], float(row.value['oldbalanceOrg']),
                float(row.value['newbalanceOrig']), row.value['nameDest'],
                float(row.value['oldbalanceDest']), float(row.value['newbalanceDest']),
                int(row.value['isFraud']), row.value['transactionDate'],
            ]
            self._session.execute(INSERT_USER_BY_IS_FRAUD_STMT, vals)
        except Exception as e:
            raise e
            return

    def insert_into_user_by_amount(self, row):
        try:
            vals = [
                int(row.value['step']), row.value['type'], float(row.value['amount']),
                row.value['nameOrig'], float(row.value['oldbalanceOrg']),
                float(row.value['newbalanceOrig']), row.value['nameDest'],
                float(row.value['oldbalanceDest']), float(row.value['newbalanceDest']),
                int(row.value['isFraud']), row.value['transactionDate'],
            ]
            self._session.execute(INSERT_USER_BY_AMOUNT_STMT, vals)
        except Exception as e:
            raise e
            return

    def insert_into_user_transactions_by_date(self, row):
        try:
            vals = [
                int(row.value['step']), row.value['type'], float(row.value['amount']),
                row.value['nameOrig'], float(row.value['oldbalanceOrg']),
                float(row.value['newbalanceOrig']), row.value['nameDest'],
                float(row.value['oldbalanceDest']), float(row.value['newbalanceDest']),
                int(row.value['isFraud']), row.value['transactionDate'],
            ]
            self._session.execute(INSERT_USER_TRANSACTION_BY_DATE_STMT, vals)
        except Exception as e:
            raise e
            return


cs = CassandraClient()