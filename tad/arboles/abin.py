from tad.arboles.nodos import NodoArbolBinario
from random import random


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __agregar(self, sub_arbol, clave):
        if not sub_arbol:
            sub_arbol = NodoArbolBinario(clave)
        elif random() <= 0.5:
            sub_arbol.izq = self.__agregar(sub_arbol.izq, clave)
        else:
            sub_arbol.der = self.__agregar(sub_arbol.der, clave)
        return sub_arbol

    def es_vacio(self):
        return bool(self.raiz)

    def __str__(self):
        return self.__str_recursivo(self.raiz, "", True)

    def __str_recursivo(self, nodo, prefijo, es_ultimo):
        if not nodo:
            return ""

        resultado = prefijo + ("└── " if es_ultimo else "├── ") + str(nodo.clave) + "\n"

        hijos = []
        if nodo.izq:
            hijos.append((nodo.izq, False))
        if nodo.der:
            hijos.append((nodo.der, True))

        for i, (hijo, es_ultimo_hijo) in enumerate(hijos):
            nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
            resultado += self.__str_recursivo(hijo, nuevo_prefijo, i == len(hijos) - 1)

        return resultado

    def buscar(self, clave_buscar):
        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_arbol, c_b):
        if sub_arbol:
            if sub_arbol.clave == c_b:
                return sub_arbol.clave
            izq = self.__buscar(sub_arbol.izq, c_b)
            if izq is not None:
                return izq
            der = self.__buscar(sub_arbol.der, c_b)
            if der is not None:
                return der
        return None

    def __len__(self):
        return self.__cantidad_nodos(self.raiz)

    def __cantidad_nodos(self, sub_arbol):
        if sub_arbol:
            return 1 + self.__cantidad_nodos(sub_arbol.izq) + self.__cantidad_nodos(sub_arbol.der)
        return 0

    def hojas(self):
        return self.__contar_hojas(self.raiz)

    def __contar_hojas(self, sub_arbol):
        if sub_arbol is None:
            return 0
        if sub_arbol.izq or sub_arbol.der:
            return self.__contar_hojas(sub_arbol.izq) + self.__contar_hojas(sub_arbol.der)
        return 1

    def internos(self):
        return self.__internos(self.raiz)

    def __internos(self, sub_arbol):
        if sub_arbol is None or (sub_arbol.izq is None and sub_arbol.der is None):
            return 0
        return 1 + self.__internos(sub_arbol.izq) + self.__internos(sub_arbol.der)

    def altura(self):
        return self.__altura(self.raiz)

    def __altura(self, sub_arbol):
        if sub_arbol is None:
            return 0
        altura_izq = 1 + self.__altura(sub_arbol.izq)
        altura_der = 1 + self.__altura(sub_arbol.der)
        return altura_izq if altura_izq > altura_der else altura_der
