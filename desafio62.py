print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro Termo: '))
ra = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += ra
        cont += 1
    print('PAUSE')
    mais = int(input("Quantos termos deseja mostrar a mais: "))



