from abc import ABC, abstractmethod
from .inventory import Inventario

class Pet(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._idade = 0
        self._fome = 50
        self._felicidade = 50
        self._saude = 70
        self.inventario = Inventario()  # Composição forte

    @abstractmethod
    def brincar(self):
        pass

    def comer(self, quantidade):
        self._fome = max(0, self._fome - quantidade)
        self._saude = min(100, self._saude + 5)

    def envelhecer(self):
        self._idade += 1

    def get_status(self):
        return {
            "Nome": self._nome,
            "Idade": self._idade,
            "Fome": self._fome,
            "Felicidade": self._felicidade,
            "Saúde": self._saude
        }

class Cachorro(Pet):
    def brincar(self):
        self._felicidade = min(100, self._felicidade + 20)
        self._fome = min(100, self._fome + 10)

class Gato(Pet):
    def brincar(self):
        self._felicidade = min(100, self._felicidade + 15)
        self._fome = min(100, self._fome + 5)
