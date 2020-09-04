from CursoPython.mundo3.fase22.modulos.moedas import aumentar, diminuir

valor = float(input('Digite um valor: '))
print(f'A metade de {valor} é: {diminuir(valor, 50)}')
print(f'O dobro de {valor} é: {aumentar(valor, 50)}')
print(f'Aumentando 10%, temos: {aumentar(valor, 10)}')
