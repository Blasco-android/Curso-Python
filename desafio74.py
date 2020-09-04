# mostrar maior e menor valor de 5 numeros aleatorios enviados para um tupla

from random import randint, sample
titulo1 = 'SORTEIO MEGA SENA'
titulo2 = 'SORTEIO LOTOFACIL'

#sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
sorteio1 = tuple(sample(range(61), 6))
sorteio2 = tuple(sample(range(1, 26), 15))
palpite1 = str(sorted(sorteio1)) # int > str
palpite2 = str(sorted(sorteio2)) # int > str


print('\033[36;1m$'*70)
print(f'${titulo1:^68}$')
print(f'${palpite1:^68}$')
print('$'*70)
print(f'${titulo2:^68}$')
print(f'${palpite2:^68}$')
print('$'*70)


'''
print(f'MAIOR: {max(sorteio1)}')
print(f'MENOR: {min(sorteio1)}')
'''
