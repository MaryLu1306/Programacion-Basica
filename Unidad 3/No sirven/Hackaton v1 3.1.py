# Lista vacía para almacenar los productos
productos = []

while True:
    print("\n📋 LISTA DE COMPRAS📋")
    print("1. ¿Cuántos productos deseas comprar?")
    print("2. Agregar productos")
    print("3. Ver productos")
    print("4. Eliminar productos")
    print("5. Salir")

    opcion = input("¿Qué deseas hacer? ")

    if opcion == "1":
        producto = input("📝 Escribe la cantidad de productos:")
        cantidad de productos > 0 < 5
        print(f"✅ Puedes proceder con la elaboración de la lista.")
        else:
        print("❌ Opción inválida. Elige un numero del 1 al 5.")

    elif opcion == "2":
         producto = input("📝 Escribe el producto a agregar: ")
        producto.append(producto)
        print(f"✅ Producto '{producto}' agregada.")

    elif opcion == "3":
        if not productos:
            print("📭 No hay productos en la lista.")
        else:
            print("\n📌 Lista de Productos:")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")
     
    elif opcion == "4":
        if not productos:
            print("📭 No hay productos para eliminar.")
        else:
            num = int(input("🗑️ Número del producto a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                print(f"🗑️ Producto '{productos[num]}' eliminada.")
                producto.pop(num)
            else:
                print("❌ Número inválido.")

    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")