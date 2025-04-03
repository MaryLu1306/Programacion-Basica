# Herencia
# Clase base o padre
class Libro:
    def __init__(self, titulo, paginas, editorial, autor, genero):
        self.titulo = titulo
        self.paginas = paginas
        self.editorial = editorial
        self.autor = autor
        self.genero = genero

    def presentar(self):
        return f"Este libro se llama {self.titulo}, tiene {self.paginas} páginas, es de la editorial {self.editorial} y lo escribio {self.autor}, ¡Es un  libro de {self.genero}!."

# Clase derivada o hija
class Titulo(Libro):
    def __init__(self, titulo, paginas, editorial, autor, genero, tema):
        super().__init__(titulo, paginas, editorial, autor, genero)  # Llamada al constructor de la clase padre
        self.tema = tema

    def presentar(self):
        # Sobrescribimos el método de la clase padre
        return f"Este libro se llama {self.titulo}, tiene {self.paginas} páginas, es de la editorial {self.editorial} y lo escribio {self.autor}, ¡Es un  libro de {self.genero}!, Busca principalmente {self.tema}."

# Otra clase derivada
class Titulo2(Libro):
    def __init__(self, titulo, paginas, editorial, autor, genero, tema):
        super().__init__(titulo, paginas, editorial, autor, genero) 
        self.tema = tema

    def presentar(self):
        return f"Este libro se llama {self.titulo}, tiene {self.paginas} páginas, es de la editorial {self.editorial} y lo escribio {self.autor}, ¡Es un  libro de {self.genero}!, Busca principalmente {self.tema}."

# Programa principal
if __name__ == "__main__":
    libro = Libro("Cien años de soledad", 450, "Sudamericana" , "Gabriel Garcia Marquez", "realismo magico" )
    titulo = Titulo("La vuelta al mundo en 80 dias", 300, "Garnier Hermanos", "Julio Verne","aventura", "entretener")
    titulo2 = Titulo2("El mundo de sofia", 600, "Forlaget H Aschehoug & Co", "Jostein Gaarder", "ficcion filosofica", "enseñar")

    print(libro.presentar())
    print(titulo.presentar())
    print(titulo2.presentar())