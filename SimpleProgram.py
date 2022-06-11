from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('HW9_SparkProj').getOrCreate()

tx_df = spark.read.csv("PS_20174392719_1491204439457_log.csv")
tx_df.printSchema()

print(f'DF_SPARK_ROWS -> {tx_df.count()}')
