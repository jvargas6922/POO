"""
Ejemplo de persona y auto en Python
"""
import datetime
class Persona:
    # contructor
    def __init__(self, nombre, apellido, edad, dni ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
class Auto:
    # constructor
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def descripcion_auto(self):
        return f"{self.marca} {self.modelo} {self.anio} {self.color}"
    
    def es_auto_nuevo(self):
        if self.anio >= datetime.datetime.now().year - 1:
            return True
        else:
            return False
        
print("el siguiente programa permite registrar el auto de las personas:")
print("Ingrese los datos del Dueño/a del auto")
nombre = input("Nombre:")
apellido = input("Apellido:")
edad = (input("Edad:")) # str
edad = int(edad) # int
dni = input("DNI:")
propietario = Persona(nombre, apellido, edad, dni)
nombre_completo = propietario.nombre_completo()
print(f"el nombre del propietario es: {nombre_completo}")

if propietario.mayor_edad():
    print("Puede ingresar los datos del auto")
    print("Ingrese los datos del Auto")
    marca = input("Marca:")
    modelo = input("Modelo:")
    anio = (input("Año:")) # str
    anio = int(anio) # int
    color = input("Color:")
    auto = Auto(marca, modelo, anio, color)
    descripcion_auto = auto.descripcion_auto()
    print(f"La descripcion del auto es: {descripcion_auto}")
    if auto.es_auto_nuevo():
        print("El auto es nuevo")
    else:
        print("El auto no es nuevo")
else:
    print("No puede ingresar los datos del auto, es menor de edad")
    exit()

    

