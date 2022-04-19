from typing import Any, Tuple
from entradas import Entradas


class SegundoGrau:
    def __init__(self, entradas: Entradas) -> None:
        self._entradas:Entradas = entradas


    def _calcular_delta(self, a:int, b:int, c:int) -> float:
        # Δ = b² - 4*a*c
        return (b**2) - (4*a*c)


    def _calcular_raiz(self, a:int, b:int, delta:float) -> Tuple[Any, Any]:
        # (-b ± √Δ) / 2*a
        raiz_1 = ((-b) - (delta**0.5)) / (2*a)
        raiz_2 = ((-b) + (delta**0.5)) / (2*a)
        return raiz_1, raiz_2


    def executar(self) -> Tuple[Any, Any, float]:
        a, b, c = self._entradas.executar()

        delta = self._calcular_delta(a, b, c)
        raiz_1, raiz_2 = self._calcular_raiz(a, b, delta)
        return raiz_1, raiz_2, delta
