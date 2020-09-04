soma = 0

for c in range(1, 7):
    num = int(input('Digite um valor 1/{}'.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros pares digitados é: {}'.format(soma))
