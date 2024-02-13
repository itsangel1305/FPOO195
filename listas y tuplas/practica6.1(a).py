def capturar_numeros():
    return tuple((int, input("Ingresa números separados por espacio: ")()))

def calcular_numeros(nums):
    moda = max(set(nums), key=nums.count)
    return {
        'Sumatoria': sum(nums),
        'Número mayor': max(nums),
        'Número menor': min(nums),
        'Promedio': sum(nums) / len(nums),
        'Moda': moda,
        'Rango': max(nums) - min(nums)
    }

def menu():
    nums = capturar_numeros()
    opciones = ['Sumatoria', 'Número mayor', 'Número menor', 'Promedio', 'Moda', 'Rango', 'Salir']
    while True:
        print("\n".join(f"{i}. {opcion}" for i, opcion in enumerate(opciones, 1)))
        opcion = input("Elige una opción: ")
        
        if opcion == '7':
            print("Saliendo del programa...")
            break
        elif opcion in [str(i) for i in range(1, 7)]:
            numeros = calcular_numeros(nums)
            print(opciones[int(opcion)-1] + ":", numeros[opciones[int(opcion)-1]])
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
