# Teste de Python 
# Autor: Darlan Carrião

O teste consiste no seguinte:

Neste desafio você precisa calcular o número médio de estrelas de cada restaurante.

Você irá trabalhar com um conjunto de dados presente no Yelp Dataset, o arquivo yelp_academic_dataset_review.json (https://www.kaggle.com/yelp-dataset/yelp-dataset?select=yelp_academic_dataset_review.json)

Construa um script (de preferência em Python ou em Go) que leia o arquivo JSON acima e publique o resultado para outro script processar os dados.

Para processamento dos dados, construa um script que calcule o número médio de stars para cada business_ide salve o resultado em um banco de dados SQL.
Os campos starts e business_id estão presentes no arquivo yelp_academic_dataset_review.json.

Sugestões: 
Utilize um sistema de mensageria entre o script de publicação dos dados com o script que irá consumir os dados.
Tente realizar o cálculo em tempo real.
 
#########  Para executar o teste:

Requisitos para execução dos arquivos:

1. Ter o Python instalado na máquina, de preferência versão 3.7, segue abaixo o link para a instalação do Python:
   https://realpython.com/installing-python/

2. Instalar o Kafka na máquina, segue abaixo o guia para instalar o kafka:
   https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm

3. Instalar o pacote kafka-python:
   https://kafka-python.readthedocs.io/en/master/install.html

4. Fazer download do arquivo yelp_academic_dataset_review.json em:
   https://www.kaggle.com/yelp-dataset/yelp-dataset?select=yelp_academic_dataset_review.json

5. Alterar no arquivo producer.py, a variável filename para o caminho onde foi efetuado o download do arquivo .json

6. Executar o arquivo consumer.py:
   python3 consumer.py
   
7. Executar o arquivo producer.py:
   python3 producer.py
   
   Bem, eu escolhi python e Kafka porque ambos são mais rápidos e escaláveis que outras tecnologias, principalmente por ser um arquivo com mais de 6GB de tamanho e outra linguagem poderia travar na leitura.
   A solução tomada foi um kafka instalado na minha própria máquina, entretanto se utilizar o Azure ou AWS poderia enviar várias mensagens simultâneas para consumir acredito que um processo no AWS lambda iria resolver de forma bem rápida isto.
   
   Grato pela oportunidade.
