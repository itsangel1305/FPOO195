from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

def busUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("Nada", "Usuario no encontrado")
    else:
        resultado.delete('1.0', END)
        usuarioStr = "ID: {}\nNombre: {}\nCorreo: {}\n".format(usuarioBD[0][0], usuarioBD[0][1], usuarioBD[0][2])
        resultado.insert(END, usuarioStr)

def actualizarVistaUsuarios():
    for usuario in usuarios_treeview.get_children():
        usuarios_treeview.delete(usuario)
    usuarios = objControlador.obtenerTodosLosUsuarios()
    for usuario in usuarios:
        usuarios_treeview.insert('', 'end', values=usuario)

def on_tab_changed(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Consultar Usuarios":
        actualizarVistaUsuarios()

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

tab1 = ttk.Frame(panel)
tab2 = ttk.Frame(panel)
tab3 = ttk.Frame(panel)
tab4 = ttk.Frame(panel)
tab5 = ttk.Frame(panel)

panel.add(tab1, text="Agregar Usuario")
panel.add(tab2, text="Buscar Usuario")
panel.add(tab3, text="Consultar Usuarios")
panel.add(tab4, text="Actualizar Usuario")
panel.add(tab5, text="Eliminar Usuario")

Label(tab1, text="Registro de usuarios", fg="black", font=("Modern", 18)).pack()
var1 = tk.StringVar()
Label(tab1, text="Nombre: ").pack()
Entry(tab1, textvariable=var1).pack()
var2 = tk.StringVar()
Label(tab1, text="Correo: ").pack()
Entry(tab1, textvariable=var2).pack()
var3 = tk.StringVar()
Label(tab1, text="Password: ").pack()
Entry(tab1, textvariable=var3).pack()
Button(tab1, text="Guardar usuario", command=ejecutaInsert).pack()

Label(tab2, text="Buscar Usuario", fg="red", font=("Mono", 18)).pack()
varBus = tk.StringVar()
Label(tab2, text="Id: ").pack()
Entry(tab2, textvariable=varBus).pack()
Button(tab2, text="Buscar usuario", command=busUsuario).pack()
Label(tab2, text="Registrado:", fg="blue", font=("Mono", 16)).pack()
resultado = tk.Text(tab2, height=5, width=52)
resultado.pack()

usuarios_treeview = ttk.Treeview(tab3, columns=('ID', 'Nombre', 'Correo'), show='headings')
usuarios_treeview.heading('ID', text='ID')
usuarios_treeview.heading('Nombre', text='Nombre')
usuarios_treeview.heading('Correo', text='Correo')
usuarios_treeview.pack()

panel.bind("<<NotebookTabChanged>>", on_tab_changed)

ventana.mainloop()
