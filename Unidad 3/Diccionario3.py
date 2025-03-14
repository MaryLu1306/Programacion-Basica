#programa de diccionarios número 3

# Crear un diccionario con más de dos valores por clave
profesores = {
    "Eduardo": {"materia": "Programación Basica", "promedio": 8.4},
    "Enrique": {"materia": "Ciencia e Ingenieria de Materiales", "promedio": 9.1},
    "Marlem": {"materia": "Calculo integral", "promedio": 9.7},
    "Guillermo": {"materia": "Estadistica y Control de Calidad", "promedio": 9.0},
    "Adylen": {"materia": "Ingles", "promedio": 10.0},
    "Martha": {"materia": "Administracion y Contabilidad", "promedio": 10.0},
    "Jorge": {"materia": "Algebra Lineal", "promedio": 0}
}

# Imprimir el diccionario completo
print("Diccionario de profesores:")
for nombre, detalles in profesores.items():
    print(f"{nombre}: {detalles}")