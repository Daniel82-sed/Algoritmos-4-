#CODIGO GENERADO POR INTELIGENCIA ARTFICIAL UTILIZANDO COMO BASE LA ESTRUCTURA Y FORMA DE
#PROGRAMACIÓN DEL PROFESOR JUAN , TIENE COMENTARIOS Y FUNCIONES CLARA MASS OTRA VERSION
#DEL MISMO CODIGO QUE CUMPLE LO MISMO PERO DE UNA FORMA MAS SIMPLE COMENTADO DE FORMA 
#COMPLETA AL FINAL DEL CODIGO 
#---------------------------------------------------------------------------------
# ============================================================
# VALIDACIÓN DE EXPRESIONES BALANCEADAS USANDO RECURSIVIDAD
# ============================================================
# Se reutiliza el concepto de Pila (estructura LIFO) de los
# códigos de referencia "Pila_1_.py" y "Pila_2_y_operacion_postfija.py".
# La Pila se implementa con nodos enlazados (Nodo + puntero "tope"),
# igual que en los archivos originales, porque es la estructura ideal
# para verificar el ORDEN de apertura y cierre de símbolos: el último
# símbolo abierto debe ser el primero en cerrarse (LIFO).

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        self.tam = 0  # cantidad de elementos en la pila

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):
        # Inserta un nuevo dato en el tope de la pila (al inicio)
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tam += 1

    def pop(self):
        # Saca y devuelve el dato que está en el tope
        if self.esta_vacia():
            raise Exception("Error: No hay elementos en la pila")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tam -= 1
        return dato

    def peek(self):
        # Muestra el dato del tope sin eliminarlo
        if self.esta_vacia():
            raise Exception("Error: No hay elementos en la pila")
        return self.tope.dato

    def __len__(self):
        return self.tam


# Diccionario que relaciona cada símbolo de cierre con su símbolo
# de apertura correspondiente. Sirve para saber, al encontrar un
# cierre, si coincide con lo último que se abrió (tope de la pila).
CIERRES = {
    ')': '(',
    ']': '[',
    '}': '{'
}
APERTURAS = set(CIERRES.values())


def es_balanceada_recursivo(expresion, indice, pila):
    """
    Función RECURSIVA que revisa la expresión posición por posición.

    Parámetros:
        expresion (str): la cadena completa a validar.
        indice (int): posición actual que se está analizando (avanza
                      en cada llamada recursiva, como si fuera el
                      contador de un for, pero manejado por recursión).
        pila (Pila): guarda los símbolos de apertura que aún no han
                     sido cerrados, respetando el orden LIFO.

    Devuelve:
        True  -> si la expresión está balanceada.
        False -> si no lo está (símbolo mal cerrado, desordenado o sobrante).

    CASO BASE:
        Cuando "indice" llega al final de la cadena (indice == len(expresion)),
        ya no quedan símbolos por revisar. En ese punto la expresión solo
        está balanceada si la pila quedó vacía (todo lo abierto se cerró).

    LLAMADA RECURSIVA:
        En cada paso se procesa UN solo carácter y luego la función se
        vuelve a llamar a sí misma con indice + 1, avanzando de a un
        carácter por vez hasta llegar al caso base. Así se reemplaza
        el uso de un bucle for/while por recursividad.
    """

    # --- CASO BASE ---
    # Si ya recorrimos toda la expresión, el resultado depende de
    # que no haya quedado ningún símbolo de apertura sin cerrar.
    if indice == len(expresion):
        return pila.esta_vacia()

    caracter = expresion[indice]

    # Si el carácter es un símbolo de apertura, se guarda en la pila
    # porque "está pendiente" de que llegue su cierre correspondiente.
    if caracter in APERTURAS:
        pila.push(caracter)
        return es_balanceada_recursivo(expresion, indice + 1, pila)

    # Si el carácter es un símbolo de cierre, se compara con el tope
    # de la pila (el último símbolo abierto, según orden LIFO).
    if caracter in CIERRES:
        # Error si no hay nada que cerrar (pila vacía) o si el símbolo
        # del tope no corresponde al cierre actual (orden incorrecto).
        if pila.esta_vacia() or pila.pop() != CIERRES[caracter]:
            return False
        return es_balanceada_recursivo(expresion, indice + 1, pila)

    # Cualquier otro carácter (letras, números, espacios) se ignora
    # y simplemente avanzamos al siguiente índice.
    return es_balanceada_recursivo(expresion, indice + 1, pila)


def validar_expresion(expresion):
    """
    Función "envoltorio" (wrapper) que prepara los datos iniciales
    (índice = 0 y una pila vacía) y llama a la función recursiva.
    Se separa de la función recursiva para no obligar al usuario
    a pasar manualmente el índice y la pila cada vez que valida
    una expresión nueva.
    """
    # Quitamos los espacios para poder validar expresiones como "( { } )"
    expresion_limpia = expresion.replace(" ", "")
    pila = Pila()
    return es_balanceada_recursivo(expresion_limpia, 0, pila)


# ============================================================
# PRUEBAS
# ============================================================
casos_de_prueba = [
    "( { } )",      # balanceada
    "( { ) }",      # no balanceada: orden incorrecto
    "( [ ] ) { }",  # balanceada
    "( [ ] { }",    # no balanceada: falta un cierre
    ""              # vacía: se considera balanceada (no hay nada sin cerrar)
]

for expr in casos_de_prueba:
    resultado = validar_expresion(expr)
    estado = "BALANCEADA" if resultado else "NO BALANCEADA"
    print(f'Expresion: "{expr}"  ->  {estado}')


"""
Segunda implementación
-----------------------
Versión más simple del mismo problema, también recursiva, pero sin
usar la clase Pila con nodos: aquí se usa una lista de Python como
pila (append = push, pop = pop), lo que simplifica mucho el código
manteniendo la misma lógica de recursividad y orden LIFO.

def es_balanceada(expresion, pila=None):
    # En la primera llamada se crea la pila (lista vacía).
    if pila is None:
        pila = []

    # CASO BASE: si la expresión quedó vacía, ya se revisó todo.
    # Está balanceada solo si no quedaron símbolos abiertos en la pila.
    if not expresion:
        return len(pila) == 0

    caracter = expresion[0]        # primer caracter a analizar
    resto = expresion[1:]          # el resto de la expresión (para la recursión)

    pares = {')': '(', ']': '[', '}': '{'}

    if caracter in "([{":
        # Es apertura: se apila y se sigue con el resto (llamada recursiva)
        pila.append(caracter)
        return es_balanceada(resto, pila)

    if caracter in ")]}":
        # Es cierre: debe coincidir con el último abierto (tope de la pila)
        if not pila or pila.pop() != pares[caracter]:
            return False
        return es_balanceada(resto, pila)

    # Si es otro caracter (espacio, letra, etc.) se ignora y se avanza
    return es_balanceada(resto, pila)


# Pruebas
pruebas = ["( { } )", "( { ) }", "( [ ] ) { }", "( [ ] { }", ""]
for e in pruebas:
    r = es_balanceada(e.replace(" ", ""))
    print(f'"{e}" -> {"BALANCEADA" if r else "NO BALANCEADA"}')
"""