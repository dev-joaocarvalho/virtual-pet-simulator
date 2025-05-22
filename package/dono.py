class Dono:
    def __init__(self, nome):
        self.nome = nome
        self.pet = None  # Associação fraca

    def adotar_pet(self, pet):
        self.pet = pet
