"""
    Guarda información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, cedula, edad

#Ingreso nuevo registro 1
nombre = "Felix"
apellido = "Torres Jara"
cedula = "1011019092"
edad = 31
cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# ejecutar el SQL
cursor.execute(cadena_sql)

#Ingreso nuevo registro 2
nombre = "Andrea"
apellido = "Espinoza Torres"
cedula = "1011019093"
edad = 30
cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)

# ejecutar el SQL
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
