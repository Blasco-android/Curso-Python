r1 = int(input('Digite a primera reta'))
r2 = int(input('Digite a segunda reta'))
r3 = int(input('Digite a terceira reta'))

if r1 < r2+r3 and r2 < r3+r1 and r3 < r2+r1:
    print('forma trinanguo ', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isosceles')

else:
    print('Não forma trinagulo')