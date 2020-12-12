from kafka import KafkaProducer
import json
import ijson
import pandas as pd

colunas = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date']
eventos = ['string', 'number']

def read_big_file():
    filename = '/projetos/intelligence/yelp_academic_dataset_review.json'
    data = ijson.parse(open(filename, 'r'), multiple_values=True)
    dados = []
    linha = []
    grava = 0
    soma = 0
    for prefix, event, value in data:
        if event in eventos:
            if prefix in colunas:
                linha.append(value)
        else:
            if event == 'end_map':
                grava = 1

        if grava == 1:
            dados.append(linha)
            grava = 0
            linha = []


    my_df = pd.DataFrame(dados, columns=colunas)
    fjson = my_df.to_json()

    return fjson

producer = KafkaProducer(bootstrap_servers=
                         ['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Send data in JSON format
producer.send('JSONtopic', read_big_file())
