# Clase Nodo:
# Representa cada elemento que se va a guardar dentro de la pila.
class Nodo:
    def __init__(self, dato):
        # Guarda una referencia al siguiente nodo.
        # Al crear el nodo, inicialmente no apunta a ninguno.
        self.siguiente = None

        # Guarda el dato que tendrá este nodo.
        self.dato = dato


# Clase Pila:
# Se encarga de crear y manejar la estructura de datos tipo pila.
class Pila:
    def __init__(self):
        # El tope representa el elemento que está arriba de la pila.
        # Al comenzar, la pila está vacía, por eso es None.
        self.tope = None

    # Método para comprobar si la pila está vacía.
    def esta_vacia(self):
        # Si el tope es None, significa que no hay elementos.
        return self.tope is None

    # Método para agregar un elemento a la pila.
    def push(self, dato):
        # Creamos un nuevo nodo con el dato recibido.
        nuevo = Nodo(dato)

        # El nuevo nodo apunta al elemento que anteriormente
        # estaba en el tope de la pila.
        nuevo.siguiente = self.tope

        # Ahora el nuevo nodo se convierte en el nuevo tope.
        self.tope = nuevo

    # Método para sacar el elemento que está en el tope.
    def pop(self):
        # Primero comprobamos si la pila está vacía.
        if self.esta_vacia():
            # Si está vacía, no hay nada que sacar.
            return None

        # Guardamos el dato que está en el nodo del tope.
        dato = self.tope.dato

        # Movemos el tope al siguiente nodo.
        self.tope = self.tope.siguiente

        # Devolvemos el dato que acabamos de sacar.
        return dato

    # Método para consultar el elemento que está en el tope
    # sin eliminarlo de la pila.
    def peek(self):
        # Comprobamos si la pila está vacía.
        if self.esta_vacia():
            return None

        # Devolvemos solamente el dato que está en el tope.
        return self.tope.dato

    # Método para comprobar si los paréntesis, llaves y corchetes
    # de una expresión están correctamente balanceados.
    def parentesis_balanceados(self, expresion):
        # Creamos una pila que utilizaremos para guardar
        # los símbolos de apertura.
        pila = Pila()

        # Diccionario que relaciona cada símbolo de cierre
        # con su símbolo de apertura correspondiente.
        pares = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # Obtenemos los símbolos de apertura:
        # (, { y [
        aperturas = set(pares.values())

        # Obtenemos los símbolos de cierre:
        # ), } y ]
        cierres = set(pares.keys())

        # Recorremos cada carácter de la expresión.
        for caracter in expresion:

            # Si encontramos un símbolo de apertura,
            # lo guardamos en la pila.
            if caracter in aperturas:
                pila.push(caracter)

            # Si encontramos un símbolo de cierre,
            # debemos comprobar si corresponde con el último
            # símbolo de apertura guardado.
            elif caracter in cierres:

                # Si la pila está vacía, significa que encontramos
                # un cierre sin tener una apertura correspondiente.
                if pila.esta_vacia():
                    return False

                # Sacamos de la pila el último símbolo de apertura.
                tope = pila.pop()

                # Comprobamos si el símbolo de apertura coincide
                # con el símbolo que corresponde al cierre actual.
                if tope != pares[caracter]:
                    return False

        # Si al terminar la expresión la pila está vacía,
        # todos los símbolos de apertura fueron cerrados correctamente.
        return pila.esta_vacia()
# ============================================================
# PRUEBAS DEL PROGRAMA
# ============================================================

# Creamos un objeto de la clase Pila.
pila = Pila()


# Primera expresión:
# ( { } )
# Está balanceada porque cada símbolo de apertura
# tiene su correspondiente símbolo de cierre.
expresion1 = "( { } )"

# Segunda expresión:
# ( { ) }
# No está balanceada porque el ')' intenta cerrar
# el '{', pero debería cerrarse primero con '}'.
expresion2 = "( { ) }"

# Tercera expresión:
# ( [ ] ) { }
# Está balanceada porque todos los símbolos
# se abren y se cierran correctamente.
expresion3 = "( [ ] ) { }"

# Cuarta expresión:
# ( [ ] { }
# No está balanceada porque falta el ')' final
# para cerrar el primer paréntesis.
expresion4 = "( [ ] { }"


# Comprobamos cada expresión y mostramos el resultado.
print(expresion1, "-->", pila.parentesis_balanceados(expresion1),
      "Balanceada, cada token de apertura puede cerrarse.")

print(expresion2, "-->", pila.parentesis_balanceados(expresion2),
      "No balanceado, no es posible cerrar cada token de apertura con su token de cierre.")

print(expresion3, "-->", pila.parentesis_balanceados(expresion3),
      "Balanceado.")

print(expresion4, "-->", pila.parentesis_balanceados(expresion4),
      "No balanceado, falta un paréntesis de cierre.")