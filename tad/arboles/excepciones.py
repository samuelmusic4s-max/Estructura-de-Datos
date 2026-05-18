class DuplicatedKeyError(Exception):
    def __init__ (self, nueva_clave):
        super().__init__(f"La clave [{nueva_clave}] se encuentra DUPLICADA")

class HomogeneityError(Exception):
    def __init__(self, nueva_clave, tipo_dato) -> None:
        super().__init__(f"La clave [{nueva_clave}] NO ES DEL TIPO DE DATO [{tipo_dato}]")
