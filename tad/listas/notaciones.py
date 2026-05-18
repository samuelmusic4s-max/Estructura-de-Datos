from tad.listas.pila import Pila

# Autores:
# Andrés Felipe Caguasango Chiran
# Samuel Alejandro Botina Narváez


class Postfija:
    def __init__(self, expresion_infija):
        self.validar_expresion(expresion_infija)
        self.expresion_infija = self.to_list(expresion_infija)

    def validar_expresion(self, expresion):
        cont = 0
        if expresion.strip() == "":
            raise ValueError("Ingrese una expresion válida por favor")
        if not isinstance(expresion, str):
            error = "Ingrese una cadena con una expresion válida por favor"
            raise ValueError(error)
        caracteres_validos = set('0123456789+-*/^()x ')
        for char in expresion:
            if char.isnumeric():
                continue
            if char not in caracteres_validos:
                error = "Operaciones no soportadas por esta clase."
                error += " Intente nuevamente solo con +, -, x, *, /, ^"
                raise ValueError(error)
            if char == "(":
                cont += 1
            if char == ")":
                cont -= 1
                if cont < 0:
                    error = "Inconsistencias en los paréntesis. Ingrese una"
                    error += " cadena válida."
                    raise ValueError(error)
        if cont != 0:
            error = "Inconsistencias en los paréntesis. Ingrese una"
            error += " cadena válida."
            raise ValueError(error)

    def to_list(self, in_fija: str):
        digits = ""
        expresion = []
        for char in in_fija:
            if char.isnumeric():
                digits += char
                continue
            else:
                if digits != "":
                    expresion.append(digits)
                    digits = ""
                if char != " ":
                    expresion.append(char)
        if digits != "":
            expresion.append(digits)
        return expresion

    def in_fija(self):
        return " ".join(str(oper) for oper in self.expresion_infija)

    def post_fija(self):
        reglas = {
            '+': [1, 1],
            '-': [1, 1],
            '*': [2, 2],
            '/': [2, 2],
            '^': [3, 4],
            '(': [5, 0],
            'x': [2, 2]
        }
        operadores = Pila()
        expresion_postfija = []
        for oper in self.expresion_infija:
            if oper.isnumeric():
                expresion_postfija.append(oper)
                continue
            if oper not in reglas:
                continue
            if operadores.es_vacia():
                operadores.apilar(oper)
                continue
            if oper == ')':
                while not operadores.es_vacia() and operadores.cima() != '(':
                    expresion_postfija.append(operadores.desapilar())
                operadores.desapilar()
                continue
            if reglas[oper][0] <= reglas[operadores.cima()][1]:
                while (not operadores.es_vacia() and
                       reglas[oper][0] <= reglas[operadores.cima()][1]):
                    expresion_postfija.append(operadores.desapilar())
            operadores.apilar(oper)
        while not operadores.es_vacia():
            expresion_postfija.append(operadores.desapilar())
        return " ".join(str(oper) for oper in expresion_postfija)

    def eval_expr_aritmetica(self):
        operaciones = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '^': lambda a, b: a ** b,
            'x': lambda a, b: a * b
        }
        operandos = Pila()
        expresion_postfija = self.post_fija().split(" ")
        for oper in expresion_postfija:
            if oper.isnumeric():
                operandos.apilar(int(oper))
                continue
            num2 = operandos.desapilar()
            num1 = operandos.desapilar()
            try:
                resultado = operaciones[oper](num1, num2)
            except ZeroDivisionError as e:
                print("Error : ", e)
                raise ValueError("NO SE PUEDE DIVIDIR ENTRE 0")
            except Exception as e:
                raise ValueError(f"Error inesperado: {e}")
            else:
                operandos.apilar(resultado)
        return float(operandos.desapilar())
