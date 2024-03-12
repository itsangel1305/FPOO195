import tkinter as tk
from tkinter import messagebox
from persona import Usuario



class LoginInterfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("crear matricula")
        
        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()
        
        self.label_Apellidopaterno = tk.Label(master, text="Apellido paterno:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()
        
        self.label_contraseña = tk.Label(master, text="Apellido materno:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()
        
        self.label_contraseña = tk.Label(master, text= "*")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()
        
        self.label_contraseña = tk.Label(master, text="Carrera:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()
        
        
        self.button_login = tk.Button(master, text="Matricula", command=self.login)
        self.button_login.pack()

    def login(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()
        if correo == "" or contraseña == "":
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        usuario = Usuario.verificar_usuario(correo, contraseña)
        if usuario:
            messagebox.showinfo("Bienvenido", f"¡Matricula creada! matricula: {usuario.nombre}")
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos." )

def main():
    root = tk.Tk()
    login_interfaz = LoginInterfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()










