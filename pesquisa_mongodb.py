# -*- coding: utf-8 -*-
from pymongo import MongoClient
import datetime
import pprint

# Conexão com o MongoClient.
client = MongoClient('localhost', 27017)
# Obtendo um banco de dados.
db = client.test_database
# Obtendo uma coleção.
posts = db.test_collection

# pesquisa por autor.
resultado = pprint.pprint(posts.find_one({"author": "Neviim"}))
print("...")

# lista todos
for post in posts.find({"author": "Neviim"}):
    pprint.pprint(post)
print("...")

# contando registros.
print("Total Coleção:", posts.count())
print("Autor, Neviim:", posts.find({"author": "Neviim"}).count())
print("...")

# "$lt", operador para fazer uma consulta de intervalo e também, ordenar os resultados por autor.
# seleciona os documentos onde o valor do campo especificado seja menor que o valor especificado.
# o campo data esta no formato: [Ano,Mes,Dia,Hora,Minuto]
d = datetime.datetime(2017, 10, 25, 10, 50)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)
print("...")

# 
