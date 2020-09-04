# Brasileirão 2019

tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
        'Athletico - PR', 'São Paulo', 'Internacional', 'Corinthians',
        'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
        'Atlético - MG', 'Fluminense', 'Botafogo', 'Ceará',
        'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')


print('=-'*50)
print('OPÇÕES:')
print('\033[31;1m [A] \033[m - Os 4 primeiros colocados.')
print('\033[31;1m [B] \033[m - Os 4 ultimos colocados.')
print('\033[31;1m [C] \033[m - Tabela Completa de classificação.')
print('\033[31;1m [D] \033[m - Time Campeão.')
print('\033[31;1m [E] \033[m - Saber a posição de um time qualquer.')
print('\033[31;1m [F] \033[m - Fecha o Programa.')

opcao = str(input('Digite uma Opção: ')).upper().split()[0]

while True:
    if opcao not in ('ABCDEF'):
        print('\033[32;1m OPÇÃO INVALIDA!!! \033[m')
    opcao = str(input('Digite uma Opção: ')).upper().split()[0]

    if opcao in 'A':
        print(f'Os 4 primeiros colocados são: ')
        for pos, time in enumerate(tabela[:4]):
            print(f'\033[32;1m {pos+1}º - {time} \033[m')
        print('=-' * 50)

    elif opcao in 'B':
        print(f'Os 4 Ultimos colocados são: ')
        for pos, time in enumerate(tabela[15:]):
            print(f'\033[31;1m {pos+17}º - {time} \033[m')
        print('=-' * 50)

    elif opcao in 'C':
        print(tabela)
        print('=-'*50)

    elif opcao in 'D':
        print(f' {tabela[0]} CAMPEÃO !!!')
        print('=-' * 50)

    elif opcao == 'E':
        time_pos = input('Digite um time pra saber sua posição: ').capitalize() #Tranforma a 1º letra em maiuscula
        print(f'O {time_pos} está em {tabela.index(time_pos)+1}º lugar.')

    elif opcao in 'F':
        break
print('=-'*50)
print('--* FIM *--')
