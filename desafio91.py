from random import randint
from time import sleep
from operator import itemgetter # função para definir o que sera ordenador dentro do dicionario

jogo = {'jogador-01': randint(1,6),
        'jogador-02': randint(1, 6),
        'jogador-03': randint(1, 6),
        'jogador-04': randint(1, 6)}
ranking = list()

print('=-'*30)
print('Lançando os Dados...')
for k, v in jogo.items():
    print(f'- {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print('=-'*30)
print('==RANKING==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')


# Resolução01
'''
jogo_dados = []
jogador = {}

for c in range(0, 4):
    jogador['jogador'] = c+1
    jogador['tirou'] = randint(1, 6)
    jogo_dados.append(jogador.copy())

print('=-'*30)
print('Valores Sorteados: ')
for e in jogo_dados:
    for k, v in e.items():
        print(f'{k} {v}', end=' ')
    print('no dado')
    sleep(1)
'''
