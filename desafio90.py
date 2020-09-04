aluno = {}

aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno['media'] < 5:
    aluno['status'] = 'REPROVADO'

elif aluno['media'] in (5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75):
    aluno['status'] = 'RECUPERAÇÂO'

elif aluno['media'] >= 7:
    aluno['status'] = 'APROVADO'

print('=-'*20)
print(f'Aluno: {aluno["nome"]}')
print(f'Media: {aluno["media"]}')
print(f'Situação: {aluno["status"]}')
print('=-'*20)
