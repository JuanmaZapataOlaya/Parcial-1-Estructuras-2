class Libro:
    def __init__(self, titulo, autor, fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion

def quicksort_libros(libros):
    if len(libros) <= 1:
        return libros
    pivot = libros[len(libros) // 2].titulo
    menores, iguales, mayores = [], [], []
    for libro in libros:
        if libro.titulo < pivot:
            menores.append(libro)
        elif libro.titulo == pivot:
            iguales.append(libro)
        else:
            mayores.append(libro)
    return quicksort_libros(menores) + iguales + quicksort_libros(mayores)

def busqueda_binaria(libros, titulo):
    izquierda, derecha = 0, len(libros) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if libros[medio].titulo == titulo.lower():
            return medio
        elif libros[medio].titulo < titulo.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

libros = [
    Libro("python programming", "John Doe", 2019),
    Libro("el teorema del machetazo", "Juan Zapata", 2020),
    Libro("la pregunta por la buena vida", "Alice Johnson", 2018),
    Libro("machine learning", "Bob Brown", 2021),
    Libro("como estudiar calculo facil", "Profe Alex", 2024),
    Libro("compiladores y torturas egipcias", "Andres Sicard", 1995),
    Libro("fisica 1","sears zemansky", 1997),
    Libro("la importancia del no","Ramiro Ortega", 2001)
]

libros_ordenados = quicksort_libros(libros)
for libro in libros_ordenados:
    print(libro.titulo)




titulo_buscado = input("Que libro buscas: ")

indice = busqueda_binaria(libros_ordenados, titulo_buscado)
if indice != -1:
    print(f"El libro '{titulo_buscado}' fue encontrado en la posición {indice}.")
else:
    print(f"El libro '{titulo_buscado}' no fue encontrado.")
