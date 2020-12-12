from kafka import KafkaConsumer
import sys
import json
import pandas as pd

consumer = KafkaConsumer ('JSONtopic',bootstrap_servers = ['localhost:9092'],
value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    df = pd.read_json(message[6])
    print(df.head())
    df2 = df.groupby('business_id', as_index=False)['stars'].mean()
    print(df2)
sys.exit()