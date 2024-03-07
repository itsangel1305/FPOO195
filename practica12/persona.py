class Usuario:
    usuarios = []

    def __init__(self, id, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        Usuario.usuarios.append(self)

    def verificar_usuario(correo, contraseña):
        for usuario in Usuario.usuarios:
            if usuario.correo == correo and usuario.contraseña == contraseña:
                return True
        return False
