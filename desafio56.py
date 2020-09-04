import os

soma = 0
cont = 0
maior = -999


for people in range(1, 5):
    print('******{}º PESSOA******'.format(people))
    name = str(input('Type the name: '))
    age = int(input('Type the age: '))
    sexo = str(input('Type the sexo[ M ] / [ F ]: ')).upper()

    # soma e media da idade
    soma += age
    media = soma / people
    #Verifica entre os homens do grupo qual é mais velho.
    if age > maior and sexo in 'Mm':
        maior = age
        name_man = name
    #verifica quantas mulheres tem menos de 20 anos.
    if sexo in 'Ff' and age < 20:
        cont += 1

print('\nA soma da idade do grupo é {}, e asua media é {}.'.format(soma, media))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maior, name_man))
print('Temos {} mulheres menores de 20 anos'.format(cont))

