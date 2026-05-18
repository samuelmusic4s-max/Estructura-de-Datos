from typing import Any

from tad.arboles.abinbus import ArbolBinarioBusqueda

class Libro:
    def __init__(self, titulo, isbn, autores="", numero_paginas=0) -> None:
        self.titulo = titulo
        self.isbn = isbn
        self.autores = autores
        self.numero_paginas = numero_paginas

    def __setattr__(self, name: str, value: str) -> None:
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

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Libro):
            return False
        return self.titulo == otro.titulo and self.isbn == otro.isbn

    def __lt__(self, otro: object) -> bool:
        if not isinstance(otro, Libro):
            raise TypeError(f"No se puede comparar un objeto de la clase libro con un objeto de tipo {type(otro)}")
        return ((self.titulo < otro.titulo) or
                self.isbn < otro.isbn if self.titulo == otro.titulo else False)

    def __str__(self) -> str:
        return "{�" + f":{self.titulo}:{self.isbn}:{self.numero_paginas} pags" + "}"
