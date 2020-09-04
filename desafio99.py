'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que
analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep

def linha():
    print('=-' * 30)


def maior(* num):
    print('Analisando os valores passados...')
    sleep(.5)
    print(f' - {num} - Foram informados {len(num)} valores ao todo.')
    sleep(.5)
    maior = cont = 0
    for n in num:
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n

    print(f'O maior número informado foi {maior}.')



linha()
maior(1, 5, 8, 9, 11)
linha()
maior(4, 1, 10)
linha()
maior(10, 13, 11, 23, 45)
linha()
