# Instalando conector com banco mongodb Lib PyMongo
from pymongo import MongoClient

# Criando a conexao com o banco
client = MongoClient("localhost", 27017)

# Exibindo as bases de dados cadastrados no mongodb
print(client.list_database_names())

# criando uma base de dados no mongoDB
db = client.Usuario

#Inserindo muitos valores no mongodb
db.tb_usuario.insert_many(
   [
       {
        "nome": "Carlos",
        "sobrenome": "Mendonça",
        "idade": 32
        }
   ]
)

# Inserindo apenas um unico valor na tabela
db.tb_usuario.insert_one({
    "nome": "Gisele"
})