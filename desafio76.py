tabela = ('NoteBook', 1800.00, 'Cadeira', 600.00, 'Mesa', 450.00, 'Celular', 1950.00)

print('_' * 40)
print('{:^40}'.format('TABELA DE PREÇO'))
print('_' * 40)
for c in range(0, len(tabela), 2):
    print(f'{tabela[c]:.<30}', f'R${tabela[c+1]:>7.2f}')
print('_' * 40)
