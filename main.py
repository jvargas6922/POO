# importar clases
from practica_1 import Persona
from practica_3 import Celular
from practica_4 import Mascota
from datetime import datetime

# crear una instancia de Persona, Mascota, Celular,

persona = Persona("Joffred", 38, datetime(1985, 5, 15))
persona.presentarse()
persona.cumpleanios()

celular = Celular("Apple", "iPhone 13", 256)
celular.encender()
celular.mostrar_info()
celular.apagar()