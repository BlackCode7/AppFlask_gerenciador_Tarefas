def adicao(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    return n1 / n2


if __name__ == '__main__':
    print('Para efetuar corretamente as operações digite um dos símbolos: +, -, *, /')
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))

    operador = input('Digite o operador do cálculo: ')

    result = None

    if operador == '+':
        result = adicao(n1, n2)
        print('O reltado da soma foi {}'.format(result))

    elif operador == '-':
        result = subtracao(n1, n2)
        print('O reltado da subtração foi {}'.format(result))

    elif operador == '*':
        result = multiplicacao(n1, n2)
        print('O reltado da Multiplicação foi {}'.format(result))

    elif operador == '/':
        result = divisao(n1, n2)
        print('O reltado da Divisão foi {}'.format(result))

    else:
        print("Operador incorreto")