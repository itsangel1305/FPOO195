from tkinter import Tk, Frame

#1.Creamos la ventana
Ventana= Tk() # Uso de poo creando un objeto ventana
Ventana.title("Ejemplo con 3 frames")
Ventana.geometry("600x400")

#2. Colocamos frames de la ventana
seccion1= Frame(Ventana,bg="blue")
seccion1.pack(expand= True,fill='both')

seccion2= Frame(Ventana,bg="green")
seccion2.pack(expand= True,fill='both')

seccion3= Frame(Ventana,bg="purple")
seccion3.pack(expand= True,fill='both')


#Ejecuta la ventana
Ventana.mainloop()
