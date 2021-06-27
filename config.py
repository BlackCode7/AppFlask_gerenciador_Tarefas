import random
import string

API_PORT = 5000
API_HOST = '127.0.0.1'
API_BASE_URL = '/api'
DEBUG = True

LOGIN_TESTE = ''
SENHA_TESTE = 'Admin123@'

# Criando um gerador de senhas aleatórias
gen = string.ascii_letters+string.digits+string.ascii_uppercase
SECRET_KEY = ''.join(random.choice(gen) for i in range(32))


# Configuração do mysql
MYSQL_PORT = '3306'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'xG4uChuzkF2XWaCt'
# Nome do banco de dados
MYSQL_DATABASE = 'Nome do banco de dados'