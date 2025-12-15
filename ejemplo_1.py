"""
Ejemplo de Automovil POO en Python
"""

class Automovil:
    #constructor
    def __init__(self, color, marca, modelo, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def arrancar(self):
        print(f"El automóvil {self.marca} {self.modelo} ha arrancado.")

    def frenar(self):
        print(f"El automóvil {self.marca} {self.modelo} está frenando.")

    def acelerar(self):
        print(f"El automóvil {self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")

    def anio(self):
        print(f"El automóvil {self.marca} {self.modelo} es del año 2020.")
        self.anio = 2020


auto = Automovil("Rojo", "Toyota", "Corolla", 120)
auto.arrancar()
auto.frenar()
auto.acelerar()

camioneta = Automovil("Azul", "Ford", "F-150", 100) 
camioneta.arrancar()
camioneta.frenar()
camioneta.acelerar()
camioneta.anio()