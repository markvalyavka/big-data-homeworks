
// Create keyspace
CREATE KEYSPACE hw8_valyavka WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };


// used for query 1
CREATE TABLE IF NOT EXISTS hw8_valyavka.user_by_is_fraud
(
    step bigint,
    type text,
    amount float,
    nameOrig text,
    oldbalanceOrg float,
    newbalanceOrig float,
    nameDest text,
    oldbalanceDest float,
    newbalanceDest float,
    isFraud int,
    transactionDate date,
    PRIMARY KEY ((nameOrig), isFraud)
);

// used for query 2
CREATE TABLE IF NOT EXISTS hw8_valyavka.user_by_amount
(
    step bigint,
    type text,
    amount float,
    nameOrig text,
    oldbalanceOrg float,
    newbalanceOrig float,
    nameDest text,
    oldbalanceDest float,
    newbalanceDest float,
    isFraud int,
    transactionDate date,
    PRIMARY KEY ((nameOrig), amount))
WITH CLUSTERING ORDER BY (amount DESC);


// used for query 3
CREATE TABLE IF NOT EXISTS hw8_valyavka.user_transactions_by_date
(
    step bigint,
    type text,
    amount float,
    nameOrig text,
    oldbalanceOrg float,
    newbalanceOrig float,
    nameDest text,
    oldbalanceDest float,
    newbalanceDest float,
    isFraud int,
    transactionDate date,
    PRIMARY KEY ((nameDest), transactionDate))
WITH CLUSTERING ORDER BY (transactionDate DESC);
