boletim = list()
alunos = list()
notas = list()
media = 0

while True:
    alunos.append(input('NOME: '))
    notas.append(float(input('NOTA 1: ')))
    notas.append(float(input('NOTA 2: ')))
    alunos.append(notas[:])
    media = (sum(notas)/2)
    alunos.append(media)
    boletim.append(alunos[:])
    alunos.clear()
    notas.clear()


    ask = input('Deseja continuar [S/N]: ')
    if ask in 'Nn':
        break

print(f'{"ID":<4}', f'{"NOME":<14}', f'{"MEDIA"}')
print('-'*35)
for i, aluno in enumerate(boletim):
    print(f'{i:<4}', f'{aluno[0]:<14}', f'{aluno[2]:.2f}')
print('-'*35)

while True:
    print('Para ver a nota do aluno')
    opcao = int(input('Digite a ID do Aluno(33 fecha) : '))
    for i, aluno in enumerate(boletim):
        if opcao == i:
            print(f'Notas de {aluno[0]} são: {aluno[1]}')
    if opcao == 33:
        break
    print('-' * 35)
print('FECHANDO PROGRAMA')
