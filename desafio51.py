termo1 = int(input('Digite o primeiro termo de um PA: '))
ra = int(input('Digite a razão desta PA: '))
dez = termo1 + (10-1) * ra

for pa in range(termo1, dez + ra, ra):
    print('{}'.format(pa), end=' → ')
