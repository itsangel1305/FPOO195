# Almacenar la contraseña en una variable
contraseña_guardada = "MiContraseña123"

# Solicitar al usuario una contraseña
contraseña_ingresada = input("Ingrese la contraseña: ")

# Verificar si la contraseña coincide (sin distinción de mayúsculas/minúsculas)
if contraseña_guardada.lower() == contraseña_ingresada.lower():
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")
