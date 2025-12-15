"""
Programacion estructura VS POO
"""

# Programacion Estructurada
# def crear_cliente(nombre, edad):
#     return {'nombre': nombre, 'edad': edad}

# def saludar(cliente):
#     print(f"Hola, {cliente['nombre']}")

# cliente = crear_cliente("Joffred", 39)
# saludar(cliente)

#POO (Programacion Orientada a Objetos)
class Cliente:
    # contructor
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, {self.nombre}")

cliente = Cliente("Joffred", 39)
Cliente.saludar(cliente)

