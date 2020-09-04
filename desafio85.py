lista = [[], []]

for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('#' * 30)
print(f'Lista: {lista}')
print(f'Pares: {sorted(lista[0])}')
print(f'Impares: {sorted(lista[1])}')
