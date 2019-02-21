from confluent_kafka import Producer


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed : {}'.format(err))
    else:
        print('Message delivery to {} [{}]'.format(msg.topic, msg.partition))


p = Producer({'bootstrap.servers': 'kafka1:9092,kafka2:9092,kafka3:9092'})
p.poll(0)
msg = 'Hello Python'
p.produce('ykkim-topic', msg.encode('utf-8'), callback=delivery_report)
p.flush()
