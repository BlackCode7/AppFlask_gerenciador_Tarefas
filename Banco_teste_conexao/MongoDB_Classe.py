from pymongo import MongoClient


class BancoMongo:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return self.nome

