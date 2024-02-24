class Armas:
    
    def seleccionarArma(self,nombre):
        seleccion= int(input("Seleccionar el arma:\n 1=Riflede asalto\n 2= Espada energia\n 3= Rifle M392"))
        
        if(seleccion == 1):
            print("rifle de asalto asignado a "+ nombre)
            print("Municiones 7.62 * 52mm, sin Mira")
            
        if(seleccion == 2):
            print("Espada de energia asignada a"+ nombre)
            print("Arma creada por los Shagheili")
        
        if(seleccion == 3):
            print("rifle M392 asignada a "+ nombre)
            print("Municiones 7.62 * 52mm, con Mira")    
         
    def recargarArma(self, municion):
            cargador= 25
            cargador= cargador + municion
            print("Arma recargada al "+ str(cargador)+ "%")
            