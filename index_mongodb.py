# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pymongo
import datetime
import pprint

# Conexão com o MongoClient.
client = MongoClient('localhost', 27017)
# Obtendo um banco de dados.
db = client.test_database

# A adição de índices pode ajudar a acelerar certas consultas e também pode
# adicionar funcionalidades adicionais para consultar e armazenar documentos.

# Primeiro, precisa criar collection: profiles e o índice:
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
id_inf = sorted(list(db.profiles.index_information()))

# Observe que temos dois índices agora: um é o índice no _id que o MongoDB cria
# automaticamente e o outro é o índice no user_id que acabamos de criar.
print(id_inf)
print("...")

# Configurar alguns perfis de usuários:
''' (caso for a primeira vez descomente)
user_profiles = [{'user_id': 211, 'name': 'Neviim'},
                 {'user_id': 212, 'name': 'Jads'}]
result = db.profiles.insert_many(user_profiles)
print(result)
'''

# O índice nos impede de inserir um documento cujo user_id já está na coleção:
novo_profile      = {'user_id': 213, 'name': 'Orion'}
duplicado_profile = {'user_id': 212, 'name': 'Estrelas'}

# Este estara sendo gravado.
result = db.profiles.insert_one(novo_profile)

# Este dara erro, por estar gravado este user_id (212)
result = db.profiles.insert_one(duplicado_profile)
# pymongo.errors.DuplicateKeyError: E11000 duplicate key error collection:
# test_database.profiles index: user_id_1 dup key: { : 212 }
