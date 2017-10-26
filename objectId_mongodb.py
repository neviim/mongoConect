# -*- coding: utf-8 -*-
from pymongo import MongoClient
import datetime
import pprint

# Conexão com o MongoClient.
client = MongoClient('localhost', 27017)
# Obtendo um banco de dados.
db = client.gran_turismo_sport
# Obtendo uma coleção.
posts = db.carros

# Usando um dicionários para representar um documento.
post = {"author": "Audi",
        "text": "R8 Turbo V12!",
        "tags": ["carro", "corrida", "gts"],
        "date": datetime.datetime.utcnow()}

# Para inserir um documento: (post), em uma coleção: (posts [db.carros]).
post_id = posts.insert_one(post).inserted_id
print(post_id)
print("...")

# Mostra se a coleção de postagens realmente foi criada no servidor.
#print(db.collection_names(include_system_collections=False))

# Retorno a coleção com o ultimo post_id gerado no posts.insert_one(post).inserted_id
pprint.pprint(posts.find_one({"_id": post_id}))
print("...")

# Observe que um ObjectId não é o mesmo que a sua representação
# de seqüência de caracteres:
post_id_as_str = str(post_id)
print(post_id_as_str)
print(posts.find_one({"_id": post_id_as_str})) # retorna None
print("...")

# Uma tarefa comum nas aplicações web é obter um ObjectId a partir do URL da
# solicitação e encontrar o documento correspondente. É necessário neste caso
# converter o ObjectId de uma string antes de passar para find_one:

# Por exemplo a estrutura da web obtém o post_id do URL e o passa como uma string
# def get(post_id):
#    # Converte de string para ObjectId:
#    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
from bson.objectid import ObjectId
print(posts.find_one({'_id': ObjectId(post_id_as_str)}))
