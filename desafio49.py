valor = int(input('Digite o numero da tabuada que deseja saber: '))
print('\033[1;36;mTABUADA DO {}\033[m\n'.format(valor))

for c in range(1, 11):
    resultado = valor * c
    print('{} X {:2} = {}'.format(valor, c, resultado))
print('fim')
