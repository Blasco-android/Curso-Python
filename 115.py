from CursoPython.mundo3.fase23.menus import principal, option1, option2, option3
from CursoPython.my_module.colors import yellow, nocolor, red
from time import sleep
from CursoPython.mundo3.fase23.arquivos import busca_arquivo, criar_arquivo, cadastrar


arquivo = 'cadastro.txt'
if not busca_arquivo(arquivo):
    criar_arquivo(arquivo)

while True:
    try:
        principal()
        option = int(input(f'{yellow()}Sua Opção: {nocolor()}'))
        if option == 1:
            option1()
            continue
        elif option == 2:
            option2()
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            cadastrar(arquivo, nome, idade)
            continue
        elif option <= 0 or option > 3:
            print(f'{red()} ERRO - Digite uma opção valida')
            continue
    except ValueError:
        print(f'{red()} ERRO - Digite um numero inteiro')
        continue
    if option == 3:
        break
    sleep(2)
option3()
