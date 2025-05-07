
from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv

archivo = "datos.csv"

#Nombre del archivo
datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]

guardar_diccionarios_en_csv(archivo, datos)

leer_diccionarios_de_csv(archivo)

datos_leidos = leer_diccionarios_de_csv(archivo)
print("Datos leídos del archivo CSV:")
print(datos_leidos)
