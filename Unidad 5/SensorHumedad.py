import time

def sensor_humedad():
    limite = 400  

    while True:
        try:
            humedad = int(input("Ingresa el valor del sensor (0 a 1023): "))

            if humedad < 0 or humedad > 1023:
                print("⚠️  Valor fuera de rango. Debe ser entre 0 y 1023.")
                continue

            if humedad > limite:
                print("🌵 Suelo seco. Regar la planta.")
            else:
                print("💧 Suelo húmedo. No regar.")
            
            time.sleep(2)

        except ValueError:
            print("❌ Por favor, ingresa un número entero válido.")

sensor_humedad()