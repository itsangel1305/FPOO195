import tkinter as tk
from tkinter import messagebox
from persona import Usuario



class LoginInterfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        
        self.label_correo = tk.Label(master, text="Correo:")
        self.label_correo.pack()
        self.entry_correo = tk.Entry(master)
        self.entry_correo.pack()
        
        self.label_contraseña = tk.Label(master, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()
        
        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()
        if correo == "" or contraseña == "":
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        usuario = Usuario.verificar_usuario(correo, contraseña)
        if usuario:
            messagebox.showinfo("Bienvenido", f"¡Login exitoso! Usuario: {usuario.nombre}")
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos.")

def main():
    root = tk.Tk()
    login_interfaz = LoginInterfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()

