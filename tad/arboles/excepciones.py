class DuplicatedKeyError(Exception):
    def __init__ (self, nueva_clave):
        super().__init__(f"La clave [{nueva_clave}] se encuentra DUPLICADA")

class HomogeneityError(Exception):
    def __init__(self, type_nueva_clave, tipo_dato, accion) -> None:
        super().__init__(f"El arbol es del tipo de dato [{tipo_dato.__name__}], no se pueden {accion} variables del tipo {type_nueva_clave}")
