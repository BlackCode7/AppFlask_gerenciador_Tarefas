from itertools import count

from pymongo import MongoClient

# Conectando
client = MongoClient("localhost", 27017)
# Exibir bases no banco
print(client.list_database_names())
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# criando uma basade dados
db = client.BancoMongo_1
db.tb_BancoMongo.insert_many(
    [
        {
            "Nome_Banco": "MongoDB",
            "Tipo_Banco": "Nao_Relacional",
            "Vantagem_Banco": "Bom"
        },
{
            "Nome_Banco": "MySQL",
            "Tipo_Banco": "Relacional",
            "Vantagem_Banco": "Bom"
        },
{
            "Nome_Banco": "PostgreSQL",
            "Tipo_Banco": "Relacional",
            "Vantagem_Banco": "Bom"
        },
{
            "Nome_Banco": "Abdc",
            "Tipo_Banco": "Nao_Relacional",
            "Vantagem_Banco": "Ruim"
        },
{
            "Nome_Banco": "Relat",
            "Tipo_Banco": "Nao_Relacional",
            "Vantagem_Banco": "Ruim"
        }
    ]
)

table = db.tb_BancoMongo
asa = table.update_many(
    {"banda": "Iron Maden"}, {"$set": {"nome": "BandaNova"}}
)

print(asa["tb_BancoMongo"])