# Lista de nombres
Nombres = ["Aaron" , "Saba" , "Alexa" , "Manuel" , "Victor", "Cristian" , "Arturo" , "Roberto" , "Oswaldo" , "Emrique "]

#Lista de edades
Edades = [19, 18, 18, 18, 18, 18, 18, 18, 18, 18]

#Lista de materias
Materias = ["Algebra lineal" , "Estadistica y control de calidad" , "Calculo integral" , "Programación básica", "Ingenieria de los materiales" , "Administracion y contabilidad" , "Ingles"]

#Lista de profesores 
Profesores = ["Eduardo" , "Enrique" , "Marlem" , "Guillermo" , "Adylen" , "Laura" , ""]

#Lista de frutas 
Frutas = ["manzana" , "piña" , "pera" , "melon" , "sandia" , "naranja" , "mandarina" , "guayaba" , "fresas" , "platano"] 

print(Nombres)
print(Edades)
print(Materias)
print(Profesores)
print(Frutas)
print(len(Nombres))
print(max(Edades))
print(min(Edades))
Materias.remove("Programación básica")
print (Materias)
Materias.append("Programación avanzada")
print (Materias)
print(len(Materias))
Materias.remove ("Estadistica y control de calidad")
Materias.insert (1, "Programacion basica")
print(Materias)
for Materia in Materias:
    print(Materia)
print(len(Materias))
