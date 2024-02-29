from usuario import Usuario

def agregar_usuario():
    id = int(input("Ingrese el ID del usuario: "))  
    nombre = input("Ingrese el nombre del usuario: ")
    correo = input("Ingrese el correo electrónico del usuario: ")
    contraseña = input("Ingrese la contraseña del usuario: ")
    Usuario(id, nombre, correo, contraseña)  
def consultar_usuarios():
    for usuario in Usuario.usuarios:
        print(usuario.consultar_usuario())

def editar_usuario():
    id = int(input("Ingrese el ID del usuario a editar: "))  
    nombre = input("Ingrese el nuevo nombre del usuario: ")
    correo = input("Ingrese el nuevo correo electrónico del usuario: ")
    contraseña = input("Ingrese la nueva contraseña del usuario: ")
    if Usuario.editar_usuario(id, nombre, correo, contraseña):
        print("Usuario actualizado.")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    id = int(input("Ingrese el ID del usuario a eliminar: ")) 
    if Usuario.eliminar_usuario(id):  
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

def menu():
    while True:
        print("\n[1] Agregar usuario")
        print("[2] Mostrar usuarios")
        print("[3] Editar usuario")
        print("[4] Eliminar usuario")
        print("[5] Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            consultar_usuarios()
        elif opcion == '3':
            editar_usuario()
        elif opcion == '4':
            eliminar_usuario()
        elif opcion == '5':
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")

menu()
