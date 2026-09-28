"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS
                    Validador de Sudoku + Sistema de Permisos
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
--------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado


═══════════════════════════════════════════════════════════════════════════════
                            PARTE 1: VALIDADOR DE SUDOKU (3.5)
═══════════════════════════════════════════════════════════════════════════════

Usar conjuntos de Python para validar un tablero de Sudoku.

REGLAS DEL SUDOKU:
- Cada fila debe contener los números 1-9 sin repetir
- Cada columna debe contener los números 1-9 sin repetir
- Cada subcuadro 3x3 debe contener los números 1-9 sin repetir
"""

# Importamos el módulo de expresiones regulares.
# Se utilizará para comprobar que cada elemento sea un dígito del 1 al 9.
import re


NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# PUNTO 1.1 (1.0): Validar una fila
def validar_fila(tablero, num_fila):
    """
    Retorna True si la fila contiene exactamente los números 1-9 sin repetir.
    
    Ejemplo:
        validar_fila(TABLERO, 0) -> True (fila [5,3,4,6,7,8,9,1,2])
    """

    # Obtenemos la fila indicada por num_fila.
    # Por ejemplo, si num_fila = 0 obtenemos la primera fila.
    fila = tablero[num_fila]

    # Una fila de Sudoku debe tener exactamente 9 elementos.
    if len(fila) != 9:
        return False

    # ---------------------------------------------------------------
    # VALIDACIÓN CON EXPRESIONES REGULARES
    # ---------------------------------------------------------------
    #
    # La expresión [1-9] significa:
    # "un solo carácter que sea un número entre 1 y 9".
    #
    # str(numero) convierte el número a texto porque las expresiones
    # regulares trabajan con cadenas.
    #
    # fullmatch() comprueba que TODO el valor coincida.
    #
    # Por ejemplo:
    #     5  -> válido
    #     9  -> válido
    #     0  -> inválido
    #     10 -> inválido
    # ---------------------------------------------------------------

    for numero in fila:
        if re.fullmatch(r"[1-9]", str(numero)) is None:
            return False

    # ---------------------------------------------------------------
    # VALIDACIÓN UTILIZANDO CONJUNTOS
    # ---------------------------------------------------------------
    #
    # set(fila) convierte la fila en un conjunto.
    #
    # Una característica de los conjuntos es que NO permiten
    # elementos repetidos.
    #
    # Por ejemplo:
    #
    #     set([1, 2, 2, 3])
    #
    # produce:
    #
    #     {1, 2, 3}
    #
    # Como NUMEROS_VALIDOS contiene exactamente los números 1 al 9,
    # podemos comparar ambos conjuntos.
    #
    # Si son iguales:
    #     - están todos los números del 1 al 9
    #     - no falta ninguno
    #     - no hay repetidos
    # ---------------------------------------------------------------

    numeros_fila = set(fila)

    return numeros_fila == NUMEROS_VALIDOS


# PUNTO 1.2 (1.0): Validar una columna
def validar_columna(tablero, num_columna):
    """
    Retorna True si la columna contiene exactamente los números 1-9 sin repetir.
    
    
    Ejemplo:
        validar_columna(TABLERO, 0) -> True (columna [5,6,1,8,4,7,9,2,3])
    """

    # El tablero debe tener 9 filas.
    if len(tablero) != 9:
        return False

    # ---------------------------------------------------------------
    # OBTENER LA COLUMNA
    # ---------------------------------------------------------------
    #
    # Una columna se obtiene tomando la misma posición de cada fila.
    #
    # Por ejemplo, para num_columna = 0:
    #
    # TABLERO[0][0] -> 5
    # TABLERO[1][0] -> 6
    # TABLERO[2][0] -> 1
    #
    # La comprensión de lista:
    #
    # [fila[num_columna] for fila in tablero]
    #
    # significa:
    # "toma de cada fila el elemento que está en num_columna".
    # ---------------------------------------------------------------

    columna = [fila[num_columna] for fila in tablero]

    # Comprobamos que cada elemento sea un dígito del 1 al 9.
    for numero in columna:
        if re.fullmatch(r"[1-9]", str(numero)) is None:
            return False

    # Convertimos la columna en conjunto.
    #
    # Si existe un número repetido, set() eliminará la repetición.
    # Por eso después de la comparación sabremos si están exactamente
    # los números del 1 al 9.
    numeros_columna = set(columna)

    return numeros_columna == NUMEROS_VALIDOS


# PUNTO 1.3 (1.5): Validar un subcuadro 3x3
def validar_subcuadro(tablero, fila_inicio, col_inicio):
    """
    Retorna True si el subcuadro 3x3 contiene exactamente los números 1-9.
    
    fila_inicio y col_inicio indican la esquina superior izquierda del subcuadro.
    Los valores válidos son: 0, 3, 6
    
    Ejemplo:
        validar_subcuadro(TABLERO, 0, 0) -> True (subcuadro superior izquierdo)
        validar_subcuadro(TABLERO, 3, 6) -> True (subcuadro central derecho)
    
    """

    # ---------------------------------------------------------------
    # VALIDAMOS LA POSICIÓN INICIAL
    # ---------------------------------------------------------------
    #
    # Un subcuadro 3x3 solamente puede comenzar en:
    #
    # 0, 3 o 6
    #
    # Por ejemplo:
    #
    # (0,0) -> esquina superior izquierda
    # (0,3) -> parte superior central
    # (0,6) -> esquina superior derecha
    # (3,0) -> parte central izquierda
    # ...
    # (6,6) -> esquina inferior derecha
    #
    # Utilizamos un conjunto para comprobar que el valor pertenezca
    # a las posiciones permitidas.
    # ---------------------------------------------------------------

    if fila_inicio not in {0, 3, 6}:
        return False

    if col_inicio not in {0, 3, 6}:
        return False

    # Creamos un conjunto vacío donde iremos guardando
    # los números encontrados en el subcuadro.
    numeros_subcuadro = set()

    # ---------------------------------------------------------------
    # RECORRER LAS 3 FILAS
    # ---------------------------------------------------------------
    #
    # Si fila_inicio = 0:
    #
    # range(0, 3)
    #
    # produce:
    # 0, 1, 2
    #
    # Si fila_inicio = 3:
    #
    # range(3, 6)
    #
    # produce:
    # 3, 4, 5
    #
    # Así recorremos exactamente las tres filas del subcuadro.
    # ---------------------------------------------------------------

    for fila in range(fila_inicio, fila_inicio + 3):

        # -----------------------------------------------------------
        # RECORRER LAS 3 COLUMNAS
        # -----------------------------------------------------------
        #
        # De la misma forma, recorremos solamente tres columnas.
        # -----------------------------------------------------------

        for columna in range(col_inicio, col_inicio + 3):

            numero = tablero[fila][columna]

            # Comprobamos que sea un número entre 1 y 9.
            if re.fullmatch(r"[1-9]", str(numero)) is None:
                return False

            # Agregamos el número al conjunto.
            #
            # Si el número ya estaba, set() no lo vuelve a agregar.
            # Esto nos ayuda a detectar repeticiones cuando finalmente
            # comparemos el conjunto con NUMEROS_VALIDOS.
            numeros_subcuadro.add(numero)

    # El subcuadro debe contener exactamente los números 1 al 9.
    return numeros_subcuadro == NUMEROS_VALIDOS


"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 2: SISTEMA DE PERMISOS CON LISTAS (2.0)
═══════════════════════════════════════════════════════════════════════════════

Implementar operaciones de subconjuntos usando la clase Conjunto con listas enlazadas.

CONTEXTO:
Un sistema tiene roles con diferentes permisos. Debes verificar si un rol
tiene todos los permisos necesarios para realizar ciertas acciones.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)
    
    def esta_vacio(self):
        return self.cabeza is None
    
    def pertenece(self, x):
        """Retorna True si x está en el conjunto"""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        """Agrega x si no existe"""
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTOS A IMPLEMENTAR
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 2.1 (1.0): Verificar si es subconjunto
def es_subconjunto(conjunto_a, conjunto_b):
    """
    Retorna True si conjunto_a es subconjunto de conjunto_b.
    Es decir, si TODOS los elementos de A están en B.
    
    A ⊆ B significa: para todo x en A, x también está en B
    
    Ejemplo:
        A = {leer, escribir}
        B = {leer, escribir, eliminar}
        es_subconjunto(A, B) -> True (A ⊆ B)
        es_subconjunto(B, A) -> False (B no es subconjunto de A)
    
    """

    # ---------------------------------------------------------------
    # IDEA DEL SUBCONJUNTO
    # ---------------------------------------------------------------
    #
    # Queremos comprobar:
    #
    #       A ⊆ B
    #
    # Esto significa:
    #
    # "cada elemento que está en A también debe estar en B".
    #
    # Recorremos A nodo por nodo y utilizamos el método pertenece()
    # de B para comprobar si ese elemento existe.
    # ---------------------------------------------------------------

    actual = conjunto_a.cabeza

    # Mientras existan nodos en A, seguimos recorriendo.
    while actual:

        # Si el elemento actual de A NO pertenece a B,
        # entonces A no puede ser subconjunto de B.
        if not conjunto_b.pertenece(actual.dato):
            return False

        # Avanzamos al siguiente nodo.
        #
        # Esto es importante porque garantiza que el while avance
        # y termine cuando lleguemos al final de la lista.
        actual = actual.siguiente

    # Si llegamos hasta aquí significa que revisamos TODOS
    # los elementos de A y todos estaban en B.
    return True


# PUNTO 2.2 (0.5): Verificar permisos de usuario
def tiene_permisos(permisos_usuario, permisos_requeridos):
    """
    Retorna True si el usuario tiene TODOS los permisos requeridos.
    
    Esto es equivalente a verificar si permisos_requeridos ⊆ permisos_usuario
    
    Ejemplo:
        usuario = Conjunto(["leer", "escribir", "eliminar"])
        requeridos = Conjunto(["leer", "escribir"])
        tiene_permisos(usuario, requeridos) -> True
        
        requeridos2 = Conjunto(["leer", "admin"])
        tiene_permisos(usuario, requeridos2) -> False (no tiene "admin")
    """

    # ---------------------------------------------------------------
    # IMPORTANTE:
    #
    # Aquí debemos comprobar:
    #
    #     permisos_requeridos ⊆ permisos_usuario
    #
    # NO al contrario.
    #
    # Por ejemplo:
    #
    # usuario:
    # {leer, escribir, eliminar}
    #
    # requeridos:
    # {leer, escribir}
    #
    # Queremos comprobar:
    #
    # {leer, escribir} ⊆ {leer, escribir, eliminar}
    #
    # Esto es verdadero.
    # ---------------------------------------------------------------

    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1: VALIDADOR DE SUDOKU")
    print("=" * 60)
    
    # Probar validación de filas
    print("\n📋 Validando filas:")
    for i in range(9):
        resultado = validar_fila(TABLERO, i)
        print(f"  Fila {i+1}: {'✓' if resultado else '✗'}")
    
    # Probar validación de columnas
    print("\n📋 Validando columnas:")
    for j in range(9):
        resultado = validar_columna(TABLERO, j)
        print(f"  Columna {j+1}: {'✓' if resultado else '✗'}")
    
    # Probar validación de subcuadros
    print("\n📋 Validando subcuadros 3x3:")
    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:
            resultado = validar_subcuadro(TABLERO, fi, ci)
            print(f"  Subcuadro ({fi+1},{ci+1}): {'✓' if resultado else '✗'}")
    
    print("\n" + "=" * 60)
    print("PARTE 2: SISTEMA DE PERMISOS")
    print("=" * 60)
    
    # Definir roles
    admin = Conjunto(["leer", "escribir", "eliminar", "crear_usuarios"])
    editor = Conjunto(["leer", "escribir"])
    viewer = Conjunto(["leer"])
    
    print(f"\n👤 Roles definidos:")
    print(f"  Admin: {admin}")
    print(f"  Editor: {editor}")
    print(f"  Viewer: {viewer}")
    
    # Probar subconjuntos
    print(f"\n🔍 Verificando subconjuntos:")
    print(f"  ¿Viewer ⊆ Editor? {es_subconjunto(viewer, editor)}")  # True
    print(f"  ¿Editor ⊆ Admin? {es_subconjunto(editor, admin)}")    # True
    print(f"  ¿Admin ⊆ Editor? {es_subconjunto(admin, editor)}")    # False
    
    # Probar permisos
    print(f"\n🔐 Verificando permisos:")
    
    accion_editar = Conjunto(["leer", "escribir"])
    accion_admin = Conjunto(["crear_usuarios", "eliminar"])
    
    print(f"  Acción editar requiere: {accion_editar}")
    print(f"  Acción admin requiere: {accion_admin}")
    
    print(f"\n  ¿Editor puede editar? {tiene_permisos(editor, accion_editar)}")  # True
    print(f"  ¿Viewer puede editar? {tiene_permisos(viewer, accion_editar)}")    # False
    print(f"  ¿Admin puede hacer acción admin? {tiene_permisos(admin, accion_admin)}")  # True
    print(f"  ¿Editor puede hacer acción admin? {tiene_permisos(editor, accion_admin)}")  # False
