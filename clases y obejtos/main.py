from personaje import * 
from Armas import * 
#creamos el objeto de la clase personaje  
spartan = Personaje()
Arma= Armas()

#Usamos los atributos Spartan
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Usamos los metodos del Spartan
spartan.correr(False)
spartan.lanzarGranada()

#Usamos los metodos del arma
Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(65)
