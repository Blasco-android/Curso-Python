soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1  # contador
        soma += c  # acomulador

print('A soma de todos os {} multiplos de 3 de 1 a 500 é: \033[1;31m {} \033[m'.format(cont, soma))