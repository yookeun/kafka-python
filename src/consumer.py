from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers':'kafka1:9092,kafka2:9092,kafka3L9092',
    'group.id': 'ykkim-group',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['ykkim-topic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print('Consumer error {}'.format(msg.error))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()