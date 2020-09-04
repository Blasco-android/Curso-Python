from CursoPython.my_module.colors import red, close


while True:
    try:
        num = int(input('Digite um numero inteiro: '))
    except:
        print(f'{red()} - ERRO! digite um numero inteiro valido!{close()}')
    else:
        break

while True:
    try:
        num1 = float(input('Digite um numero real: '))
    except:
        print(f'{red()} - ERRO! digite um numero real valido!{close()}')
    else:
        break

print(f'Inteiro: {num} - Real: {num1}')


