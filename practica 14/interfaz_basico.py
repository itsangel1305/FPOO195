import tkinter as tk
from tkinter import simpledialog, messagebox
from cuenta_basico import Cuenta

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Cuentas")
        self.cuentas = []

        # Menú principal
        self.menu_principal()

    def menu_principal(self):
        # Limpiar la ventana
        for widget in self.ventana.winfo_children():
            widget.destroy()
        
        tk.Label(self.ventana, text="Menú Principal", font=('Arial', 16)).pack(pady=10)

        tk.Button(self.ventana, text="Crear Nueva Cuenta", command=self.crear_cuenta).pack(fill=tk.X, padx=50, pady=5)
        tk.Button(self.ventana, text="Consultar Saldo", command=self.seleccionar_cuenta_para_consulta).pack(fill=tk.X, padx=50, pady=5)
        tk.Button(self.ventana, text="Ingresar Efectivo", command=lambda: self.seleccionar_cuenta_para_operacion('ingresar')).pack(fill=tk.X, padx=50, pady=5)
        tk.Button(self.ventana, text="Retirar Efectivo", command=lambda: self.seleccionar_cuenta_para_operacion('retirar')).pack(fill=tk.X, padx=50, pady=5)
        tk.Button(self.ventana, text="Salir", command=self.ventana.quit).pack(fill=tk.X, padx=50, pady=5)

    def crear_cuenta(self):
        numero_cuenta = simpledialog.askstring("Crear Cuenta", "Número de cuenta:")
        titular = simpledialog.askstring("Crear Cuenta", "Nombre del titular:")
        edad = simpledialog.askinteger("Crear Cuenta", "Edad del titular:")
        saldo = simpledialog.askfloat("Crear Cuenta", "Saldo inicial:")
        if all([numero_cuenta, titular, edad, saldo]) is not None:
            nueva_cuenta = Cuenta(numero_cuenta, titular, edad, saldo)
            self.cuentas.append(nueva_cuenta)
            messagebox.showinfo("Éxito", "Cuenta creada correctamente.")
        self.menu_principal()

    def seleccionar_cuenta_para_consulta(self):
        self.seleccionar_cuenta('consulta')

    def seleccionar_cuenta_para_operacion(self, operacion):
        self.seleccionar_cuenta(operacion)

    def seleccionar_cuenta(self, operacion):
        if not self.cuentas:
            messagebox.showerror("Error", "No hay cuentas disponibles. Por favor, crea una cuenta primero.")
            return
        

if __name__ == "__main__":
    raiz = tk.Tk()
    app = Aplicacion(raiz)
    raiz.mainloop()