from typing import List, Tuple


class Grafico:
    def __init__(self) -> None:
        pass


    def _gerar_valores(self) -> Tuple[List[float], List[float]]:
        valores_x = []
        valores_y = []
        for x in range(-3, 4):
            equacao = '+X²-2X-3'

            equacao = equacao.replace('²', '**2')
            # print(equacao)


            if equacao[:2] in ['+X', '-X']:
                equacao = equacao.replace('X', f'({x})', 1)
            elif equacao[1].isdigit():
                equacao = equacao.replace('X', f'*({x})', 1)

            # print(equacao)

            equacao = equacao.replace('X', f'*({x})', 1)
            # print(equacao)

            valores_x.append(x)
            valores_y.append(eval(equacao))

        return valores_x, valores_y


    def executar(self):
        valores_x, valores_y = self._gerar_valores()

        print(valores_x)
        print(valores_y)
