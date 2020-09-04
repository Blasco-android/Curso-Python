num = (
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: '))
)

print(f'TUPLA = {num}')
print(f'O número 9 apreceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na {num.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado')
print('Números Pares: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
