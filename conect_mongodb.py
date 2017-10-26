# -*- coding: utf-8 -*-
from pymongo import MongoClient
import datetime
import pprint

# Conexão com o MongoClient.
client = MongoClient('localhost', 27017)

# Obtendo um banco de dados.
#db = client['test-database']
db = client.test_database

# Obtendo uma coleção.
#collection = db['test-collection']
posts = db.test_collection
#print(collection)

# --- Inserte um documento.
post = {"author": "Neviim",
        "text": "Este é um poste teste!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id
print(post_id)

# Obtendo um único documento com find_one().
print(pprint.pprint(posts.find_one()))
