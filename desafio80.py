num = list()

for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado no final da lista')

    else:
        i = 0
        while i < len(num):
            if n <= num[i]:
                num.insert(i, n)
                print(f'Adicionado na posição {i}')
                break
            i += 1

print(f'Lista: {num}')
