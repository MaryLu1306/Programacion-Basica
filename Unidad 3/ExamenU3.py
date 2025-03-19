import time  

# Lista vacía de alumnos 
alumnos = []

print("¡Te damos la bienvenida al Instituto Tecnológico de Pabellón de Arteaga!")
print ("Contamos con formacion en:")
print ("Ingenieria Mecatrónica")
print ("Ingenieria Industrial")
print ("Ingenieria en Gestión Empresarial")
print ("Ingenieria en Logistica")
print ("Maestría en Ingenieria Mecatrónica")
print("Para empezar tienes que registrarte.")

while True:
    print("\n📋 LISTA DE ALUMNOS📋")
    print("1. Registrar alumno")
    print("2. Dar de baja a alumno")
    print("3. Ver lista de alumnos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    # Registrar alumno
    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        carrera = input ("Ingrese la carrera de su preferencia:")
        edad = input("Ingrese su edad: ")
        calificacion = input("Ingrese su calificación: ")


        # Agregar alumno a la lista
        alumnos.append({"nombre": nombre, "carrera": carrera, "edad": edad, "calificación": calificacion})
        print(f"✅ Alumno {nombre} registrado correctamente.")

    elif opcion == "2": 
        if not alumnos:  
            print("❌ No hay alumnos registrados, no puedes dar de baja a ninguno.")  
        else:  
            try:
                num = int(input("Número de alumno a eliminar: ")) - 1
                if 0 <= num < len(alumnos):
                    eliminado = alumnos.pop(num)
                    print(f"✅ Alumno '{eliminado['nombre']}' dado de baja.")
                else:
                    print("❌ Número no registrado.")
            except ValueError:
                print("❌ Ingresa un número válido.")

    elif opcion == "3":
        if not alumnos:
            print("📭 No hay alumnos registrados.")
        else:
            print("\n📌 Lista de Alumnos:")
            for i, alumno in enumerate(alumnos, 1):
                print(f"{i}. {alumno['nombre']} - Carrera: {alumno['carrera']} - Edad: {alumno['edad']} - Calificación: {alumno['calificación']}")

    elif opcion == "4":
        print("La actualización de listas se ha realizado correctamente. ¡Hasta luego!")
        time.sleep(1)  # Pausa de 1 segundo antes de salir
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")
