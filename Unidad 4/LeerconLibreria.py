import csv
from Archivos import guardar_diccionarios_en_csv
# Nombre del archivo a leer y de la función a importar

def leer_diccionarios_de_csv(nombre_archivo):
    """Lee un archivo CSV y lo convierte en una lista de diccionarios."""
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return []


def guardar_diccionarios_en_csv(nombre_archivo, lista_diccionarios):
    """Guarda una lista de diccionarios en un archivo CSV."""
    if not lista_diccionarios:
        print("La lista de diccionarios está vacía.")
        return

    encabezados = lista_diccionarios[0].keys()

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        campo_nombres = diccionarios[0].keys()
        escritor = csv.DictWriter(archivo_csv, fieldnames=campo_nombres)
        escritor.writeheader()
        escritor.writerows(diccionarios)

datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]

archivo = "datos.csv"

guardar_diccionarios_en_csv(archivo, datos)
print(f"Datos guardados en {nombre_archivo} exitosamente.")

datos_leidos = leer_diccionarios_de_csv(archivo)
print("Datos leídos del archivo CSV:")
print(datos_leidos)