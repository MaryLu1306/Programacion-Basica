# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de cadenas
nombres = ["Ana", "Luis", "Pedro"]

# Lista con diferentes tipos de datos
mixta = [10, "Python", True, 3.14]

# Lista vacía
vacia = []

print(numeros)
print(nombres)
print(mixta)
print(vacia)

input("Presiona Enter para continuar...")

# Parte dos del programa

# Acceder a los elementos de una lista

# Modificar un elemento de la lista
nombres[1] = "Carlos"  

# Agregar elementos a la lista
nombres.append("Lu")
nombres.append("Min") 

# Eliminar elementos de la lista
if "Ana" in nombres:
    nombres.remove("Ana")  


# Recorrer la lista con un bucle for
print("\nLista de nombres actualizada:")
for nombre in nombres:
    print(nombre)

if numeros:  # Verifica que la lista no esté vacía antes de usar max() y min()
    print("Máximo valor en números:", max(numeros))  # Máximo 
    print("Mínimo valor en números:", min(numeros))  # Mínimo 

numeros.sort()  # Ordenar la lista de menor a mayor
print("Lista de números ordenada:", numeros)

numeros.reverse()  # Invertir la lista
print("Lista de números en orden inverso:", numeros)