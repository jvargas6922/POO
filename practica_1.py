"""
¿En qué consistirá la Demo?
Vamos a crear una clase Persona con atributos simples y un método que permita al objeto “presentarse”.
1. Definir una clase Persona con el método especial __init__() (listo)
2. Asignar atributos: nombre, edad (listo)
3. Crear el método presentarse() que imprima una presentación(listo)
4. Instanciar dos objetos diferentes con datos propios (listo)
5. Ejecutar el método presentarse() desde cada objeto (listo)
6. Ver cómo cada objeto mantiene su propio estado (listo)
7. Bonus: Agregar otro método, como cumplir_anios() que sume 1 a la edad
📌 Objetivo: visualizar cómo una clase puede generar múltiples objetos, cada uno con su identidad y
comportamiento.
"""
from datetime import datetime
class Persona:
    def __init__(self, nombre, edad, fecha_nacimiento):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        # self.edad = self.edad + 1
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")

    def cumpleanios(self):
        # validar si la fecha de hoy es igual a la fecha de nacimiento
        hoy = datetime.now()
        if hoy.day == self.fecha_nacimiento.day and hoy.month == self.fecha_nacimiento.month:
            self.cumplir_anios()
            print(f" La edad de la persona por su fecha de nacimiento es {hoy.year - self.fecha_nacimiento.year}")



# Estatica
# persona = Persona("Joffred", 38)
# persona.presentarse()
# persona.cumplir_anios()
# print(*"---" * 10)
# cliente = Persona("Ana", 33)
# cliente.presentarse()
# cliente.cumplir_anios()

# dinamica
# validacion de campo nombre

# hoy = datetime.now()
# print(hoy)
# print("mes actual:", hoy.month)
# print("dia actual:", hoy.day)
# print(f"Hoy es {hoy.day}/{hoy.month}/{hoy.year}")



while True:
    nombre = input("ingrese su nombre: ")
    if nombre.strip() != "" and not nombre.isdigit():
        break
    else:
        print("Por favor ingrese un nombre válido.")

# validacion de campo edad
while True:
    edad = input("ingrese su edad: ")
    if edad.isdigit() and int(edad) > 0:
        edad = int(edad)
        break
    else:
        print("Por favor ingrese una edad válida.")

fecha_nacimiento = input("Ingrese su fecha de nacimiento (año/mes/dia): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
print("Fecha de nacimiento ingresada:", fecha_nacimiento)

persona = Persona(nombre, edad, fecha_nacimiento)
persona.presentarse()
# persona.cumplir_anios()
persona.cumpleanios()





