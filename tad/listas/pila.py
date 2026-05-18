from tad.listas.nodos import NodoListaSimplementeEnlazada


class Pila:
    """Clase que implementa el funcionamiento del TAD Pila
    """
    def __init__(self):
        """Método constructor que realiza la creación e inicialización de
        una Pila
        """
        self.__cima = None
        self.__contador = 0

    def es_vacia(self):
        """Método que verifica si la pila se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la pila es vacia. False en caso contrario
        """
        return self.__contador == 0

    def apilar(self, nuevo_dato):
        """Método que realiza la entrada de un nuevo dato a la pila.
        Realizar la validación de Homogeneidad para cada dato ingresado
        a la pila
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la pila
        Returns
        -------
        bool
        True si nuevo_dato fue apilado. False en caso contrario
        """
        if not self.es_vacia() and not isinstance(nuevo_dato,
                                                  type(self.__cima.dato)):
            return False
        nuevo_nodo = NodoListaSimplementeEnlazada(nuevo_dato)
        nuevo_nodo.sig = self.__cima
        self.__cima = nuevo_nodo
        self.__contador += 1
        return True

    def desapilar(self):
        """Método que saca/quita el último nodo (elimina el nodo) de la pila
        y retorna su dato
        Returns
        -------
        object|None
        El dato del nodo desapilado y None cuando la pila no contenga
        nodos/datos
        """
        if self.es_vacia():
            return None
        dato_retorno = self.__cima.dato
        self.__cima = self.__cima.sig
        self.__contador -= 1
        return dato_retorno

    def cima(self):
        """Método que retorna el dato del último nodo ingresado en la pila,
        sin quitarlo de la misma
        Returns
        -------
        object|None
        El dato del último nodo ingresado y None cuando la pila no
        contenga nodos/datos
        """
        if self.es_vacia():
            return None
        return self.__cima.dato

    def __len__(self):
        """Método que retorna el número de nodos que contiene la pila
        Returns
        -------
        int
        Tamaño de la pila
        """
        return self.__contador

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la pila (sin desapilarlos)
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la pila, en el siguiente formato:
        “🔝[dato_n] 🔜 [dato_3] 🔜 [dato_2] 🔜 [dato_1]”
        Cuando hay un sólo dato:
        “🔝[dato_1]”
        Cuando no hay datos:
        “🔝”
        """
        cadena = "🔝"
        nodo_actual = self.__cima
        sw = 0
        while nodo_actual:
            if sw == 0:
                sw = 1
                cadena += f"[{nodo_actual}]"
                nodo_actual = nodo_actual.sig
                continue
            cadena += f" 🔜 [{nodo_actual}]"
            nodo_actual = nodo_actual.sig
        return cadena
