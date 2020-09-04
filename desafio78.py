valor = list()

for count in range (0, 5):
    valor.append(int(input(f'Digite um valor na posição {count}: ')))
print('=-'*30)
print(valor)

print(f'Maior: {max(valor)} -> Posição: ', end='')
for i, v in enumerate(valor):
    if v == max(valor):
        print(f'{i}...', end='')
print()

print(f'Menor: {min(valor)} -> Posição: ', end='')
for i, v in enumerate(valor):
    if v == min(valor):
        print(f'{i}...', end='')
print()
