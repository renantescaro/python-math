import re
from typing import Tuple


class Entradas:
    def __init__(self, entrada:str) -> None:
        self.entrada:str = entrada


    def _pegar_coeficiente(self, texto:str) -> int:
        texto = texto.replace('²', '')
        texto = texto.replace('X', '')
        texto = '-1' if texto in {'-', '-1'} else texto
        texto = '1' if texto in {'', '+', '+1'} else texto
        return int(texto)


    def executar(self) -> Tuple[int, int, int]:
        try:
            entrada = ''.join(self.entrada.split())
            entrada = entrada.replace('^2', '²')
            entrada = entrada.replace('–', '-')
            entrada = entrada.upper()

            if entrada.startswith('X') or entrada[0].isdigit():
                entrada = f'+{entrada}'

            lista = re.findall('[+-][0-9]?.X?²?', entrada)

            a = self._pegar_coeficiente(lista[0])
            b = self._pegar_coeficiente(lista[1])
            c = self._pegar_coeficiente(lista[2])

            return a, b, c

        except Exception as e:
            print(e)
