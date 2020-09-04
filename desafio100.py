'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.
'''

from time import sleep
from random import sample



def sorteia(lista):
    n = sample(range(0, 10), 5)
    lista.append(n[:])
    print(f'Sorteando 5 Valores da lista: {lista} - Pronto.')

def somaPar(lista):
    for n in lista[0]:
        if n % 2 == 0:
            soma.append(n)
    print(f'Somando os valores pares de {lista}, temos: {sum(soma)}.')


num = list()
soma = list()
sorteia(num)
somaPar(num)


