artileiro = dict()
partida = list()


artileiro['nome'] = input('Nome do Jogador: ')
jogos = int(input(f'Quantas partidas {artileiro["nome"]} jogou? '))
for i in range(0, jogos):
    gol = int(input(f'Gols na {i+1}° partida: '))
    partida.append(gol)
artileiro['gols'] = partida[:]
artileiro['total'] = sum(partida)

print('=-'*30)
print(artileiro)
print('=-'*30)
for k, v in artileiro.items():
    print(f'O Campo {k} tem o valor {v}')

print('=-'*30)
print(f'O jogador {artileiro["nome"]} jogou {jogos} partidas.')
for i, v in enumerate(artileiro['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {artileiro["total"]} gols')
print('=-'*30)
