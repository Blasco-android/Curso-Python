num = int(input('Digite um valor: '))

print('Digite 1 para converte em binario')
print('Digite 2 para converte em octal')
print('Digite 3 para converte em hexadecimal')
print('Digite 0 para sair')
codigo = int(input('Digite a opcao desejada: '))

while codigo not in (0, 1, 2, 3):
    print('\nOpcao errada digite um valor valido!!\n')
    print('Digite 1 para converte em binario')
    print('Digite 2 para converte em octal')
    print('Digite 3 para converte em hexadecimal')
    print('Digite 0 para sair')
    codigo = int(input('Digite a opcao desejada: '))

while codigo != 0:
    if codigo == 1:
        print('O bonario de {} é : {}\n'.format(num, bin(num))) #converte inteiro em binario
    elif codigo == 2:
        print('O octal de {} é : {}\n'.format(num, oct(num))) #converte inteiro em octal
    elif codigo == 3:
        print('O haxadecimal de {} é : {}\n'.format(num, hex(num)))

    print('Digite 1 para converte em binario')
    print('Digite 2 para converte em octal')
    print('Digite 3 para converte em hexadecimal')
    print('Digite 0 para sair')
    codigo = int(input('Digite a opcao desejada: '))