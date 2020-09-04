from CursoPython.mundo3.fase22.modulos.moedas import aumentar, diminuir, moeda

valor = float(input('Digite um valor: '))
print(f'A metade de {moeda(valor)} é: {moeda(diminuir(valor, 50))}')
print(f'O dobro de {moeda(valor)} é: {moeda(aumentar(valor, 50))}')
print(f'Aumentando 10%, temos: {moeda(aumentar(valor, 10))}')