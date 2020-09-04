from datetime import date

ano_nasc = int(input('Digite o ano de nascimento: '))

idade = date.today().year - ano_nasc

if idade == 18:
    print('Deve se alistar este ano')
elif idade < 18:
    tempo = 18 - idade
    print('faltam {} anos para se alistar'.format(tempo))
elif idade > 18:
    tempo1 = idade - 18
    print('deviria ter ser alistado a {} anos atras'.format(tempo1))
