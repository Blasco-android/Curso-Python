valor = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado...')
    else:
        print('Valor duplicado, não vou adicionar')
    option = input('Deseja continuar [S / N]: ').upper()
    if option == 'N':
        break
print('=-'*20)
print(sorted(valor))
