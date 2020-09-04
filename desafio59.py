# Calculadora

num1 = int(input('Digite 1º valor: '))
num2 = int(input('Digite 2º valor: '))

opcao = 0
while opcao != 5:
    print('\n[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NUMEROS')
    print('[ 5 ] SAIR')
    opcao = int(input('Escola uma opção: '))

    while opcao not in (1, 2, 3, 4, 5): # Verifica se usuario digtou opção correta
        print('\n!!OPÇÃO INVALIDA ESCOLA NOVAMENTE')
        print('[ 1 ] SOMAR')
        print('[ 2 ] MULTIPLICAR')
        print('[ 3 ] MAIOR')
        print('[ 4 ] NOVOS NUMEROS')
        print('[ 5 ] SAIR')
        opcao = int(input('Escola uma opção: '))

    if opcao == 1:
        soma = num1 + num2
        print('\033[31mA soma dos 2 numeros é: {}\033[m'.format(soma))
    elif opcao == 2:
        multi = num1 * num2
        print('\033[31mA multiplicação dos 2 numeros é: {}\033[m'.format(multi))
    elif opcao == 3:
        if num1 > num2:
            print('\033[31mO 1º numero é o MAIOR\033[m')
        if num2 > num1:
            print('\033[31mO 2º numero é o Maior\033[m')
    elif opcao == 4:
        num1 = int(input('Digite 1º valor: '))
        num2 = int(input('Digite 2º valor: '))

print('Finish')



