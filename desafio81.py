num = []

while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    option = input('Deseja Continuar [S/N]: ')
    if option in 'Nn':
        break
print(f'Você digitou {len(num)} números...')
num.sort(reverse=True)
print(f'Esta é sua lista em ordem decrescente: {num}')
if num.count(5):
    print(f'O valor 5 foi encontrado na lista ')
else:
    print(f'O valor 5 NÃO foi encontrado na lista ')

