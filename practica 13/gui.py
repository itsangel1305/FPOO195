import tkinter as tk
import tkinter.messagebox as messagebox
from clases import PasswordGenerator

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Contraseñas")
        
        self.generator = PasswordGenerator()
        
        self.length_label = tk.Label(master, text="Longitud:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.length_entry = tk.Entry(master)
        self.length_entry.insert(0, "8")
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(master, text="Mayúsculas", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self.special_char_var = tk.IntVar()
        self.special_char_checkbox = tk.Checkbutton(master, text="Caracteres Especiales", variable=self.special_char_var)
        self.special_char_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.generate_button = tk.Button(master, text="Generar Contraseña", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.password_entry = tk.Entry(master, width=30)
        self.password_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def generate_password(self):
        password = self.generator.generate_password(int(self.length_entry.get()), self.uppercase_var.get(), self.special_char_var.get())
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
