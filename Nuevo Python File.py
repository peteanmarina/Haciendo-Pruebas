# Leer el archivo JSON
with open('datos.json', 'r') as archivo:
    contenido = archivo.read()

# Convertir el contenido en un diccionario
datos = eval(contenido)

# Acceder a los datos
nombre = datos['nombre']
edad = datos['edad']
ciudad = datos['ciudad']

# Imprimir los datos
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# Datos a escribir en el archivo JSON
datos = {
    "nombre": "María",
    "edad": 25,
    "ciudad": "Barcelona"
}

# Convertir los datos en una cadena de texto en formato JSON
contenido = str(datos)

# Escribir los datos en el archivo JSON
with open('nuevos_datos.json', 'w') as archivo:
    archivo.write(contenido)

print("Archivo JSON creado correctamente.")
