
fim = ''
while fim == 'N':
    sexo = str(input('Digite o sexo [ M / F ]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção invalida digite novamente')
        sexo = str(input('Digite o sexo [ M / F ]: ')).upper()
    fim = str(input('Deseja continuar [ S / N ]: ')).upper()
