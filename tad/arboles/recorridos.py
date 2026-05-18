def __ver_nodo(sub_arbol, con_hijos=False):
    print(f"[{sub_arbol.clave}]")
    if con_hijos:
        print(f"{"O" if sub_arbol.izq else "X"} : " 
              f"{"O" if sub_arbol.der else "X"}")

def pre_orden(arbol_bin):
    __pre_orden(arbol_bin.raiz)

def __pre_orden(sub_arbol):
    if sub_arbol:
        __ver_nodo(sub_arbol)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)

def pre_orden_str(arbol_bin, separador="|>"):
    return __pre_orden_str(arbol_bin.raiz, separador).strip("|>")

def __pre_orden_str(sub_arbol, separador="|>"):
    cadena = ""
    if sub_arbol:
        cadena += f"{sub_arbol.clave}{separador}"
        cadena += f"{__pre_orden_str(sub_arbol.izq, separador)}"
        cadena += f"{__pre_orden_str(sub_arbol.der, separador)}"
    return cadena

def in_orden(arbol_bin):
    __in_orden(arbol_bin.raiz)

def __in_orden(sub_arbol):
    if sub_arbol:
        __in_orden(sub_arbol.izq)
        __ver_nodo(sub_arbol)
        __in_orden(sub_arbol.der)

def in_orden_str(arbol_bin, separador=">"):
    return __in_orden_str(arbol_bin.raiz, separador)

def __in_orden_str(sub_arbol, separador=">"):
    cadena = ""
    if sub_arbol:
        pass
