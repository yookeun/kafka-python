from confluent_kafka import Consumer, KafkaError


print("---consumer start!---")

c = Consumer({
    'bootstrap.servers':'192.168.27.3:9092,192.168.99.102:9092,192.168.2.3:9092',
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
print("---consumer end!---")