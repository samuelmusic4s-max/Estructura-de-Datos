from tad.listas.nodos import NodoListaSimplementeEnlazada


class ListaSimplementeEnlazada:
    """Clase que implementa el funcionamiento de una lista simplemente
    enlazada.
    """

    def __init__(self):
        """Método que inicializa la cabecera de una lista simplemente
        enlazada a un valor None (lista vacía).
        """
        self.__cab = None

    def es_vacia(self):
        """Método que verifica si una lista está vacía o no.
        Returns
        -------
        bool
            Devuelve True, si la lista es vacía, y False en caso contrario.
        """
        return self.__cab is None

    def agregar(self, nuevo_dato):
        """Método que agrega un nuevo nodo al final de la lista.
        ATENCIÓN: Validar la condición de homogeneidad de la lista, para
        que todos los datos sean de un mismo tipo, el cuál esta dado por
        el tipo del primer nodo.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser agregado a la lista

        Returns
        -------
        bool
            True cuando el dato es agregado a la lista. False, en caso
            contrario.
        """
        # Creación de un nuevo nodo para ser adicionado a la lista
        nuevo_nodo = NodoListaSimplementeEnlazada(nuevo_dato)
        # Si la lista es vacía se procesede a vincular el nuevo nodo
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            if type(self.__cab.dato) is not type(nuevo_dato):
                return False
            # En el caso de que la lista no sea vacía se debe ubicar el
            # nuevo nodo al final de la lista
            nodo_actual = self.__cab
            while nodo_actual.sig:
                nodo_actual = nodo_actual.sig
                # nodo_actual se encuentra en el último nodo de la lista
            nodo_actual.sig = nuevo_nodo
        return True

    def explorar(self):
        """Método que explora la lista, imprimiendo cada uno de los datos que
        contenga, siempre y cuando no sea una lista vacía.
        """
        nodo_actual = self.__cab
        while nodo_actual:
            print(nodo_actual)
            nodo_actual = nodo_actual.sig

    def buscar(self, item, por_dato=True):
        """Método de búsqueda en una lista.

        Parameters
        ----------
        item: object|int
            Puede corresponder al valor del dato a ser buscado en la lista
            o a la posición en la lista a obtener el dato.
        por_dato (bool, optional):
            Si es True, el método intentará buscar un dato por su valor,
            de lo contrario se intentará hacerlo por su posición. Por defecto
            es True.

        Returns
        -------
        object|None
            object si el dato es ubicado en la lista, None en caso contrario.
        """
        if por_dato:
            return self.__buscar_dato(item)
        else:
            return self.__buscar_pos(item)

    def __buscar_dato(self, dato_buscar):
        if type(self.__cab.dato) is not type(dato_buscar):
            return None
        nodo_actual = self.__cab
        while nodo_actual and nodo_actual.dato != dato_buscar:
            nodo_actual = nodo_actual.sig
        if nodo_actual:
            return nodo_actual.dato
        return None

    def __buscar_pos(self, posicion_buscar):
        if not isinstance(posicion_buscar, int):
            return None
        if posicion_buscar < 0 or self.es_vacia():
            return None
        if posicion_buscar == 0:
            if self.__cab:
                return self.__cab.dato
            return None
        nodo_aux = self.__cab
        cont = 0
        while nodo_aux and cont < posicion_buscar:
            cont += 1
            nodo_aux = nodo_aux.sig
        if nodo_aux:
            return nodo_aux.dato
        return None

    def insertar(self, nuevo_dato, pos=0):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será la
        posición cero (0). Si la lista ya contiene datos, serán válidas
        las posiciones intermedias o la posición inmediatamente superior
        a la del último dato.

        Parameters
        ----------
        nuevo_dato: object:
            El nuevo dato a ser insertado en la lista.
        pos (int, optional):
            Posición a insertar en la lista.

        Returns:
        --------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        if not isinstance(pos, int):
            return None
        if pos < 0:
            return None
        if pos == 0:
            if self.__cab is None:
                self.__cab = NodoListaSimplementeEnlazada(nuevo_dato)
                return True
            nodo_aux = NodoListaSimplementeEnlazada(nuevo_dato)
            nodo_aux.sig = self.__cab
            self.__cab = nodo_aux
            return True
        cont = 0
        nodo_aux = self.__cab
        while cont + 1 < pos and nodo_aux.sig:
            cont += 1
            nodo_aux = nodo_aux.sig
        if cont + 1 == pos:
            if nodo_aux.sig:
                nuevo_nodo = NodoListaSimplementeEnlazada(nuevo_dato)
                nuevo_nodo.sig = nodo_aux.sig
                nodo_aux.sig = nuevo_nodo
                return True
            nuevo_nodo = NodoListaSimplementeEnlazada(nuevo_dato)
            nodo_aux.sig = nuevo_nodo
            return True
        return False

    def suprimir(self, item, por_dato=True):
        """Método que permite suprimir uno o varios nodos de la lista ya sea
        por una posición o por el dato correspondiente.

        Parameters
        ----------
        item (object|int):
            Puede corresponder al valor del dato a ser suprimido de la lista
            o a la posición en la lista a suprimir el dato.
        por_dato (bool, optional):
            Si es True, el método intentará suprimir todos los datos
            coincidentes por su valor. Si es False, se intentará hacerlo
            por su posición. Por defecto True.

        Returns
        -------
        bool
            True cuando el dato es suprimido una o más veces de la list.
            False en caso contrario.
        """
        if por_dato:
            return self.__suprimir_dato(item)
        return self.__suprimir_pos(item)

    def __suprimir_pos(self, pos_sup):
        if self.es_vacia():
            return False
        if not isinstance(pos_sup, int):
            return False
        if self.__cab is None or pos_sup < 0:
            return False
        if pos_sup == 0:
            if self.__cab.sig:
                self.__cab = self.__cab.sig
                return True
            self.__cab = None
            return True
        nodo_aux = self.__cab
        pos = 1
        while pos != pos_sup and nodo_aux.sig:
            pos += 1
            nodo_aux = nodo_aux.sig
        if nodo_aux.sig is None:
            return False
        nodo_aux.sig = nodo_aux.sig.sig
        return True

    def __suprimir_dato(self, item):
        if self.es_vacia():
            return False
        if not isinstance(item, type(self.__cab.dato)):
            return False
        if not self.__cab.sig:
            if self.__cab.dato == item:
                self.__cab = None
                return True
            return False
        if self.__cab.dato == item:
            self.__cab = self.__cab.sig
            return True
        nodo_actual = self.__cab
        while nodo_actual.sig:
            if nodo_actual.sig.dato == item:
                nodo_actual.sig = nodo_actual.sig.sig
                return True
            nodo_actual = nodo_actual.sig
        return False

    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, o una
        cadena vacía en el caso de que la lista sea vacía.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el formato
            (ejemplo para 4 datos):
            "📜 |dato_0| -> |dato_1| -> |dato_2| -> |dato_3|"
            de lo contrario retornará una cadena con el siguiente formato:
                "📜"
        """
        cadena = "📜"
        nodo_aux = self.__cab
        while nodo_aux:
            cadena += f" |{nodo_aux}|"
            if nodo_aux.sig:
                cadena += " ->"
            nodo_aux = nodo_aux.sig
        return cadena

    def __len__(self):
        if self.es_vacia():
            return 0
        contador = 0
        nodo_aux = self.__cab
        while nodo_aux:
            contador += 1
            nodo_aux = nodo_aux.sig
        return contador

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        dato_actual = self.buscar(self.__index, False)
        if dato_actual is not None:
            self.__index += 1
            return dato_actual
        raise StopIteration
