class NodoListaSimplementeEnlazada:
    """Clase que corresponde a un nodo de una lista simplemente enlazada.
    """
    def __init__(self, dato):
        """Método constructor que incorpora un dato dentro de un nodo de
        lista simplemente enlazada. El valor del enlace siguiente es
        igual a None

        Parameters
        ----------
        dato : object
             Corresponde al valor que se va a guardar al interior del nodo.
        """
        self.dato = dato
        self.sig = None

    def __str__(self):
        return f'{self.dato}'

    def __repr__(self):
        return f'{self.dato}'
