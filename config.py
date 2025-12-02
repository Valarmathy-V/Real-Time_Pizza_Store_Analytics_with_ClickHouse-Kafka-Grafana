KAFKA_CONF = {
    'bootstrap.servers': "your redpanda server url",
    'security.protocol': "SASL_SSL",
    'sasl.mechanisms': "SCRAM-SHA-256 or 512",
    'sasl.username': "username",
    'sasl.password': "password"
}

CLICKHOUSE_CONF = {
    'host': "clickhouse cloud url",
    'port': port number,
    'user': "default",
    'password': "password",
    'database': "Db_name"
}
