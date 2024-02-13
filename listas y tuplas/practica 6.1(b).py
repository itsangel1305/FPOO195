import random


valores = [random.randint(10, 20) for _ in range(30)]
print("Lista generada:", valores)

def operaciones_lista(opcion, lista):
    if opcion == 'a':  # Contar números repetidos
        repetidos = {x: lista.count(x) for x in set(lista) if lista.count(x) > 1}
        print("Números repetidos y su cantidad:", repetidos)
    elif opcion == 'b':  # Eliminar números repetidos
        return list(set(lista))
    elif opcion == 'c':  # Reemplazar los repetidos con 0
        repetidos = {x for x in lista if lista.count(x) > 1}
        return [0 if x in repetidos else x for x in lista]
    return lista


while True:
    print("\nOpciones:")
    print("a. Contar números repetidos")
    print("b. Eliminar números repetidos")
    print("c. Reemplazar los repetidos con 0")
    print("d. Salir")
    opcion = input("Elige una opción: ").lower()

    if opcion == 'd':
        print("Saliendo del programa...")
        break
    elif opcion in ['a', 'b', 'c']:
        valores = operaciones_lista(opcion, valores)
        if opcion != 'a':  
            print("Lista actualizada:", valores)
    else:
        print("Opción no válida. Intente de nuevo.")
