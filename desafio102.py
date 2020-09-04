'''
Exercício Python 102: Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(n, show=False):
    """
    -->Função para calculo de fatorial
    :param n: numero a ser calculado
    :param show: mostra ou não a conta
    :return: o fatorial de n.
    """
    fat = 1
    if show == False:
        for c in range(n, 0, -1):
            fat *= c
        return (fat)
    else:
        for c in  range(n, 0, -1):
            if c != 1:
                print(f'{c}! x ', end='')
            else:
                print(f'{c}! ', end='')
            fat *= c
        print(f' = {fat}')



print(fatorial(6, True))
