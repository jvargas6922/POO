"""
Ejemplo de cuenta bancaria con clases en Python
"""
class CuentaBancaria:
    # constructor
    def __init__(self, titular, saldo,tipo_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")

    def retirar(self,retirar):
        if retirar > self.saldo:
            print("Fondos insuficientes para retirar.")
        else:
            self.saldo -= retirar
            print(f"Retiro de {retirar} realizado. Nuevo saldo: {self.saldo}")

    def consultar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")

cuenta_1 = CuentaBancaria("Joffred Vargas", 1000, "Ahorros")
cuenta_1.consultar_saldo()
cuenta_1.depositar(20000)
cuenta_1.retirar(2000)