from CursoPython.mundo3.fase22.modulos.moedas import resumo
from CursoPython.mundo3.fase22.modulos.dados import scan_money

valor = scan_money('Digite um valor: R$ ')
resumo(valor, 20, 10)
