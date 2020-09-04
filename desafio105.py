def notas(*nota, sit=False):
    media = sum(nota)/len(nota)
    boletim = {'total': len(nota),
               'maior': max(nota),
               'menor': min(nota),
               'media': media}
    if sit:
        if media < 6:
            boletim['situação'] = 'RUIM'
        elif 8 > media >= 6:
            boletim['situação'] = 'RAZOÁVEL'
        elif media >= 8:
            boletim['situação'] = 'OTIMA'
    return boletim



resp = notas(5.5, 9.0, 9.5, 8.0, 9.5, sit=False)
print(resp)
