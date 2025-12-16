"""
Contexto: 🙌
Imaginá que tienes que modelar un objeto del mundo real en código. Queremos representar un celular como
clase, con su información principal y funciones básicas.
Consigna: ✍
Creá una clase Celular que tenga los siguientes elementos:
    ● Atributos: marca, modelo, almacenamiento (listo)
    ● Método encender() que imprima "Encendiendo {marca} {modelo}..."
    ● Método mostrar_info() que muestre todos los atributos
"""
class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}...")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento} GB")

    def apagar(self):
        print(f"Apagando {self.marca} {self.modelo}...")

# instancia de forma estatica
s3 = Celular("Samsung", "Galaxy S21", 128)
s3.encender()
s3.mostrar_info()

# instancia de forma dinamica
marca = input("Ingrese la marca del celular: ")
modelo = input("Ingrese el modelo del celular: ")
almacenamiento = input("Ingrese el almacenamiento del celular (en GB): ")
almacenamiento = int(almacenamiento)  # Convertir a entero
print(*"---" * 20)
celular = Celular(marca, modelo, almacenamiento)
celular.encender()
celular.mostrar_info()
celular.apagar()
