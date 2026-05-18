from tad.arboles.abin import ArbolBinario
from tad.arboles.excepciones import DuplicatedKeyError, HomogeneityError
from tad.arboles.nodos import NodoArbolBinario


class ArbolBinarioBusqueda(ArbolBinario):
    def agregar(self, nueva_clave):
        if self.raiz:
            if not isinstance(nueva_clave, type(self.raiz.clave)):
                raise HomogeneityError(nueva_clave, type(self.raiz.clave))
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __agregar(self, sub_arbol, nueva_clave):
        if not sub_arbol:
            sub_arbol = NodoArbolBinario(nueva_clave)
        elif nueva_clave < sub_arbol.clave: #Dirijo busqueda por la izquierda
            sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave: #Dirijo busqueda por la derecha
            sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
        else: #No puede ser igual a un sub arbol que ya existe
            raise DuplicatedKeyError (nueva_clave)
        return sub_arbol

    def maximo(self):
        if not self.raiz:
            return None
        return self.__maximo(self.raiz)

    def __maximo(self, sub_arbol):
        if sub_arbol.der:
            return self.__maximo(sub_arbol.der)
        return sub_arbol.der

    def minimo(self):
        if not self.raiz:
            return None
        return self.__minimo(self.raiz)

    def __minimo(self, sub_arbol):
        if sub_arbol.izq:
            return self.__minimo(sub_arbol.izq)
        return sub_arbol.izq

    def buscar(self, clave):
        return self.__buscar(self.raiz, clave)

    def __buscar(self, sub_arbol, clave):
        if not sub_arbol:
            return None
        elif clave == sub_arbol.clave:
            return sub_arbol.clave
        elif clave < sub_arbol.clave:
            return self.__buscar(sub_arbol.izq, clave)
        return self.__buscar(sub_arbol.der, clave)

    def __buscar_y_reemplazar_izq(self, sub_arbol):
        if not sub_arbol.izq:
            return sub_arbol.clave, sub_arbol.der
        valor, sub_arbol.izq = self.__buscar_y_reemplazar_izq(sub_arbol.izq)
        return valor, sub_arbol

    def __buscar_y_reemplazar_der(self, sub_arbol):
        if not sub_arbol.der:
            return sub_arbol.clave, sub_arbol.izq
        valor, sub_arbol.der = self.__buscar_y_reemplazar_der(sub_arbol.der)
        return valor, sub_arbol


    def suprimir(self, clave_suprimir, mayor=True):
        exitoso, self.raiz = self.__suprimir(self.raiz, clave_suprimir, mayor)
        return exitoso

    def __suprimir(self, sub_arbol, clave_suprimir, mayor=True):
        if not sub_arbol:
            return False, None
        elif sub_arbol.clave < clave_suprimir:
            exitoso, sub_arbol.der = self.__suprimir(sub_arbol.der, clave_suprimir, mayor)
        elif sub_arbol.clave > clave_suprimir:
            exitoso, sub_arbol.izq = self.__suprimir(sub_arbol.izq, clave_suprimir, mayor)
        elif not (sub_arbol.der or sub_arbol.izq):
            sub_arbol = None
            exitoso = True
        elif not sub_arbol.der:
            sub_arbol = sub_arbol.izq
            exitoso = True
        elif not sub_arbol.izq:
            exitoso = True
            sub_arbol = sub_arbol.der
        elif mayor:
            sub_arbol.clave, sub_arbol.izq = self.__buscar_y_reemplazar_der(sub_arbol.izq)
            exitoso = True
        else:
            sub_arbol.clave, sub_arbol.der = self.__buscar_y_reemplazar_izq(sub_arbol.der)
            exitoso = True
        return exitoso, sub_arbol
