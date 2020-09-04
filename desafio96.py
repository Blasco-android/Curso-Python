def area(a, b):
    """
    -> Calcula a area de um retangulo ou quadrado
    :param a: comprimento
    :param b: largura
    :return: sem retorno
    """
    x = a * b
    print(f' A area de um terreno {a} X {b} é : {x}')


def titulo():
    print('-'*20)
    print(f'{"Controle de Terreno":^20}')
    print('-'*20)


titulo()
a = float(input('Largura(m): '))
b = float(input('Comprometo(m): '))
area(a, b)

help(area)
