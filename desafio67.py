# Multiplication Table
from time import sleep

while True:
    print('x='*20)
    n1 = int(input('Which multiplication table wants to know: '))
    if n1 <= 0:
        break

    for n2 in range(1, 11):
        nr = n1 * n2
        print(f' {n1} X {n2:2} = {nr} ')
        sleep(.5)

print('Finish')

