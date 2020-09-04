dados = list()
pessoas = list()
idade = list()

while True:
    dados.append(input('Digite um Nome: '))
    dados.append(int(input('Digite a idade: ')))
    pessoas.append(dados[:])
    idade.append(dados[1])
    dados.clear()

    resp = input('Deseja Continuar[S/N]: ')
    if resp in 'Nn':
        break

print('=-'*40)
print(pessoas)
print(idade)
print('=-'*40)
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'O maior idade foi de {max(idade)} - Idade de ', end='')
for i in pessoas:
    if i[1] == max(idade):
        print(f'{i[0]}; ', end='')
print(f'\nA menor idade foi de {min(idade)} - Idade de ', end='')
for i in pessoas:
    if i[1] == min(idade):
        print(f'{i[0]}; ', end='')

