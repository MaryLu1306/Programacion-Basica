texto = input("Introduce un texto para analizar: ")

contador_vocales = 0
contador_consonantes = 0
contador_numeros = 0
contador_otros = 0

vocales = ['a','A','á','E','e','é','i','I','í','O','o','ó','U','u']

for caracter in texto:
    caracter = caracter.lower()  

    if caracter in vocales:
        contador_vocales += 1
    elif caracter.isalpha():
        contador_consonantes += 1
    elif caracter.isdigit():
        contador_numeros += 1
    
print(f"El texto contiene {contador_vocales} vocales." )
print(f"El texto contiene {contador_consonantes} consonantes")
print(f"El texto contiene {contador_numeros} numeros")