"""
Contexto: 🙌
Queremos simular un grupo de mascotas, cada una representada por un objeto. 
Las mascotas pueden tener distintas edades, y vamos a clasificarlas.
Consigna: ✍
Creá una clase Mascota con:(listo)
    ● Atributos: nombre, edad, tipo (listo)
    ● Método presentarse() que diga "Soy {nombre}, un/a {tipo} de {edad} años." (listo)
    ● Método es_joven() que devuelva True si tiene menos de 5 años (listo)
"""

class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años.")

    def es_joven(self):
        if self.edad < 5:
            return True
        else:
            return False
        

def validar_texto(texto):
    if texto.strip() != "" and not texto.isdigit():
        return True
    else:
        return False
    
def validar_numero(numero):
    if numero.isdigit() and int(numero) > 0:
        return True
    else:
        return False

# validacion de campo nombre  
# while True:
#     nombre = input("ingrese su nombre: ")
#     if nombre.strip() != "" and not nombre.isdigit():
#         break
#     else:
#         print("Por favor ingrese un nombre válido.")

# validacion de campo edad
# while True:
#     edad = input("ingrese su edad: ")
#     if edad.isdigit() and int(edad) > 0:
#         edad = int(edad)
#         break
#     else:
#         print("Por favor ingrese una edad válida.")

# validacion de campo tipo
# while True:
#     tipo = input("ingrese su tipo: ")
#     if tipo.strip() != "" and not tipo.isdigit():
#         break
#     else:
#         print("Por favor ingrese un tipo válido.")

# mascota = Mascota(nombre, edad, tipo) 
# mascota.presentarse()
# if mascota.es_joven():
#     print(f"{mascota.nombre} es joven.")
# else:
#         print(f"{mascota.nombre} es vieja.") 


# Crear 3 mascotas con datos ingresados por el usuario
mascotas = []
cantidad_mascotas = 3

for i in range(cantidad_mascotas):
    print(f"\nIngresando datos para la mascota {i + 1}:")
    
    while True:
        nombre = input("Ingrese el nombre de la mascota: ")
        if validar_texto(nombre):
            break
        else:
            print("Por favor ingrese un nombre válido.")
    
    while True:
        edad = input("Ingrese la edad de la mascota: ")
        if validar_numero(edad):
            edad = int(edad)
            break
        else:
            print("Por favor ingrese una edad válida.")
    
    while True:
        tipo = input("Ingrese el tipo de mascota (ej. perro, gato): ")
        if validar_texto(tipo):
            break
        else:
            print("Por favor ingrese un tipo válido.")
    
    mascota = Mascota(nombre, edad, tipo)
    mascotas.append(mascota)

# Mostrar la información de cada mascota y si es joven o vieja
for mascota in mascotas:
    print(*"---" * 10)
    mascota.presentarse()
    if mascota.es_joven():
        print(f"{mascota.nombre} es joven.")
    else:
        print(f"{mascota.nombre} es vieja.")
