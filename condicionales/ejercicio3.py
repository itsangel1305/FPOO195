# Solicitar al usuario la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 110
else:
    precio_entrada = 190

# Mostrar el precio de la entrada
print(f"El precio de la entrada es: ${precio_entrada}")
