class Inventario:
    def __init__(self):
        self._itens = {"Comida": 5, "Brinquedos": 3}

    def usar_comida(self):
        if self._itens["Comida"] > 0:
            self._itens["Comida"] -= 1
            return True
        return False

    def usar_brinquedo(self):
        if self._itens["Brinquedos"] > 0:
            self._itens["Brinquedos"] -= 1
            return True
        return False
