pessoas = dict()
cadastro = list()
soma = list()
mulheres = list()
acima_media = list()

while True:
    pessoas['nome'] = input('Nome: ')
    pessoas['sexo'] = input('Sexo [M / F]: ').upper()
    while pessoas['sexo'] not in 'MF':
        print('ERRO!! - Responda apenas M ou F')
        pessoas['sexo'] = input('Sexo [M / F]: ').upper()
    pessoas['idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    soma.append(pessoas['idade'])
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    if pessoas['idade'] > sum(soma)/len(cadastro):
        acima_media.append(pessoas.copy())

    resp = input('Deseja continuar [S / N]: ').upper()
    while resp not in 'SN':
        print('ERRO!! - Responda apenas S ou N.')
        resp = input('Deseja continuar [S / N]: ').upper()
    if resp == 'N':
        break

print('=-'*50)
print(f'A) Ao todo foram {len(cadastro)} pessoas cadastradas.')
print(f'B) A media de idade é {sum(soma)/len(cadastro)}')

print(f'C) As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'{m}', end=', ')
print()
print(f'D) Lista das pessoas que estão acima da media: ')
for m in acima_media:
    print('  ', end='')
    for k, v in m.items():
        print(f'{k} = {v}; ', end='')
    print()
print('<<ENCERRADO>>')
