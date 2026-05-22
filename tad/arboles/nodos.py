class NodoArbolBinario:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

    def __str__(self):
        return f"{self.clave}"

    def tiene_hijos(self):
        return bool(self.izq or self.der)

    def __repr__(self):
        return self.__str__()
