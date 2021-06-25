if __name__ == '__main__':
    print('Para efetuar corretamente as operações digite um dos símbolos: +, -, *, /')
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))

    operador = input('Digite o operador do cálculo: ')

    if operador == '+':
        result = n1 + n2
        print('O reltado da soma foi {}'.format(result))

    if operador == '-':
        result = n1 - n2
        print('O reltado da subtração foi {}'.format(result))

    if operador == '*':
        result = n1 * n2
        print('O reltado da Multiplicação foi {}'.format(result))

    if operador == '/':
        result = n1 / n2
        print('O reltado da Divisão foi {}'.format(result))
