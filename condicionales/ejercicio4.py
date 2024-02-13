# Solicitar una cadena de caracteres al usuario
cadena = input("Ingrese una cadena de caracteres: ")

# Verificar si la cadena es un palíndromo
if cadena.lower() == cadena.lower()[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
