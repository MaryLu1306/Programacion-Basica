Algoritmo SistemaRiegoMenu
	Definir opcion Como Entero
    Definir humedad, parametro Como Real
    Definir riego_activo Como Logico
    
    parametro <- 40  // Par�metro ajustable de humedad
    riego_activo <- Falso
    
    Repetir
        // Men� principal
        Escribir "----- SISTEMA DE RIEGO AUTOM�TICO -----"
        Escribir "1. Medir humedad actual"
        Escribir "2. Activar modo autom�tico"
        Escribir "3. Salir"
        Escribir "Seleccione una opci�n:"
        Leer opcion
        
        Segun opcion Hacer
            1:  // Medir humedad manual
                humedad <- Aleatorio(10, 100)  // Simula sensor
                Escribir "-> Humedad medida: ", humedad, "%"
                Si humedad < parametro Entonces
                    Escribir "�Humedad baja! Activando riego..."
                    riego_activo <- Verdadero
                Sino
                    Escribir "Humedad adecuada. Riego inactivo."
                    riego_activo <- Falso
                FinSi
                
            2:  // Modo autom�tico (como el programa anterior)
                Escribir "Modo autom�tico activado. Ctrl+C para salir."
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
                    Esperar 2  // Espera 2 segundos (simulaci�n)
                FinMientras
                
            3:  // Salir
                Escribir "Apagando sistema..."
                
            De Otro Modo:
                Escribir "Opci�n no v�lida. Intente de nuevo."
        FinSegun
    Hasta Que opcion = 3
FinAlgoritmo
