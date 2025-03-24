# Lista vacía de alumnos 
alumnos = []

print("¡Te damos la bienvenida a la escuela ---!")
print("Para empezar tienes que registrarte.")

while True:
    print("\n📋 LISTA DE ALUMNOS📋")
    print("1. registrar alumno")
    print("4. Dar de baja a alumno")
    print("2. Ver lista de alumnos")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        Nombre = input("Ingrese su nombre")
        Edad = input("ingrese su edad")
        Calificación = input("ingrese su calificación")

