from tad.arboles.recorridos import pre_orden_str, in_orden_str, post_orden_str
from tad.arboles.abinbus import ArbolBinarioBusqueda

class Libro:
    def __init__(self, titulo, isbn, autores="", numero_paginas=0):
        self.titulo = titulo
        self.isbn = isbn
        self.autores = autores
        self.numero_paginas = numero_paginas

    def __setattr__(self, name: str, value: str):
        cadena = ""
        if name == 'titulo' and len(value) < 3:
            cadena = "El título del libro debe al menos ser de 3 caracteres"
        if name == 'isbn':
            if not value.isdigit():
                cadena = "El codigo ISBN debe estar conformado unicamente por digitos."
            elif len(value) < 10:
                cadena = "El codigo ISBN debe al menos tener 10 caracteres."
            elif len(value) > 13:
                cadena ="El codigo ISBN no puede tener mas de 13 caracteres."
        if cadena:
            raise ValueError(cadena)
        return super().__setattr__(name, value)

    def __eq__(self, otro: object):
        if not isinstance(otro, Libro):
            return False
        return self.titulo == otro.titulo and self.isbn == otro.isbn

    def __lt__(self, otro: object):
        if not isinstance(otro, Libro):
            raise TypeError(f"No se puede comparar un objeto de la clase libro con un objeto de tipo {type(otro)}")
        return ((self.titulo < otro.titulo) or
                self.isbn < otro.isbn if self.titulo == otro.titulo else False)

    def __str__(self) -> str:
        return "{�" + f":{self.titulo}:{self.isbn}:{self.numero_paginas} pags" + "}"

    def __repr__(self) -> str:
        return self.__str__()

class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.bodega_libros = ArbolBinarioBusqueda()

    def agregar_libro(self, titulo, isbn, autores="", numero_paginas=0):
        try:
            libro = Libro(titulo, isbn, autores, numero_paginas)
            self.bodega_libros.agregar(libro)
            return True
        except Exception as e:
            print("Error al intentar agregar libro ", e)

    def buscar_libro(self, titulo, isbn):
        try:
            libro = Libro(titulo, isbn)
            return self.bodega_libros.buscar(libro)
        except Exception as e:
            print("Error durante la ejecución ", e)

    def eliminar_libro(self, titulo, isbn, mayor=True):
        try:
            libro = Libro(titulo, isbn)
            self.bodega_libros.suprimir(libro, not mayor)
        except Exception as e:
            print("Error inesperado ", e)

    def mostrar_cuadro(self):
        linea_uno = "+" + "-" * 68 + "+"
        linea_dos = "-" * 70
        return f"""
        {linea_uno}
        | {"Biblioteca":<12} | {self.nombre:<50}|
        {linea_dos}
        | {"Dirección:":<12} | {self.direccion:<50}|
        {linea_dos}
        | {"Teléfono:":<12} | {self.telefono:<50}|
        {linea_uno}
        | {"No. Libros Hoja":^17} | {"No. Libros Internos":^20} | {"Altura":^6} | {"Total de libros":^15}|
        {linea_dos}
        | {str(self.bodega_libros.hojas()):>17} | {str(self.bodega_libros.internos()):>20} | {str(self.bodega_libros.altura()):>6} | {str(len(self.bodega_libros)):>15}|
        {linea_uno}
        | {"Mínimo Libro:":^17} | {str(self.bodega_libros.minimo()):<50}|
        {linea_dos}
        | {"Máximo Libro:":^17} | {str(self.bodega_libros.maximo()):<50}|
        {linea_uno}
        """

    def mostrar_libros(self, recorrido="pre_orden"):
        match recorrido.lower():
            case "pre_orden":
                print(f"{pre_orden_str(self.bodega_libros)}")
            case "in_orden":
                print(f"{in_orden_str(self.bodega_libros)}")
            case "post_orden":
                print(f"{post_orden_str(self.bodega_libros)}")
            case other:
                print("Opción inválida, elegir una de las siguientes:" \
                "pre_orden, in_orden, post_orden")
