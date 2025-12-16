"""
¿En qué consistirá la Demo?
Vamos a demostrar, con código y conceptos, cómo crear una instancia (objeto) a partir de una clase, y cómo comprobar que pertenece a esa clase.
1. Definir una clase simple llamada Animal con atributo nombre y método hablar()(listo)
2. Crear una instancia de Animal llamada mi_gato (listo)
3. Ejecutar un método desde la instancia (listo)
4. Comprobar con isinstance() que mi_gato es una instancia de Animal (listo)
5. Mostrar que una instancia tiene vida propia y puede almacenarse, pasarse como parámetro, o
    guardarse en listas
📌 Objetivo: entender que una instancia es un objeto real creado a partir de una clase, y que puede
verificarse con herramientas como isinstance().
"""

class Animal:
    # contructor
    def __init__(self, nombre):
        self.nombre = nombre

    #metodo hablar
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"
        # print(f"{self.nombre} dice: ¡Miau!")


class Animal_2:
    # contructor
    def __init__(self, nombre):
        self.nombre = nombre

    #metodo hablar
    def hablar(self):
        return f"{self.nombre} dice: ¡Gauuu!"
        # print(f"{self.nombre} dice: ¡Miau!")
    
mi_gato = Animal("Pelusa")
# mi_gato.hablar()
print(mi_gato.hablar())

mi_perro = Animal_2("Rex")
print(mi_perro.hablar())

# Comprobar que mi_gato es una instancia de Animal
if isinstance(mi_perro, Animal):
    print(f"{mi_perro.nombre} es una instancia de la clase Animal.")
else:
    print(f"{mi_perro.nombre} no es una instancia de la clase Animal.")