matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = []
soma1 = []

for l in range(0, 3): # Adicionando valores na matriz 3x3
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 30)

for l in range(0, 3): # print formato em tabela de matriz
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()

for l1 in range(0, 3): # Separando da matriz os pares e add na lista soma
    for c1 in range(0, 3):
        if matriz[l1][c1] % 2 == 0:
            soma.append(matriz[l1][c1])
print('=-' * 30)
print(f'Soma de pares da matriz: {sum(soma)}')
print(f'O maior valor da 2º linha é: {max(matriz[1])}')

for l2 in range(0, 3):
    soma1.append(matriz[l2][2])
print(f'A soma da 3ª coluna é: {sum(soma1)}')


