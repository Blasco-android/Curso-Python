from datetime import date

ano_atual = date.today().year
contmenor = 0
contmaior = 0


for c in range(1, 7):
    ano_nasc = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    if ano_atual - ano_nasc >= 18:
        contmaior += 1
    elif ano_atual - ano_nasc < 18:
        contmenor += 1
print('Temos {} pessoas maiores de 18 anos.'.format(contmaior))
print('Temos {} pessoas menores de 18 anos.'.format(contmenor))


