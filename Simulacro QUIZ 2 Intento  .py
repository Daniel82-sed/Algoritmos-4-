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
   
    
    fila = tablero[num_fila]

    numeros_fila = set(fila)

    if numeros_fila == NUMEROS_VALIDOS:
        return True

    return False



# PUNTO 1.2 (1.0): Validar una columna
def validar_columna(tablero, num_columna):
    """
    Retorna True si la columna contiene exactamente los números 1-9 sin repetir.
    
    
    Ejemplo:
        validar_columna(TABLERO, 0) -> True (columna [5,6,1,8,4,7,9,2,3])
    """
     
    columna = [fila[num_columna] for fila in tablero]

    numeros_columna = set(columna)

    if numeros_columna == NUMEROS_VALIDOS:
        return True

    return False



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

    if fila_inicio not in {0, 3, 6}: # valida las filas de incio de subcuadros del sudoku
        return False

    if col_inicio  not in {0, 3, 6}: # valida las filas de incio de subcuadros del sudoku
        return False 

    numeros_subcuadro = set()

    for fila in range (fila_inicio, fila_inicio + 3):
        for columna in range (col_inicio, col_inicio + 3):
            numero = tablero[fila][columna]
            if numero not in NUMEROS_VALIDOS:
                False
            numeros_subcuadro.add(numero)
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
    # TODO: Implementar usando es_subconjunto
    pass


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

""""
#SOLUCION DE SEGUNDA PARTE SEGUN EL DARK INK 
#INICIO SIMULACRO
    # PUNTO 2.1: Verificar si es subconjunto
    def es_subconjunto(self, otro):
        #Retorna True si este conjunto es subconjunto de otro.

        actual = self.cabeza

        # Revisamos cada elemento de este conjunto
        while actual:

            # Si el elemento no está en el otro conjunto,
            # entonces NO es subconjunto
            if not otro.pertenece(actual.dato):
                return False

            actual = actual.siguiente

        # Todos los elementos fueron encontrados
        return True

    def __str__(self):
        elementos = []
        actual = self.cabeza

        # Guardamos los elementos para mostrarlos
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        return "{" + ", ".join(elementos) + "}"


# PUNTO 2.2: Verificar permisos de usuario
def tiene_permisos(permisos_usuario, permisos_requeridos):
    # Los permisos requeridos deben estar dentro de los permisos que tiene el usuario
    return permisos_requeridos.es_subconjunto(permisos_usuario)


# --------------------------------------------------
# DEFINIR ROLES
# --------------------------------------------------

# Primero creamos los conjuntos
admin = Conjunto(["leer", "escribir", "eliminar", "crear_usuarios"])
editor = Conjunto(["leer", "escribir"])
viewer = Conjunto(["leer"])


print(f"\n👤 Roles definidos:")
print(f" Admin: {admin}")
print(f" Editor: {editor}")
print(f" Viewer: {viewer}")


# --------------------------------------------------
# PROBAR SUBCONJUNTOS
# --------------------------------------------------

print(f"\n🔍 Verificando subconjuntos:")

print(f" ¿Viewer ⊆ Editor? {viewer.es_subconjunto(editor)}")
print(f" ¿Editor ⊆ Admin? {editor.es_subconjunto(admin)}")
print(f" ¿Admin ⊆ Editor? {admin.es_subconjunto(editor)}")


# --------------------------------------------------
# PARTE 2: PROBAR PERMISOS
# --------------------------------------------------

print(f"\n🔐 Verificando permisos:")

# Permisos necesarios para editar
accion_editar = Conjunto(["leer", "escribir"])

# Permisos necesarios para realizar acciones de administrador
accion_admin = Conjunto(["crear_usuarios", "eliminar"])


print(f" Acción editar requiere: {accion_editar}")
print(f" Acción admin requiere: {accion_admin}")


# Comprobamos si cada usuario tiene los permisos necesarios
print(f"\n ¿Editor puede editar? {tiene_permisos(editor, accion_editar)}")

print(f" ¿Viewer puede editar? {tiene_permisos(viewer, accion_editar)}")

print(f" ¿Admin puede hacer acción admin? {tiene_permisos(admin, accion_admin)}")

print(f" ¿Editor puede hacer acción admin? {tiene_permisos(editor, accion_admin)}")


    
"""