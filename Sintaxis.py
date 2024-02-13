# Practica2: Sintaxis Python

# 1. Comentarios

# Soy un comentario

'''
Soy un 
comentario 
de varias líneas
'''

# 2. Cadenas

'''
print('Soy una cadena')
print("Soy una cadena")
'''

a = 'Mi banda favorita es\n'
b = "Grupo Marrano"
print(a + b)
print(a, b)

# Contar los caracteres
print(len(a))

print(b[2:5])
print(b[:5])
print(b[2:])

# 3. Variables

x = int(3)
y = str("3")
z = float(3.2)

print(type(x))
print(type(y))
print(type(z))

import random

numero = random.randrange(1, 15)
print(numero)

# 4. Solicitud de datos

var1 = input("Introduce cualquier dato: ")
var2 = str(input("Introduce cadenas: "))
var3 = int(input("Introduce solo enteros: "))
var4 = float(input("Introduce números decimales: "))

print(var1, var2, var3, var4)
''''''

#5. Booleans, operadores de comparación y logicos

print(10> 9)
print(10== 9)
print(10< 9)
print(10 >= 9)
print(10 != 9)
print(10 <= 9)


x=1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not(x < 5 and x < 10))


#para operaciones binarias
print(x < 5 & x < 10)
print(x < 5 & x < 10)
print(x < 5 & x < 10)