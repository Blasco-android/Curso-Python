'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaInt(msg=''):
    num = input(msg)
    while True:
        if not num or not num.isnumeric():
            print('\033[32;1m ERRO!! - Digite um numero inteiro.\033[m')
            num = input(msg)
        else:
            break
    return num

n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}.')
