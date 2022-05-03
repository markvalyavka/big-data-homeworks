"""Module for app configs."""


def configure_app_dev(app):

    app.config["CASSANDRA_HOST"] = "cassandra_node1"
    app.config["CASSANDRA_PORT"] = 9042
    app.config["CASSANDRA_KEYSPACE"] = "hw4_valyavka"
