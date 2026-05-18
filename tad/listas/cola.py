from tad.listas.lcse import ListaCircularSimplementeEnlazada


class Cola:
    """Clase que implementa el funcionamiento del TAD Cola
    """
    def __init__(self):
        """Método que realiza la creación e inicialización de la Cola
        """
        self.lista = ListaCircularSimplementeEnlazada()

    def es_vacia(self):
        """Método que verifica si la cola se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la cola es vacia. False en caso contrario
        """
        return len(self.lista) == 0

    def encolar(self, nuevo_dato):
        """Método que adiciona un nuevo dato al final de la cola. Realizar la
        validación de Homogeneidad para cada dato ingresado a la cola
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la cola
        Returns
        -------
        bool
        True si nuevo_dato fue encolado. False en caso contrario
        """
        if self.lista.agregar(nuevo_dato):
            return True
        return False

    def desencolar(self):
        """Método que saca/quita el primer nodo (elimina el nodo) de la cola
        y retorna su dato
        Returns
        -------
        object|None
        El dato del primer nodo de la cola y None cuando la cola no
        contenga nodos/datos
        """
        dato = self.lista.suerte(0)
        if self.lista.suprimir(0, False):
            return dato
        return None

    def frente(self):
        """Método que retorna el dato del primer nodo de la cola, sin quitarlo
        de la misma
        Returns
        -------
        object|None
        El dato del primer nodo en la cola y None cuando la cola no
        contenga nodos/datos
        """
        return self.lista.suerte(0)

    def __len__(self):
        """Método que retorna del número de nodos que contiene la cola
        Returns
        -------
        int
        Tamaño de la cola
        """
        return len(self.lista)

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la cola
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la cola, en el siguiente formato:
        "🏨|[dato_0]| 🚶🚶🚶 👈 (dato_1) 👈 (dato_2) 👈 (dato_n)"
        Cuando hay un sólo dato:
        "🏨#[dato_0]# 🚶🚶🚶"
        Cuando no hay datos:
        "🏨"
        """
        cadena = "🏨"
        if len(self.lista) == 1:
            cadena += f"#[{self.lista.suerte(0)}]# 🚶🚶🚶"
            return cadena
        sw = 0
        for dato in self.lista:
            if sw == 0:
                sw = 1
                cadena += f"|[{dato}]| 🚶🚶🚶"
                continue
            cadena += f" 👈 ({dato})"
        return cadena
