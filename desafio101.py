'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return (f' - Com {idade} anos: NÃO VOTA.')
    if 18 > idade >= 16 or idade >= 65:
        return (f' - Com {idade} anos: VOTO OPCIONAL.')
    if 65 > idade > 18:
        return (f' - Com {idade} anos: VOTO OBRIGATORIO.')


reposta = voto(int(input('Digite o ano de nascimento: ')))
print(reposta)
