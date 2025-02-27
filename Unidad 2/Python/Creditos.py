creditos = int(input("Ingrese sus creditos: "))
if creditos <=79:
    print("faltan creditos para hacer el servicio social")

if creditos >= 80 and creditos <= 119: 
    print("puedes hacer el servicio social")

if creditos >= 81 and creditos <= 119:
    print("faltan creditos para hacer las recidencias")

if creditos >= 120:
    print("puedes hacer las residencias")
