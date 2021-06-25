def valildar(valido, valido2):
    if valido == True and valido2 == True:
        return 'Valores True'
    else:
        return 'Valores Falso'


if __name__=="__main__":
    teste = False
    teste2 = True
    respostaDaFuncao = valildar(teste, teste2)

    print(respostaDaFuncao)