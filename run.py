from entradas import Entradas
from equacoes.segundo_grau import SegundoGrau
from grafico import Grafico


print('Exemplo de entrada x²+5x+6 | +x²+4x+4 | x²+6x+13')
entrada_str = str(input('Digite: '))

entradas = Entradas(entrada_str)
segundo_grau = SegundoGrau(
    entradas=entradas
)
raiz_1, raiz_2, delta = segundo_grau.executar()
print('raiz_1', raiz_1)
print('raiz_2', raiz_2)
print('delta', delta)

grafico = Grafico(
    a=entradas.a,
    b=entradas.b,
    c=entradas.c,
    equacao=entradas.equacao
)
grafico.executar()
