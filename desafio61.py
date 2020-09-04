primeiro = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += ra
    cont += 1