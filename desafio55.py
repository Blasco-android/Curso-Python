maior = -999
menor = 999

for c in range(1, 6):
    peso = int(input('Digite o peso da {}º pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('{} Kg é o maior peso!!'.format(maior))
print('{} Kg é o menor peso!!'.format(menor))