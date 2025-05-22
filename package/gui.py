import tkinter as tk
from tkinter import messagebox, simpledialog
from .pets import Cachorro, Gato
from .database import BancoDeDados
from .dono import Dono

class PetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet Simulator")
        self.pet = None
        self.dono = Dono("Jogador")  # Associação fraca
        self.criar_interface()

    def criar_interface(self):
        tk.Button(self.root, text="Adotar Cachorro", command=lambda: self.adotar_pet("Cachorro")).pack()
        tk.Button(self.root, text="Adotar Gato", command=lambda: self.adotar_pet("Gato")).pack()
        tk.Button(self.root, text="Alimentar", command=self.alimentar_pet).pack()
        tk.Button(self.root, text="Brincar", command=self.brincar_pet).pack()
        tk.Button(self.root, text="Ver Status", command=self.mostrar_status).pack()
        tk.Button(self.root, text="Salvar", command=self.salvar_pet).pack()
        tk.Button(self.root, text="Carregar", command=self.carregar_pet).pack()

    def adotar_pet(self, especie):
        nome = simpledialog.askstring("Nome", "Digite o nome do pet:")
        if nome:
            self.pet = Cachorro(nome) if especie == "Cachorro" else Gato(nome)
            self.dono.adotar_pet(self.pet)  # Associação fraca
            messagebox.showinfo("Sucesso", f"{nome} foi adotado!")

    def alimentar_pet(self):
        if self.pet and self.pet.inventario.usar_comida():
            self.pet.comer(10)
            messagebox.showinfo("Info", f"{self.pet._nome} foi alimentado!")
        else:
            messagebox.showwarning("Erro", "Sem comida no inventário!")

    def brincar_pet(self):
        if self.pet and self.pet.inventario.usar_brinquedo():
            self.pet.brincar()
            messagebox.showinfo("Info", f"{self.pet._nome} brincou!")
        else:
            messagebox.showwarning("Erro", "Sem brinquedos!")

    def mostrar_status(self):
        if self.pet:
            status = "\n".join([f"{k}: {v}" for k, v in self.pet.get_status().items()])
            messagebox.showinfo("Status", status)

    def salvar_pet(self):
        if self.pet:
            BancoDeDados.salvar_pet(self.pet)
            messagebox.showinfo("Sucesso", "Progresso salvo!")

    def carregar_pet(self):
        self.pet = BancoDeDados.carregar_pet()
        if self.pet:
            self.dono.adotar_pet(self.pet)
            messagebox.showinfo("Sucesso", f"{self.pet._nome} carregado!")
