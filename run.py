from entradas import Entradas
from equacoes.segundo_grau import SegundoGrau


print('Exemplo de entrada x²+5x+6 | x²+4x+4 | x²+6x+13')
entrada_str = str(input('Digite: '))

segundo_grau = SegundoGrau(
    entradas=Entradas(entrada_str)
)

raiz_1, raiz_2, delta = segundo_grau.executar()
print('raiz_1', raiz_1)
print('raiz_2', raiz_2)
print('delta', delta)
