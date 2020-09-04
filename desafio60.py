# Calcular o Fatorial

'''
#Utilizando modulo
from math import factorial

print('''
#[ 1 ] Calcular Fatorial
#[ 0 ] Fechar Programa
''')
abrir = int(input('Escolha uma Opcão: '))
while abrir != 0:
    num = int(input('Digite um valor: '))
    print('O fatorial de {} é {}.'.format(factorial(num)))

'''


num = int(input('Digite um numero para calcular seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
