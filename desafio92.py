from datetime import date
trabalador = dict()


for c in range(1):
    trabalador['nome'] = input('Nome: ')
    nascimento = int(input('Ano de Nascimento: '))
    trabalador['idade'] = date.today().year - nascimento
    trabalador['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))
    if trabalador['ctps'] == 0:
        break
    else:
        trabalador['contrato'] = int(input('Ano de Contratação: '))
        trabalador['salario'] = float(input('Salário: R$'))
        trabalador['aposenta'] = (trabalador['contrato'] - nascimento) + 35

print('=-'*30)
for k, v in trabalador.items():
    print(f' {k}: {v}')
