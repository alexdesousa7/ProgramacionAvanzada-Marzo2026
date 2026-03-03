# Interfaces in Python:

# No hay una palabra reservada interfaz como tal, son clases abstractas y tienes
# que obligar de alguna forma a que se implementen sus métodos (por ejemplo, 
# lanzando excepción en caso contrario)

class FileManagerInterface:

    def save_file(self):
        raise Exception("You must implement this method!")

class ImageManager(FileManagerInterface):
    pass

# Formas de importar

# No importar con la forma --> from modulo import *
# El asterisco se trae todo lo que esté definido! Puedes estar sobrescribiendo
# funciones, constantes... que se llamen igual en dos módulos diferentes.
PI = 7.28


# Comprehensions: Muy usado en Python para listas, diccionarios...
squares = [num*num for num in range (10)]

# Dunders: son los métodos con doble underscore, los que trae ya Python
# (__eq__ por ejemplo)

# Argumentos por defecto: mejor poner tipos inmutables, básicos, cuidado 
# con poner listas!!
def check_stock(my_var=[]):
    my_var.append(5)
    print(my_var)

check_stock()
check_stock() # Inesperado!!

# Mejor:
def check_stock(my_var=None):
    if my_var is None:
        my_var = []
    my_var.append(5)
    print(my_var)
