# Analise de Dados

c = h = m = 0
titulo = 'ESTATISTICAS'
while True:
    print('-+' * 20)
    print('CADASTRE UM PESSOA')
    print('-+' * 20)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M / F]: ')).strip().upper()[0]
    if idade >= 18:
        c += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F':
        if idade < 20:
            m += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S / N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{titulo:+^40}')
print(f'Total de pessoas com 18 anos : {c}')
print(f'Ao todo temos {h} ', end='')
print('Homem Cadastrado.' if h == 1 else 'Homens Cadastrados.')
print(f'E temos {m} ', end='')
print('mulher com menos de 20 anos' if m == 1 else 'mulheres com menos de 20 anos')
