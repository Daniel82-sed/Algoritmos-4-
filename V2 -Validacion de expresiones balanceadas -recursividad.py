# ============================================================
# SEGUNDA IMPLEMENTACIÓN (VERSIÓN AMPLIADA Y COMENTADA)
# Validación de expresiones balanceadas usando recursividad
# ============================================================
# Esta versión es más simple que la primera porque en lugar de usar
# una clase Pila hecha con Nodos enlazados, usa una LISTA de Python
# como si fuera una pila. Una lista de Python ya tiene los métodos
# append() y pop() que funcionan exactamente como push y pop:
#   - lista.append(x)  -> equivale a "apilar" x (push)
#   - lista.pop()      -> equivale a "desapilar" (pop), saca el ÚLTIMO
#                          elemento agregado, que es justo el
#                          comportamiento LIFO (Last In, First Out)
#                          que necesitamos para este problema.
#
# ¿Por qué necesitamos una pila (LIFO) para este problema?
# Porque el símbolo de cierre siempre debe corresponder al ÚLTIMO
# símbolo de apertura que todavía no se ha cerrado.
# Ejemplo: en "( [ ] )", cuando aparece "]" debe cerrar el "["
# que se abrió más recientemente, no el "(" que se abrió antes.


def es_balanceada(expresion, pila=None):
    """
    Función RECURSIVA que valida si una expresión está balanceada.

    Parámetros:
        expresion (str): la parte de la expresión que aún falta por
                          revisar. En cada llamada recursiva esta
                          cadena se hace más corta (se le quita el
                          primer carácter), hasta quedar vacía.
        pila (list): lista que actúa como pila. Guarda los símbolos
                     de apertura que todavía no han sido cerrados.
                     Empieza en None y se crea vacía la primera vez
                     que se llama a la función (ver más abajo).

    Devuelve:
        True  -> si la expresión está balanceada.
        False -> si no lo está.

    IMPORTANTE SOBRE EL PARÁMETRO "pila=None":
        La primera vez que el usuario llama a esta función normalmente
        NO le pasa ninguna pila, solo el texto a revisar. Por eso el
        valor por defecto es None. Dentro de la función detectamos
        ese caso y creamos la pila vacía. Esto evita que el usuario
        tenga que preocuparse por crear la pila manualmente.
    """

    # Si es la primera llamada (no viene ninguna pila todavía),
    # se crea una lista vacía que funcionará como pila.
    if pila is None:
        pila = []

    # ------------------------------------------------------
    # CASO BASE DE LA RECURSIÓN
    # ------------------------------------------------------
    # Cuando "expresion" queda vacía significa que ya se revisó
    # TODO el texto, carácter por carácter, gracias a las llamadas
    # recursivas anteriores. Aquí termina la recursión.
    #
    # En este punto, la expresión está balanceada SOLO SI la pila
    # quedó vacía. Si quedó vacía significa que cada símbolo de
    # apertura que se guardó, también encontró su cierre correcto.
    # Si la pila NO quedó vacía, significa que sobraron símbolos
    # de apertura sin cerrar (ejemplo: "( [ ] { }" le falta un ")").
    if len(expresion) == 0:
        return len(pila) == 0

    # ------------------------------------------------------
    # PASO RECURSIVO: se analiza un solo carácter por llamada
    # ------------------------------------------------------
    # Se toma el PRIMER carácter de lo que queda por revisar.
    caracter_actual = expresion[0]

    # El "resto" es todo lo que queda después de ese primer carácter.
    # Este "resto" es lo que se le pasará a la próxima llamada
    # recursiva, haciendo que la cadena sea cada vez más pequeña
    # hasta llegar al caso base (cadena vacía).
    resto_de_la_expresion = expresion[1:]

    # Diccionario que dice, para cada símbolo de CIERRE, cuál es
    # su símbolo de APERTURA correspondiente. Se usa para comparar
    # contra el tope de la pila cuando encontramos un cierre.
    pares_de_simbolos = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # --- CASO 1: el carácter actual es un símbolo de APERTURA ---
    if caracter_actual in "([{":
        # Se apila (push) el símbolo de apertura, porque queda
        # "pendiente" hasta que aparezca su cierre correspondiente.
        pila.append(caracter_actual)

        # Llamada recursiva: se sigue revisando el resto de la
        # expresión, ya con el símbolo agregado a la pila.
        return es_balanceada(resto_de_la_expresion, pila)

    # --- CASO 2: el carácter actual es un símbolo de CIERRE ---
    if caracter_actual in ")]}":
        # Error si la pila está vacía: significa que apareció un
        # cierre sin que exista ningún símbolo abierto pendiente.
        # Ejemplo: la expresión empieza directamente con ")".
        if len(pila) == 0:
            return False

        # Se saca (pop) el símbolo que está en el tope de la pila,
        # es decir, el último símbolo de apertura que se guardó.
        ultimo_simbolo_abierto = pila.pop()

        # Se compara ese símbolo con el que debería corresponder
        # al cierre actual. Si no coinciden, el ORDEN está mal.
        # Ejemplo: "( [ )" -> al llegar a ")" el tope de la pila
        # es "[", pero ")" necesita que el tope sea "(".
        simbolo_esperado = pares_de_simbolos[caracter_actual]
        if ultimo_simbolo_abierto != simbolo_esperado:
            return False

        # Si coinciden, ese par quedó correctamente cerrado y se
        # continúa revisando el resto de la expresión.
        return es_balanceada(resto_de_la_expresion, pila)

    # --- CASO 3: cualquier otro carácter (letras, números, espacios) ---
    # No afecta el balanceo, así que simplemente se ignora y se
    # avanza a la siguiente llamada recursiva con el resto del texto.
    return es_balanceada(resto_de_la_expresion, pila)


# ============================================================
# FUNCIÓN AUXILIAR PARA LIMPIAR ESPACIOS ANTES DE VALIDAR
# ============================================================
def validar(expresion):
    """
    Quita los espacios de la expresión (para poder escribir cosas
    como "( { } )" con espacios entre símbolos) y luego llama a la
    función recursiva es_balanceada() para obtener el resultado.
    """
    expresion_sin_espacios = expresion.replace(" ", "")
    return es_balanceada(expresion_sin_espacios)


# ============================================================
# PRUEBAS DE LA SEGUNDA IMPLEMENTACIÓN
# ============================================================
casos_de_prueba = [
    "( { } )",       # balanceada
    "( { ) }",       # no balanceada: orden incorrecto
    "( [ ] ) { }",   # balanceada
    "( [ ] { }",     # no balanceada: falta un cierre
    ""               # vacía: se considera balanceada
]

for expr in casos_de_prueba:
    resultado = validar(expr)
    estado = "BALANCEADA" if resultado else "NO BALANCEADA"
    print(f'Expresion: "{expr}"  ->  {estado}')