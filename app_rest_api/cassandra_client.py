"""Cassandra client."""
from retry import retry
from cassandra.cluster import NoHostAvailable


class CassandraClient:
    def __init__(self):
        self._host = None
        self._port = None
        self._keyspace = None
        self._session = None

    @retry(NoHostAvailable, delay=25, tries=4)
    def init_app(self, app):
        self._host = app.config['CASSANDRA_HOST']
        self._port = app.config['CASSANDRA_PORT']
        self._keyspace = app.config['CASSANDRA_KEYSPACE']
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


cs = CassandraClient()