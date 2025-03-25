from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv
import time

archivo = "alumnos.csv"

# Lista vacia de alumnos
alumnos = leer_diccionarios_de_csv(archivo)

print("¡Te damos la bienvenida al Instituto Tecnológico de Pabellón de Arteaga!")
print("Contamos con formacion en:")
print("Ingenieria Mecatrónica")
print("Ingenieria Industrial")
print("Ingenieria en Gestión Empresarial")
print("Ingenieria en Logistica")
print("Maestría en Ingenieria Mecatrónica")
print("Para empezar tienes que registrarte.")

while True:
    print("\n📋 LISTA DE ALUMNOS📋")
    print("1. Registrar alumno")
    print("2. Dar de baja a alumno")
    print("3. Ver lista de alumnos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        carrera = input("Ingrese la carrera de su preferencia: ")
        edad = input("Ingrese su edad: ")
        calificacion = input("Ingrese su calificación: ")

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
        time.sleep(1)  
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")

guardar_diccionarios_en_csv(archivo, alumnos)

datos_leidos = leer_diccionarios_de_csv(archivo)
print("Datos leídos del archivo CSV:")
print(datos_leidos)