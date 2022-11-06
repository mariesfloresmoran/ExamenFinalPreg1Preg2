"""
Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). Considerar que un libro puede tener varios autores.
Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.
Dicho programa debe tener un menu (a interactuar en la línea de comando) para:
    Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
    Opción 2: Listar libros. - 
    Opción 3: Agregar libro. - 
    Opción 4: Eliminar libro. - 
    Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado. - 
    Opción 6: Ordenar libros por título. - 
    Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados. - 
    Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores. - 
    Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores). - 
    Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)
"""
# BASE
libros = []

class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor #debe ser una lista de str

    def mostrar_datos(self):
        return f"{self.id} Libro: {self.titulo} - Género: {self.genero} - ISNB: {self.ISBN} - Editorial: {self.editorial} - Autor(es): {self.autor}"
    
    def editarLibros(self, titulo, genero, ISBN, editorial, autor):
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor
        print("Modificación Existosa")

def lista_libros_prueba():
    libro1 = Libro(1, "Divina Comedia","Tragedia","jjjj","Pacasmayo","Jonathan,Stephanie".split(","))
    libro2 = Libro(5, "Comedia","Tragedia","jhjh","Luz","Jonatha".split(","))
    libro3 = Libro(9, "ZZZ","Ficción","hkhk","Luz","Jonatha".split(","))
    libro4 = Libro(16, "AAA","Comedia","hkhk","Pacasmayo","Jonatha,Stephanie".split(","))
    libros.append(libro1)
    libros.append(libro2)
    libros.append(libro3)
    libros.append(libro4)
    print(libros)

def mostrar_libros():
    for libro in libros:
        print(libro.mostrar_datos())

# Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.

# Opción 2: Listar libros.
"""Terminado"""
def listadoLibros():  
    print("El nuevo listado es: \n")
    if libros:
        for objLibro in libros:
            print(objLibro.mostrar_datos())
    else:
        print("La lista se encuentra vacía.")

# Opción 3: Agregar libro.

# Opción 4: Eliminar libro.

# Opción 5: Buscar libro por ISBN o por título.

# Opción 6: Ordenar libros por título.

# Opción 7: Buscar libros por autor, editorial o género. 

# Opción 8: Buscar libros por número de autores.

# Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).

# Opción 10: Guardar libros en archivo de disco duro (.txt o csv).

#MENU PRINCIPAL