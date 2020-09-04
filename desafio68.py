# Jogar par ou impar

from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*30)
v = 0
while True:
    n1 = int(input('Escolha um numero 1 a 10: '))
    pc = randint(0, 10)
    total = n1 + pc
    tipo = ' ' # dar um espaço se não pularar a linha 15

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [ P / I ]: ')).strip().upper()[0]
    print(f'Você jogou {n1} e o Coputador jogou {pc}. Total = {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu \o/')
            v += 1
        else:
            print('Você Perdeu :(')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu \o/')
            v += 1
        else:
            print('Você Perdeu :(')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER - Você venceu {v} vezes')



