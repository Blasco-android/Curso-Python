lista = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = input('Deseja Continuar [S/N]: ')
    if resp in 'Nn':
        break

print('=-'*30)
print(f'Lista completa: {lista}')
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Lista Pares: {par}')
print(f'Lista Impares: {impar}')
