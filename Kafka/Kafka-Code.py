-- Kafka Kurulumu ve Topic oluşumu için gerekli kodlar

sudo nohup bin/zookeeper-server-start.sh config/zookeeper.properties &

sudo nohup bin/kafka-server-start.sh config/server.properties &

sudo bin/kafka-topics.sh --create --topic kafkaTopic --bootstrap-server localhost:9092


sudo bin/kafka-console-producer.sh --topic kafkaTopic --bootstrap-server localhost:9092

sudo bin/kafka-topics.sh --bootstrap-server=localhost:9092 –list

sudo bin/kafka-console-consumer.sh --topic ornek --from-beginning --bootstrap-server localhost:9092

(Optional) - sudo bin/kafka-topics.sh --bootstrap-server localhost:9092 --kafkaTopic --topic ornek