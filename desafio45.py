from random import randint


print('Digite 0 para TESOURA')
print('Digite 1 para PEDRA')
print('Digite 2 para PAPEL')
jogar = int(input('Escolha uma opcao: '))

jogo = 'TESOURA' , 'PEDRA', 'PAPEL'

appjoga = randint(0, 2)

if jogar == appjoga:
    print('EMPATE')
elif jogar == 0 and appjoga == 1:
    print('VC - TESOURA VS APP - ', jogo[appjoga])
    print('VC PERDEU')
elif jogar == 0 and appjoga == 2:
    print('VC - TESOURA VS APP - ', jogo[appjoga])
    print('VC GANHOU')
elif jogar == 1 and appjoga == 0:
    print('VC - PEDRA VS APP - ', jogo[appjoga])
    print('VC GANHOU')
elif jogar == 1 and appjoga == 3:
    print('VC - PEDRA VS APP - ', jogo[appjoga])
    print('VC PERDEU')
elif jogar == 2 and appjoga == 0:
    print('VC - PAPEL VS APP - ', jogo[appjoga])
    print('VC PERDEU')
elif jogar == 2 and appjoga == 1:
    print('VC - PAPEL VS APP - ', jogo[appjoga])
    print('VC PERDEU')
