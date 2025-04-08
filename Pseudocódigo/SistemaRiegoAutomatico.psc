Algoritmo SistemaRiegoAutomatico
	// Definici�n de variables
	Definir humedad_suelo, parametro_humedad Como Real
	Definir llave_abierta Como L�gico
	// Par�metro de humedad 
	parametro_humedad <- 20
	// Inicio del programa
	Escribir 'Sistema de Riego Autom�tico - Iniciado'
	// Bucle principal del sistema
	Repetir
		Escribir 'Ingrese el valor de humedad actual (%): '
		// Leer humedad del sensor
		Leer humedad_suelo
		// Comparar humedad con par�metro
		Si humedad_suelo<parametro_humedad Entonces
			// Accionar sistema de riego
			llave_abierta <- Verdadero
			Escribir 'Humedad baja (', humedad_suelo, '%). Activando riego...'
		SiNo
			// Mantener sistema apagado
			llave_abierta <- Falso
			Escribir 'Humedad adecuada (', humedad_suelo, '%). Riego no necesario.'
		FinSi
		// Esperar antes de la pr�xima lectura
		Escribir 'Esperando 1 hora para pr�xima medici�n...'
	Hasta Que Falso
FinAlgoritmo // Bucle infinito (en sistema real)
