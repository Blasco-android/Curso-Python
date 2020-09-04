num1 = int(input('Digite o primeiro numero: \n'))
num2 = int(input('Digite o segundo numero: \n'))

if num1 > num2:
    print('O primeiro é o maior')
elif num2 > num1:
    print('O primeiro é o maior'.format(num2))
else:
    print('ambos são iguais')