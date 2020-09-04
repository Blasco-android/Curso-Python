from time import sleep


def lin():
    print('=-' * 30)


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if i < f:
        for c in range(i, f+1, p):
            print(f'  {c} ', end='')
            sleep(0.5)
        print('--> fim')
    if i > f:
        for c in range(i, f-1, -p):
            print(f'  {c} ', end='')
            sleep(0.5)
        print('--> fim')


lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('  Inicio: '))
fim = int(input('  Fim:    '))
passo = int(input('  Passo:  '))
contador(inicio, fim, passo)
lin()
