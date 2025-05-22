
class Inventario:
    def __init__(self):
        self._itens = {"Comida": 5, "Brinquedos": 3}

    def usar_comida(self):
        if self._itens["Comida"] > 0:
