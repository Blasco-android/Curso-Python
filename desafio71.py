# Simulador de caixa automatico
from math import floor

titulo = 'BANCO BLASCO'
print('$'*30)
print(f'\033[31;1m{titulo:^30}\033[m')
print('$'*30)

saque = int(input('Valor do Saque: R$ '))
total = saque
cedula = 50
totalC = 0
while True:
    if total >= cedula:
        total -= cedula
        totalC += 1
    else:
        if totalC > 0:
            print(f'Cedulas de R${cedula}: {totalC}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalC = 0
        if total == 0:
            break
print('$'*30)
print('Volte Sempre ao Banco Blasco')