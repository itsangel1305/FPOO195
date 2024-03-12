class Usuario:
    usuarios = []

    def __init__(self, id, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        Usuario.usuarios.append(self)

    @classmethod
    def verificar_usuario(cls, correo, contraseña):
        for usuario in cls.usuarios:
            if usuario.correo == correo and usuario.contraseña == contraseña:
                return usuario
        return None

