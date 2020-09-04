# JOGO - adinvinhe em que numero pensei

from random import randint

num = randint(1, 11)
palpite = 0
cont = 0

while palpite != num:
    palpite = int(input('Em qual numero estou pensando: '))
    cont += 1
    if palpite < num:
        print('È mais')
    elif palpite > num:
        print('É menos!')

print('Acertou pensei no {}, vc usou {} tentivas.'.format(num, cont))
