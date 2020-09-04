num = int(input('Enter a number [999 STOP]: '))
cont = 0
soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Enter a number [999 STOP]: '))
print('You entered {} and this sum is {}'.format(cont, soma))
