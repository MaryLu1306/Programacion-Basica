Algoritmo SistemaRiegoMenu
	Definir opcion Como Entero
    Definir humedad, parametro Como Real
    Definir riego_activo Como Logico
    
    parametro <- 40  // Parámetro ajustable de humedad
    riego_activo <- Falso
    
    Repetir
        // Menú principal
        Escribir "----- SISTEMA DE RIEGO AUTOMÁTICO -----"
        Escribir "1. Medir humedad actual"
        Escribir "2. Activar modo automático"
        Escribir "3. Salir"
        Escribir "Seleccione una opción:"
        Leer opcion
        
        Segun opcion Hacer
            1:  // Medir humedad manual
                humedad <- Aleatorio(10, 100)  // Simula sensor
                Escribir "-> Humedad medida: ", humedad, "%"
                Si humedad < parametro Entonces
                    Escribir "¡Humedad baja! Activando riego..."
                    riego_activo <- Verdadero
                Sino
                    Escribir "Humedad adecuada. Riego inactivo."
                    riego_activo <- Falso
                FinSi
                
            2:  // Modo automático (como el programa anterior)
                Escribir "Modo automático activado. Ctrl+C para salir."
                Mientras Verdadero Hacer
                    humedad <- Aleatorio(10, 100)
                    Escribir "Humedad actual: ", humedad, "%"
                    Si humedad < parametro Entonces
                        Escribir "[RIEGO ACTIVADO]"
                        riego_activo <- Verdadero
                    Sino
                        Escribir "[RIEGO INACTIVO]"
                        riego_activo <- Falso
                    FinSi
                    Esperar 2  // Espera 2 segundos (simulación)
                FinMientras
                
            3:  // Salir
                Escribir "Apagando sistema..."
                
            De Otro Modo:
                Escribir "Opción no válida. Intente de nuevo."
        FinSegun
    Hasta Que opcion = 3
FinAlgoritmo
