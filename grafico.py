from typing import List, Tuple
from matplotlib import pyplot as plt


class Grafico:
    def __init__(self, a: int, b: int, c: int, equacao: str) -> None:
        self.a: int = a
        self.b: int = b
        self.c: int = c
        self.equacao: str = equacao

    def _gerar_valores(self) -> Tuple[List[float], List[float]]:
        valores_x = []
        valores_y = []
        for x in range(-5, 5):
            equacao = self.equacao.replace('²', '**2')

            if equacao[:2] in ['+X', '-X']:
                equacao = equacao.replace('X', f'({x})', 1)
            elif equacao[1].isdigit():
                equacao = equacao.replace('X', f'*({x})', 1)

            equacao = equacao.replace('X', f'*({x})', 1)

            valores_x.append(x)
            valores_y.append(eval(equacao))

        return valores_x, valores_y

    def executar(self):
        valores_x, valores_y = self._gerar_valores()

        fig, ax = plt.subplots()

        ax.plot(valores_x, valores_y, linewidth=2.0)

        print(f'valores_x:{valores_x}')
        print(f'valores_y:{valores_y}')

        ax.set(
            xlim=(0, 8),
            ylim=(0, 8),
            xticks=range(min(valores_x), max(valores_x)),
            yticks=range(min(valores_y), max(valores_y))
        )
        plt.show()
