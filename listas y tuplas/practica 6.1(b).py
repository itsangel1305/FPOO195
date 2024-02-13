from collections import Counter
from statistics import mode

# Función para capturar números del usuario
def capturar_numeros():
    nums = input("Ingresa números separados por espacio: ").split()
    return tuple(map(int, nums))

# Funciones para las operaciones
def sumatoria(nums):
    return sum(nums)

def numero_mayor(nums):
    return max(nums)

def numero_menor(nums):
    return min(nums)

def promedio(nums):
    return sum(nums) / len(nums)

def calcular_moda(nums):
    try:
        return mode(nums)
    except:
        return "No se puede calcular moda con múltiples modas"

def rango(nums):
    return max(nums) - min(nums)

# Función principal
def menu():
    nums = capturar_numeros()
    while True:
        print("\n1. Sumatoria de los elementos de la lista")
        print("2. Número mayor de la lista")
        print("3. Número menor de la lista")
        print("4. Promedio")
        print("5. Moda")
        print("6. Rango")
        print("7. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            print("Sumatoria:", sumatoria(nums))
        elif opcion == '2':
            print("Número mayor:", numero_mayor(nums))
        elif opcion == '3':
            print("Número menor:", numero_menor(nums))
        elif opcion == '4':
            print("Promedio:", promedio(nums))
        elif opcion == '5':
            print("Moda:", calcular_moda(nums))
        elif opcion == '6':
            print("Rango:", rango(nums))
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
