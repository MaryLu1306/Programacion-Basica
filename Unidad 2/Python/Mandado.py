# Lista vacía para almacenar los productos
lista_compras = []

#Preguntar al usuario si desea realizar su mandado
= input("¿Deseas hacer tu mandado? (si/no):"). lower()

#Verificar respuesta
 if opcion == si:
    print("¿Cuantos productos deseas comprar?")
 else:
    print("Cerrando programa")

#Verificar respuesta
 if opcion > 0:
    print("Agrega los productos")

# Agregar productos
producto1 = input("Agrega el primer producto: ")
lista_compras.append(producto1)

producto2 = input("Agrega el segundo producto: ")
lista_compras.append(producto2)

producto3 = input("Agrega el tercer producto: ")
lista_compras.append(producto3)

# Mostrar la lista completa
print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")

print("\n✅ ¡Lista creada con éxito!")