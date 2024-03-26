from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador: 
    def conexion(self):
        try:
            conex=sqlite3.connect("C:/Users/acidi/OneDrive/Escritorio/POO/FPOO195/tksQLite/db195.db")
            print("conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
            
    def encriptapass(self,cont):
        passPlana=cont
        passPlana= passPlana.encode()
        sal= bcrypt.gensalt()
        passHash= bcrypt.hashpw(passPlana,sal)
        
        return passHash 

    def insertUsuario(self,nom,corr,cont):
        
        conexion= self.conexion()
        
        if( nom== "" or corr== "" or cont== ""):
            messagebox.showwarning("cuidado", "inputs vacios menso")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            conH= self.encriptapass(cont)
            datos=(nom,corr,conH)
            sqlInsert="insert into usuarios(Nombre,Correo,Password) values(?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito", "Eso tilin!!!!")
    
         