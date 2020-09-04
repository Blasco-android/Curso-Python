# Numero por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um numero de 0 a 20: '))

while n > 20:
    print('Numero invalido!!')
    n = int(input('Digite um numero de 0 a 20: '))
print(f'*-Você digitou \033[31;1m{extenso[n]}\033[m-*')

resp = input('Quer continuar [S / N]: ').strip().upper()[0]
while resp not in 'N':
    n = int(input('Digite um numero de 0 a 20: '))
    print(f'*-Você digitou \033[31;1m{extenso[n]}\033[m-*')
    resp = input('Quer continuar [S / N]: ').strip().upper()[0]
print('FIM')
