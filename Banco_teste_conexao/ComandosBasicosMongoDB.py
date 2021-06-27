# Instalando conector com banco mongodb Lib PyMongo
from pip._internal.commands import show
from pymongo import MongoClient

# Criando a conexao com o banco
client = MongoClient("localhost", 27017)

# Exibindo as bases de dados cadastrados no mongodb
print(client.list_database_names())

# criando uma base de dados no mongoDB
db = client.Usuario_teste_2

#Inserindo muitos valores no mongodb
db.tb_usuario_teste_2.insert_many(
   [
       {
        "nome": "Carlos",
        "sobrenome": "Mendonça",
        "idade": 32
        }
   ]
)

# Inserindo apenas um unico valor na tabela
db.tb_usuario_teste_2.insert_one({
    "nome": "Gisele"
})

# listando os registros do banco no mongoDB
item_1 = db.tb_usuario_teste_2.find()
print('retornando o primerio item do banco >>> ', item_1[0])
#print('Mostra um registro especifico >>> ', db.tb_usuario_teste_2.findOne({nome:/ma/i}))
#print(show.collections)
print(db.tb_usuario_teste_2.find())

print('Trazendo 2 elementos >>> ', db.tb_usuario_teste_2.find().limit(2))

print('Trazendo 2 elementos >>> ', db.tb_usuario_teste_2.find().limit(2))

print('Atualizando elementos >>> ', db.tb_usuario_teste_2.find_one({"roll_no": item_1[1]}))