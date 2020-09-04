artileiro = dict()
partida = list()
tabela = list()

while True:
    # recebe codigo, nome, qnt de partidas, gols por partidas
    artileiro['nome'] = input('Nome do Jogador: ').upper()
    jogos = int(input(f'Quantas partidas {artileiro["nome"]} jogou? '))
    for i in range(0, jogos):
        gol = int(input(f'  Gols na {i+1}° partida: '))
        partida.append(gol)
    artileiro['gols'] = partida[:]
    artileiro['total'] = sum(partida)
    tabela.append(artileiro.copy())
    partida.clear()

    #pergunta se quer salvar mais jogadores ou fechar
    option = input('Deseja continuar [S/ N]: ').upper()
    while option not in 'SN':
        print('ERRO!! - Digite S ou N apenas.')
        option = input('Deseja continuar [S/ N]: ').upper()
    if option == 'N':
        break

# Mostra a tabela de jogadores salvos.
print('=-'*30)
print()
print(f'cod  ', end='')
for i in artileiro.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for k, v in enumerate(tabela):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('=-'*30)

status = int(input('Digite o cod. do jogador para mostrar seus dados(33 - Fecha): '))
while True:
    if status == 33:
        break
    if status >= len(tabela):
        print('ERRO - Não exixte jogador com este codigo.')
    else:
        print('=-'*30)
        print(f'  Levantamento do jogador {tabela[status]["nome"]}:')
        for i, v in enumerate(tabela[status]['gols']):
            print(f'  => Na partida {i+1}, fez {v} gols')
        print('=-'*30)

    status = int(input('Digite o cod. do jogador para mostrar seus dados(0 - Fecha): '))
print('---Thanks for Using---')