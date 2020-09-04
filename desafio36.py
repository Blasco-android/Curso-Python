valor_imovel = int(input('Qual o valor do imovel: '))
salario = int(input('Qual seu salario: '))
parcela = int(input('Numero de parcelas: '))

valor_parcela = valor_imovel / parcela
porcentual_salarial = salario * .03

if valor_parcela > porcentual_salarial:
    print('Empresimo Negado')
else:
    print('Emprestimo Aprovado')

