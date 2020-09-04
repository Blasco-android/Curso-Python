from CursoPython.mundo3.fase22.modulos.moedas import aumentar, diminuir, moeda

valor = float(input('Digite um valor: '))
print(f'A metade de {moeda(valor)} é: {diminuir(valor, 50, True)}')
print(f'O dobro de {moeda(valor)} é: {aumentar(valor, 50, True)}')
print(f'Aumentando 10%, temos: {aumentar(valor, 10, True)}')
