Algoritmo sensor de humedad
		
		Definir humedad Como Entero
		Definir limite Como Entero
		
		limite <- 400  // Si la humedad es mayor, el suelo está seco
		
		Mientras Verdadero Hacer
			
			Escribir "Ingresa el valor del sensor (0 a 1023): "
			Leer humedad
			
			Si humedad > limite Entonces
				Escribir "Suelo seco. Regar la planta."
			Sino
				Escribir "Suelo húmedo. No regar."
			FinSi
			
			Esperar 2 segundos
			
		FinMientras
FinAlgoritmo
