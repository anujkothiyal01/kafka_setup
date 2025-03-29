from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'realtime_data'

while True:
    data = {
        "timestamp": time.time(),
        "stock_price": round(random.uniform(100, 500), 2)
    }
    producer.send(topic, value=data)
    print(f"Sent: {data}")
    time.sleep(2)  # Send data every 2 seconds
