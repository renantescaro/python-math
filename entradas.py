import re
from typing import Tuple


class Entradas:
    def __init__(self, entrada:str) -> None:
        self.equacao:str = entrada
        self.a: int = 0
        self.b: int = 0
        self.c: int = 0


    def _pegar_coeficiente(self, texto:str) -> int:
        texto = texto.replace('²', '')
        texto = texto.replace('X', '')
        texto = '-1' if texto in {'-', '-1'} else texto
        texto = '1' if texto in {'', '+', '+1'} else texto
        return int(texto)


    def _preparar_entrada(self, entrada:str) -> str:
        entrada = ''.join(entrada.split())
        entrada = entrada.replace('^2', '²')
        entrada = entrada.replace('–', '-')
        entrada = entrada.upper()

        if entrada.startswith('X') or entrada[0].isdigit():
            entrada = f'+{entrada}'
        return entrada


    def executar(self) -> Tuple[int, int, int]:
        try:
            self.equacao = self._preparar_entrada(self.equacao)

            lista = re.findall('[+-][0-9]?.X?²?', self.equacao)
            self.a = self._pegar_coeficiente(lista[0])
            self.b = self._pegar_coeficiente(lista[1])
            self.c = self._pegar_coeficiente(lista[2])

            return self.a, self.b, self.c

        except Exception as e:
            print(e)
