"""
Ejemplo de Persona POO en Python
"""
class Persona:
    # constructor
    def __init__(self, nombre, apellido, sexo, fecha_nacimiento, edad, rut = "12345678-9"):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad
        self.rut = rut

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Sexo: {self.sexo}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Edad: {self.edad}")
        print(f"RUT: {self.rut}")

    def mayor_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")
    
persona_1 = Persona("Joffred", "Vargas", "Masculino", "01-01-1985", 39)
persona_1.mostrar_info()

persona_2 = Persona("Daniela", "Gonzalez", "Femenino", "09-11-1989", 36, "12345448-9")
persona_2.mostrar_info()
persona_2.mayor_edad()