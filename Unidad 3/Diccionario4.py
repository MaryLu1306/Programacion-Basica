#programa de diccionarios número 4

# Crear un diccionario con más de dos valores por clave
compañeros = {
    "Aaron": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Enrique": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Sabayd": {"carrera": "Ingenieria Mecatrónica", "edad": 19},
    "Alexa": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Manuel": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Victor": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Cristian": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Arturo": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Roberto": {"carrera": "Ingenieria Mecatrónica", "edad": 18},
    "Oswaldo": {"carrera": "Ingenieria Mecatrónica", "edad": 18}
}

# Imprimir el diccionario completo
print("Diccionario de compañeros:")
for nombre, detalles in compañeros.items():
    print(f"{nombre}: {detalles}")