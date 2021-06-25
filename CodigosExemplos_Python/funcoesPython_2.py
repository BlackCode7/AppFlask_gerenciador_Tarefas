# Passagem de parametros
def valildar(valido, valido2=True):
    if valido and valido2:
        return 'Valores True'
    else:
        return 'Valores Falso'


if __name__ == "__main__":
    teste = False
    teste2 = True
    respostaDaFuncao = valildar(teste, teste2)

    print(respostaDaFuncao)