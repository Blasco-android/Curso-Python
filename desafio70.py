# Estatísticas em produtos

titulo = 'BLASCO ELETRO'
rodape = 'FIM DE PROGRAMA'
print('|'*40)
print(f'||{titulo:^36}||')
print('|'*40)

totalValor = valormil = cont = barato = 0
pdtbarato = ''
while True:
    produto = str(input('Nome do Produto: '))
    valor = int(input('Valor do Produto R$: '))
    cont += 1
    totalValor += valor
    if valor > 1000:
        valormil += 1

    # Recebe o menor valor e o produto do mesmo.
    if cont == 1 or valor < barato:
        barato = valor
        pdtbarato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Adicionar mais produto [ S / N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('|'*40)
print(f'||{rodape:^36}||')
print(f'Total da compra: \033[32mR${totalValor:.2f}\033[m')
print(f'\033[32m{valormil}\033[m Produto custando mais de R$1000.00')
print(f'O produto mais barato: \033[32m{pdtbarato}\033[m Valo: \033[32mR${barato}\033[m')