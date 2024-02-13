from statistics import multimode

def capturar_numeros():
    return tuple(map(int, input("Ingresa números separados por espacio: ").split()))

def menu():
    nums = capturar_numeros()
    operaciones = {
        '1': ('Sumatoria', lambda nums: sum(nums)),
        '2': ('Número mayor', lambda nums: max(nums)),
        '3': ('Número menor', lambda nums: min(nums)),
        '4': ('Promedio', lambda nums: sum(nums) / len(nums)),
        '5': ('Moda', lambda nums: multimode(nums)),
        '6': ('Rango', lambda nums: max(nums) - min(nums)),
    }

    while True:
        print("\n1. Sumatoria de los elementos de la lista")
        print("2. Número mayor de la lista")
        print("3. Número menor de la lista")
        print("4. Promedio")
        print("5. Moda")
        print("6. Rango")
        print("7. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '7':
            print("Saliendo del programa...")
            break
        elif opcion in operaciones:
            operacion, funcion = operaciones[opcion]
            resultado = funcion(nums)
            print(f"{operacion}: {resultado}")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

