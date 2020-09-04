from CursoPython.my_module.colors import white_back, close
from CursoPython.my_module.title import title_white_back, title_green_back, title_cyan_back, title_red_back
from time import sleep


def PyHELP(txt):
    title_cyan_back(f'Acessando o Manual do Comando \'{txt}\'')
    sleep(2)
    print(white_back(), end='')
    help(txt)
    print(close(), end='')


while True:
    title_green_back('SISTEMA DE AJUDA PyHELP')
    ajuda = input('Função ou Biblioteca: ')
    if ajuda == 'exit':
        break
    else:
        PyHELP(ajuda)

title_red_back('See You Later!!')
