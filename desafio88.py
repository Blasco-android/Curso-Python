from random import sample
from time import sleep

while True:
    print('1 - MEGA SENA')
    print('2 - LOTOFACIL')
    print('0 - FECHAR')
    option = int(input('Escolha uma opção: '))

    while option not in (0, 1, 2):
        print('\033[33;1mDIGITE UM VALOR VALIDO!!\033[m')
        print('1 - MEGA SENA')
        print('2 - LOTOFACIL')
        print('0 - FECHAR')
        option = int(input('Escolha uma opção: '))

    if option == 0:
        break

    if option == 1:
        print('$'*36)
        print(f'{"SORTEIO MEGA SENA":^36}')
        print('$'*36)
        palpites = int(input('\nQuantos jogos deseja: '))
        print(f'\n-=-=-=-= SORTEANDO {palpites} JOGOS =-=-=-=-\n')
        for c in range(1, palpites+1):
            jogos = list(sample(range(1, 61), 6))
            print(f'JOGO {c}: {sorted(jogos)}')
            sleep(1)
        print(f'\n{"-=-=-=-=-=< BOA SORTE ! >=-=-=-=-=-":^36}')

    if option == 2:
        print('$'*36)
        print(f'{"SORTEIO LOTOFACIL":^36}')
        print('$'*36)
        palpites = int(input('\nQuantos jogos deseja: '))
        print(f'\n-=-=-=-= SORTEANDO {palpites} JOGOS =-=-=-=-\n')
        for c in range(1, palpites+1):
            jogos = list(sample(range(1, 26), 15))
            print(f'JOGO {c}: {sorted(jogos)}')
            sleep(1)
        print(f'\n{"-=-=-=-=-=< BOA SORTE ! >=-=-=-=-=-":^36}')

print(f'\n{"-=-=-=-=-=< ENCERRANDO ! >=-=-=-=-=-":^36}')
