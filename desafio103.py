'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols
ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(nome='desconhecido', gol=0):
    if nome == '':
        nome = '<desconhecido>'
    if not gol or not gol.isnumeric():
        gol = 0
    print(f'O jogador {nome}, fez {gol} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gol = input('Numeros de gols: ')
ficha(nome, gol)
