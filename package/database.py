
import pickle

class BancoDeDados:
    @staticmethod
    def salvar_pet(pet, filename="pet_save.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(pet, file)

    @staticmethod
    def carregar_pet(filename="pet_save.pkl"):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
