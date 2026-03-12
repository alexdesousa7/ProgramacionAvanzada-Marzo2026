# SQLAlchemy
# Es un ORM (Object-Relational Mapper)

# Concatenar llamadas a métodos:
my_text = "hola"
my_solution = my_text.upper().lower().capitalize()
# "HOLA".lower().capitalize()
# "hola".capitalize()
# "Hola"
print(my_solution)

# ORM y lazy query: Pseudocódigo (Django)
# my_queryset = Clase.filter("...").all()
# print("Ya he obtenido la queryset")
# my_user = ClaseUser.filter("...")
# my_elem = my_queryset.first() # SABE HACERLO BIEN Y RÁPIDO!!!!

# Un poco la misma línea que con código:
my_even_numbers = [2*i for i in range(100)]
my_last_even_number = my_even_numbers[-1]
my_last_even_number = 198 # !!!

# TODO: Adjuntar extensiones VSCode útiles, unique_together, un ejemplo de relationship.

# Igual que SQLAlchemy te ayuda a mapear a DB...
# ¿Existe alguna opción para que desde un dataframe de Pandas
# (por ejemplo, un Excel) ya te genere tus clases SQLAlchemy?
# --> DEBERES PARA CASA.
# Pandas --> Una librería para trabajar con grandes conjuntos de datos
# de forma eficiente, aplicando filtros etc. --> MUY USADO EN DATA SCIENCE.


# Ejecución de tareas asíncronas:
# Está de moda el encolado y ejecución de las mismas según tenga capacidad
# (la misma idea de recibir eventos e irlos procesando)
# La infraestructura subyacente suele ser un broker de mensajería (Kafka, RabbitMQ, Redis)
