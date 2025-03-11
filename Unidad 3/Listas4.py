# Lista de nombres
Nombres = ["Aaron" , "Saba" , "Alexa" , "Manuel" , "Victor", "Cristian" , "Arturo" , "Roberto" , "Oswaldo" , "Emrique "]

#Lista de edades
Edades = [19, 18, 18, 18, 18, 18, 18, 18, 18, 18]

#Lista de materias
Materias = ["Algebra lineal" , "Estadistica y control de calidad" , "Calculo integral" , "Programación básica", "Ingenieria de los materiales" , "Dibujo asistido por computadora" , "Administracion y contabilidad" , "Ingles", "calculo diferencial"]

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
Materias.append([1], "Programación basica")
print(Materias)
