

class Cuenta:
    def __init__(self, numero_cuenta, titular, edad, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad

