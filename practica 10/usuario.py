class Usuario:
    usuarios = [] 

    def __init__(self, id, nombre, correo, contraseña):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        Usuario.usuarios.append(self) 

    def consultar_usuario(self):
        return (self.__id, self.__nombre, self.__correo)

   
    def editar_usuario(cls, id, nombre, correo, contraseña):
        for usuario in cls.usuarios:
            if usuario.__id == id:
                usuario.__nombre = nombre
                usuario.__correo = correo
                usuario.__contraseña = contraseña
                return True
        return False

    
    def eliminar_usuario(cls, id):
        for i, usuario in enumerate(cls.usuarios):
            if usuario.__id == id:
                del cls.usuarios[i]
                return True
        return False
