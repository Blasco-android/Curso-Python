palavras = ('PYTHON', 'JAVA', 'RODRIGO', 'SANDRA', 'DJANGO')

for p in palavras:
    print(f'\nVogais em {p}: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
