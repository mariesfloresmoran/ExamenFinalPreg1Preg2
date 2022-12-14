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

def mostrar_libros():
    for libro in libros:
        print(libro.mostrar_datos())

# Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.

import pandas as pd

url = "https://raw.githubusercontent.com/mariesfloresmoran/ExamenFinalPreg1Preg2/main/Libros.csv"
disco_duro = pd.read_csv(url, header = 0 )

def Listado_disco_duro(): 
    print(disco_duro)

#print(disco_duro)

# Opción 2: Listar libros

def listadoLibros():  
    print("El nuevo listado es: \n")
    if libros:
        for objLibro in libros:
            print(objLibro.mostrar_datos())
    else:
        print("La lista se encuentra vacía.")

# Opción 3: Agregar libro

def registrarnuevolibro():
    print("Registro de Nuevo Libro: \n")
    id= int(input("Ingrese el numero de ID del Libro: "))
    titulo= input("Ingrese el Título del Libro: ")
    genero= input("Ingrese el Género del Libro: ")
    ISBN= input("Ingrese el numero de ISBN del Libro: ")
    editorial= input("Ingrese la Editorial del Libro: ")
    autor = input("Ingrese la lista de autores separada por comas: ")
    objLibro = Libro(id,titulo,genero,ISBN,editorial,autor.split(","))
    libros.append(objLibro)
    
    df_dictionary = pd.DataFrame([libros])
    print('df_dictionary: ', df_dictionary)
    out = pd.concat([disco_duro, df_dictionary], ignore_index=True)
    print(out)

    df = pd.DataFrame()

# Opción 4: Eliminar libro

def eliminarlibro():
    libro_a_eliminar = input("Ingrese el nombre del libro que desea eliminar: ")

    libro = next((i for i in libros if i.titulo == libro_a_eliminar), None)

    #comprobación:
    if libro:
        print("Libro encontrado: ", libro.titulo)
        print("Borrando ...")
        libros.remove(libro)

    print("La nueva lista de Libros es: ")
    for l in libros:
        print(l)

# Opción 5: Buscar libro por ISBN o por título

def menu_busqueda_isbn_titulo():
    global libros
    def buscar_por_isbn():
        isbn = input ("Ingrese la ISBN: ")
        resultado_busqueda_isbn = [i for i in libros if isbn.lower() in i.ISBN.lower()]
        if resultado_busqueda_isbn:
            print("Libros encontrados:")
            for libro in resultado_busqueda_isbn:
                print(libro.mostrar_datos())
                break
        else:
            print ("No se encontraron coincidencias, intente con otra búsqueda.")

    def buscar_por_titulo():
        titulo = input ("Ingrese el Título: ")
        resultado_busqueda_titulo = [i for i in libros if titulo.lower() in i.titulo.lower()]
        if resultado_busqueda_titulo:
            print("Libros encontrados:")
            for libro in resultado_busqueda_titulo:
                print(libro.mostrar_datos())
        else:
            print ("No se encontraron coincidencias, intente con otra búsqueda.")

    while True:
        print("Elija la opción por la cual desee buscar:")
        print("1. Buscar por ISBN")
        print("2. Buscar por Título")
        print("3. Para salir")
        
        opcion = int(input("Ocpción: "))
        if opcion == 1:
            buscar_por_isbn()
        elif opcion == 2:
            buscar_por_titulo()
        elif opcion == 3:
            break

# Opción 6: Ordenar libros por título

def ordenar_libro_por_titulo():
    print("La lista sin ordenar era: ")
    mostrar_libros()
    libros.sort(key=lambda libro: libro.titulo)
    print("La nueva lista ordenada es: ")
    mostrar_libros()

# Opción 7: Buscar libros por autor, editorial o género

def menu_busqueda_autor_editorial_genero():
    def buscar_por_autor():
        autor = input ("Ingrese el Autor: ")
        resultado_busqueda_autor = [i for i in libros if autor.lower() in [j.lower() for j in i.autor]]
        if resultado_busqueda_autor:
            print("Libros encontrados:")
            for libro in resultado_busqueda_autor:
                print(libro.mostrar_datos())
        else:
            print ("No se encontraron coincidencias, intente con otra búsqueda.")
    
    def buscar_por_editorial():
        editorial = input ("Ingrese la Editorial: ")
        resultado_busqueda_editorial = [i for i in libros if editorial.lower() in i.editorial.lower()]
        if resultado_busqueda_editorial:
            print("Libros encontrados:")
            for libro in resultado_busqueda_editorial:
                print(libro.mostrar_datos())
        else:
            print ("No se encontraron coincidencias, intente con otra búsqueda.")

    def buscar_por_genero():
        genero = input ("Ingrese el Género: ")
        resultado_busqueda_genero = [i for i in libros if genero.lower() in i.genero.lower()]
        if resultado_busqueda_genero:
            print("Libros encontrados:")
            for libro in resultado_busqueda_genero:
                print(libro.mostrar_datos())
        else:
            print ("No se encontraron coincidencias, intente con otra búsqueda.")
    
    global libros
    while True:
        print("Elija la opción por la cual desee buscar:")
        print("1. Buscar por autor")
        print("2. Buscar por editorial")
        print("3. Buscar libros por género")
        print("4. Para salir")

        opcion = int(input("Ocpción: "))
        if opcion == 1:
            buscar_por_autor()
        elif opcion == 2:
            buscar_por_editorial()
        elif opcion == 3:
            buscar_por_genero()
        elif opcion == 4:
            break

# Opción 8: Buscar libros por número de autores

def menu_busqueda_cant_autores():
    global libros
    qautor = int(input ("Ingrese la cantidad de autores por la cual desea buscar: "))
    resultado_busqueda_qautor = [i for i in libros if len(i.autor) == qautor]
    if resultado_busqueda_qautor:
        print("Libros encontrados:")
        for libro in resultado_busqueda_qautor:
            print(libro.mostrar_datos())
    else:
        print ("No se encontraron coincidencias, intente con otra búsqueda.")


# Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores)

def editaractualizarlibro():
    print("Modificación de Datos\n")
    id=input("Ingrese el ID del libro a modificar: ")
    for objLibro in libros:
        if id == objLibro.id:
            titulo = input("Ingrese el título: ")
            genero = input("Ingrese el genero: ")
            ISBN = input("Ingrese el ISBN: ")
            editorial = input("Ingrese la Editorial: ")
            autor = input("Ingrese los autores separados por comas: ")
            objLibro.editarLibros(titulo, genero, ISBN, editorial, autor)
            objLibro.mostrar_datos()

# Opción 10: Guardar libros en archivo de disco duro (.txt o csv)
def Guardar_libros_en_disco_duro():
    disco_duro.extend(objLibro)
    print(disco_duro)
    disco_duro.to_csv(index=False)

#MENU PRINCIPAL
def mainmenu():
    while True:
        print("\n")
        print("            Bienvenidos            ")
        print("               Menú                ")
        print("\n")
        print("Seleccione una de las siguientes opciones: ");
        print("1. Leer archivo de disco duro")
        print("2. Listar libros")
        print("3. Agregar libro")
        print("4. Eliminar libro")
        print("5. Buscar libro por ISBN o Título")
        print("6. Ordenar libros por título")
        print("7. Buscar libro por autor, editorial o género")
        print("8. Buscar libros por número de autores")
        print("9. Editar o actualizar datos de un libro")
        print("10.Guardar datos en archivo de disco duro")

        opcion = int(input("Ocpción: "))
        if opcion == 1:
            Listado_disco_duro()
        elif opcion == 2:
            listadoLibros()
        elif opcion == 3:
            registrarnuevolibro()  
        elif opcion == 4:
            eliminarlibro() 
        elif opcion == 5:
            menu_busqueda_isbn_titulo()
        elif opcion == 6:
            ordenar_libro_por_titulo()
        elif opcion == 7:
            menu_busqueda_autor_editorial_genero()
        elif opcion == 8:
            menu_busqueda_cant_autores()  
        elif opcion == 9:
            editaractualizarlibro()
        elif opcion == 10:
            Guardar_libros_en_disco_duro()
mainmenu() 
