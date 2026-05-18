from tad.listas.nodos import NodoListaSimplementeEnlazada


class ListaCircularSimplementeEnlazada:
    def __init__(self):
        self.__final = None
        self.__contador = 0

    def es_vacia(self):
        return self.__contador == 0

    def agregar(self, nuevo_dato):
        nuevo_nodo = NodoListaSimplementeEnlazada(nuevo_dato)
        if self.es_vacia():
            nuevo_nodo.sig = nuevo_nodo
            self.__final = nuevo_nodo
            self.__contador += 1
            return True
        if not isinstance(nuevo_dato, type(self.__final.dato)):
            return False
        nuevo_nodo.sig = self.__final.sig
        self.__final.sig = nuevo_nodo
        self.__final = nuevo_nodo
        self.__contador += 1
        return True

    def insertar(self, nuevo_dato, pos=0):
        if not isinstance(pos, int) or pos < 0:
            return False
        if not self.es_vacia():
            if not isinstance(nuevo_dato, type(self.__final.dato)):
                return False
        if pos == self.__contador:
            return self.agregar(nuevo_dato)
        if pos > self.__contador:
            pos = pos % self.__contador
        nuevo_nodo = NodoListaSimplementeEnlazada(nuevo_dato)
        if pos == 0:
            if self.es_vacia():
                nuevo_nodo.sig = nuevo_nodo
                self.__final = nuevo_nodo
                self.__contador += 1
                return True
            nuevo_nodo.sig = self.__final.sig
            self.__final.sig = nuevo_nodo
            self.__contador += 1
            return True
        nodo_aux = self.__final.sig
        cont = 1
        while cont < pos:
            nodo_aux = nodo_aux.sig
            cont += 1
        nuevo_nodo.sig = nodo_aux.sig
        nodo_aux.sig = nuevo_nodo
        self.__contador += 1
        return True

    def suprimir(self, item, por_dato=True):
        if por_dato:
            return self.__suprimir_por_dato(item)
        return self.__suprimir_por_posicion(item)

    def __suprimir_por_dato(self, dato):
        if self.es_vacia():
            return False
        if not isinstance(dato, type(self.__final.dato)):
            return False
        nodo_aux = self.__final.sig
        if nodo_aux.dato == dato:
            if self.__contador > 1:
                self.__final.sig = self.__final.sig.sig
                self.__contador -= 1
                return True
            if self.__contador == 1:
                self.__final = None
                self.__contador = 0
                return True
            return False
        cont = 1
        while cont < self.__contador:
            if nodo_aux.sig.dato == dato:
                if cont == self.__contador - 1:
                    self.__final = nodo_aux
                nodo_aux.sig = nodo_aux.sig.sig
                self.__contador -= 1
                return True
            cont += 1
            nodo_aux = nodo_aux.sig
        return False

    def __suprimir_por_posicion(self, pos):
        if not isinstance(pos, int) or pos < 0 or self.es_vacia():
            return False
        pos = pos % self.__contador
        if pos == 0:
            if self.__contador > 1:
                self.__final.sig = self.__final.sig.sig
                self.__contador -= 1
                return True
            else:
                self.__final = None
                self.__contador = 0
            return True
        nodo_aux = self.__final.sig
        cont = 1
        while cont < pos:
            nodo_aux = nodo_aux.sig
            cont += 1
        if cont == self.__contador - 1:
            nodo_aux.sig = self.__final.sig
            self.__final = nodo_aux
            self.__contador -= 1
            return True
        elif cont < self.__contador:
            nodo_aux.sig = nodo_aux.sig.sig
            self.__contador -= 1
            return True
        return False

    def buscar(self, item, por_dato=True):
        if por_dato:
            return self.buscar_por_dato(item)
        return self.buscar_por_posicion(item)

    def buscar_por_posicion(self, pos_rel):
        if not isinstance(pos_rel, int) or self.es_vacia():
            return None
        if pos_rel < 0:
            return None
        pos_rel = pos_rel % self.__contador
        nodo_actual = self.__final.sig
        contador = 0
        while contador < pos_rel:
            contador += 1
            nodo_actual = nodo_actual.sig
        return nodo_actual.dato

    def buscar_por_dato(self, dato_buscar):
        if self.es_vacia():
            return None
        if not isinstance(dato_buscar, type(self.__final.dato)):
            return None
        cont = 0
        nodo_aux = self.__final.sig
        while cont < self.__contador:
            if nodo_aux.dato == dato_buscar:
                return nodo_aux.dato
            nodo_aux = nodo_aux.sig
            cont += 1
        return None

    def buscar_cuantos(self, dato_buscar):
        if self.es_vacia():
            return 0
        if not isinstance(dato_buscar, type(self.__final.dato)):
            return 0
        cont = 0
        cont2 = 0
        nodo_aux = self.__final.sig
        while cont < self.__contador:
            cont += 1
            if nodo_aux.dato == dato_buscar:
                cont2 += 1
            nodo_aux = nodo_aux.sig
        return cont2

    def suerte(self, pos_rel):
        return self.buscar(pos_rel, False)

    def __str__(self):
        if self.es_vacia():
            return "⭕ --> ⭕"
        cadena = "⭕"
        nodo_aux = self.__final.sig
        cont = 0
        while cont < self.__contador:
            cont += 1
            cadena += f" --> [{nodo_aux}]"
            nodo_aux = nodo_aux.sig
        cadena += " --> ⭕"
        return cadena

    def __len__(self):
        return self.__contador

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= self.__contador:
            raise StopIteration
        dato_actual = self.buscar(self.__index, False)
        self.__index += 1
        return dato_actual
