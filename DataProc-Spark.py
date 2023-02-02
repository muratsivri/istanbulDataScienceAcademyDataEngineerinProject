Scala

spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar

import spark.implicits._

import org.apache.spark.sql.types._

import org.apache.spark.sql.functions

import java.sql.Timestamp

import org.apache.spark.sql.streaming.Trigger.ProcessingTime

val bucket = "dataengineeringproject"

spark.conf.set("temporaryGcsBucket", bucket)

spark.conf.set("parentProject", "dataengineerexample")

val kafkaDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers","34.173.76.50:9092").option("subscribe","kafkaTopic").load

val schema = StructType(List(StructField("eth_from",StringType),StructField("eth_to",StringType),StructField("eth_value", FloatType),StructField("eth_tms",StringType),StructField("eth_hash", StringType),StructField("eth_paymount_amount", StringType)))

val activationDF = kafkaDF.select(from_json($"value".cast("string"),schema).alias("activation"))

val df = activationDF.select($"activation"("eth_from").alias("eth_from"),

$"activation"("eth_to").alias("eth_to"),

$"activation"("eth_value").alias("eth_value"),

$"activation"("eth_tms").alias("eth_tms"),

$"activation"("eth_hash").alias("eth_hash"),

$"activation"("eth_paymount_amount").alias("eth_paymount_amount"))

val modelCountDF = df.filter($"activation"("eth_value")<")

val modelCountQuery = modelCountDF.writeStream.outputMode("append").format("bigquery").option("table","dataEngineeringProjectDataset.dataEngineeringProjectTable").option("checkpointLocation", "/path/to/checkpoint/dir/in/hdfs").option("credentialsFile","/home/cloudusemurat1/dataengineerexample-68a603830680.json").option("failOnDataLoss",false).option("truncate",false).start().awaitTermination()