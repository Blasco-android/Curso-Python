print('-'*20)
print('SEQUENCIA DE FIBONACCI')
print('-'*20)

n1,n2 = 0, 1
cont = 2
nterms = int(input('How many terms: '))

if nterms <= 0:
    print('Please enter a positive integer!')
elif nterms == 1:
    print('Sequence Fibonacci: ', end='')
    print(n1)
else:
    print('Seuence Fibonacci: ')
    print(n1, ',', n2, end=', ')
    while cont <= nterms:
        nth = n1 + n2
        print(nth, end=' , ')
        n1 = n2
        n2 = nth
        cont += 1

