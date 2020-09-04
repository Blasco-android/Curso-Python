#Palindromo se le as mesma palavra ou frase de tras pra frente

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separa as palavras de uma frase ou as letras de uma palavra
junto = ''.join(palavras) #junta as palavras ou substitui os espaço por quaquer outro caracteres

inverso = junto[::-1] #metodo ser o for utilizando fatiamento :inicio :fim -1inverso

'''
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

'''
print(junto, inverso)
if junto == inverso:
    print('PALINDROMO')
else:
    print('NÃO É PALINDROMO')
