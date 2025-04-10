import time

def sistema_riego_menu():
    parametro = 20  
    riego_activo = False
    opcion = 0
    
    while opcion != 3:
        print("----- SISTEMA DE RIEGO AUTOMÁTICO -----")
        print("1. Medir humedad actual")
        print("2. Activar modo automático")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
        time.sleep(2) 

        if opcion == 1:  
            humedad = float(input("Ingrese la humedad actual (%): "))  
            print(f"-> Humedad medida: {humedad}%")
            if humedad < parametro:
                time.sleep(1) 
                print("¡Humedad baja! Activando riego...")
                riego_activo = True
                time.sleep(1)
                 
            else:
                time.sleep(1) 
                print("Humedad adecuada. Riego inactivo.")
                riego_activo = False
                time.sleep(1) 
        
        elif opcion == 2:  
            print("Modo automático activado. Presione Ctrl+C para salir.")
            try:
                while True:
                    humedad = float(input("Ingrese la humedad actual (%): "))  
                    print(f"Humedad actual: {humedad}%")
                    if humedad < parametro:
                        time.sleep(2)
                        print("[RIEGO ACTIVADO]")
                        riego_activo = True
                        

                    else:
                        time.sleep(2)
                        print("[RIEGO INACTIVO]")
                        riego_activo = False
                        

            except KeyboardInterrupt:
                print("\nSaliendo del modo automático.")
            time.sleep(2)
        elif opcion == 3: 
            print("Apagando sistema...")
            time.sleep(4)

        else:
            print("Opción no válida. Intente de nuevo.")
            time.sleep (4)

sistema_riego_menu()
