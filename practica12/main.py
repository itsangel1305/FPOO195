from tkinter import messagebox
from Logintkinter import mostrarMensajes, addbtn

class Usuario:
    usuarios = []

    def __init__(self, id, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        Usuario.usuarios.append(self)

def agregar_usuario():
    id = int(input("Ingrese el ID del usuario: "))  
    nombre = input("Ingrese el nombre del usuario: ")
    correo = input("Ingrese el correo electrónico del usuario: ")
    contraseña = input("Ingrese la contraseña del usuario: ")
    Usuario(id, nombre, correo, contraseña)  
    mostrarMensajes(correo, contraseña)
    addbtn(correo, contraseña)
    
agregar_usuario()