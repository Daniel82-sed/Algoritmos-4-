"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS (B)
            Gestión de Horarios Académicos + Inventario con Listas
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
--------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado



═══════════════════════════════════════════════════════════════════════════════
                    PARTE 1: GESTIÓN DE HORARIOS ACADÉMICOS (2.5)
═══════════════════════════════════════════════════════════════════════════════

Una universidad organiza el día académico en 10 franjas (numeradas 1 a 10).
El horario se guarda en un diccionario: cada clave es el nombre de un profesor
y cada valor es el CONJUNTO de franjas que tiene ocupadas.

Las funciones deben trabajar con CUALQUIER diccionario de horarios, no solo
con HORARIOS. La cantidad de profesores es variable.
"""

HORARIOS = {
    "garcia":   {1, 2, 6},
    "martinez": {1, 6, 7, 10},
    "lopez":    {7, 8, 10},
    "ruiz":     {2, 6, 8, 10},
}

TODAS_LAS_FRANJAS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# PUNTO 1.1 (0.8): Conflictos entre todos los pares de profesores
def conflictos_globales(horarios):
    """
    Retorna un DICCIONARIO con los conflictos de cada par de profesores,
    donde un conflicto es una franja en la que AMBOS tienen clase.

    Reglas del formato:
      - La clave es una tupla con los dos nombres ORDENADOS ALFABÉTICAMENTE.
      - El valor es el conjunto de franjas en conflicto.
      - Los pares SIN conflicto NO aparecen en el diccionario.
      - Cada par aparece UNA sola vez: ("ana","luis") o ("luis","ana"),
        nunca las dos.

    Ejemplo:
        h = {"luis": {2, 3}, "ana": {1, 2}, "sara": {5}}
        conflictos_globales(h) -> {("ana", "luis"): {2}}
        # los pares con "sara" no aparecen porque no tienen conflicto
    """

    # --- CÓDIGO ORIGINAL (comentado, no se elimina) ---
    # Motivo: imprimía en pantalla en vez de RETORNAR el diccionario, filtraba
    # con len(comunes) >= 2 (un conflicto de una sola franja también cuenta) y
    # la condición "comunes <= comunes" siempre es verdadera (no filtra nada).
    # La idea de recorrer los pares (i, j > i) y la intersección eran correctas
    # y se conservan abajo.
    #
    # conflictos = list(horarios.keys())
    # for i in range(len(conflictos)):
    #     for j in range (i + 1, (len(conflictos))):
    #         c1, c2 = conflictos[i], conflictos[j]
    #         comunes = horarios[c1] & horarios[c2]
    #
    #         if len(comunes) >= 2:
    #                     if comunes <= comunes :
    #                         """"comunes = {
    #                             c1 +" ---- Y ----- " + c2 : comunes
    #                         }
    #                         print(comunes)"""
    #                         print(f"  {c1} <---> {c2}")
    #                         print(f"Horarios en conflicto:{comunes}")

    # --- CÓDIGO CORREGIDO ---
    # Lista de nombres (antes se llamaba "conflictos"; se renombra para
    # reservar ese nombre al diccionario que sí se retorna).
    nombres = list(horarios.keys())
    conflictos = {}

    # j empieza en i + 1, así cada par se revisa UNA sola vez.
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            c1, c2 = nombres[i], nombres[j]
            comunes = horarios[c1] & horarios[c2]  # franjas ocupadas por ambos

            # Un conjunto vacío es "falso": solo guardamos pares con conflicto.
            if comunes:
                # tuple(sorted(...)) garantiza la clave en orden alfabético.
                conflictos[tuple(sorted((c1, c2)))] = comunes

    return conflictos


# PUNTO 1.2 (0.8): Franja más congestionada
def franja_mas_congestionada(horarios):
    """
    Retorna la franja (un entero) en la que MÁS profesores tienen clase
    al mismo tiempo.

    Reglas:
      - Si hay empate, retorna la franja MENOR.
      - Si ningún profesor tiene clases, retorna None.

    Ejemplo:
        h = {"ana": {1, 2}, "luis": {2, 3}, "sara": {3}}
        franja_mas_congestionada(h) -> 2
        # las franjas 2 y 3 tienen 2 profesores cada una; gana la menor
    """

    # --- CÓDIGO ORIGINAL (comentado, no se elimina) ---
    # Motivo: solo imprimía qué docentes ocupaban cada franja; nunca contaba
    # ni retornaba la franja con más profesores. Además recorría todos los
    # horarios una vez por cada franja (más costoso).
    #
    # todas_los_horas = set()
    #
    # for profesor, horas in horarios.items():
    #     todas_los_horas = todas_los_horas | horas
    #
    # for hora in sorted(todas_los_horas):
    #     print(f"\n  Hora congestionada -- > {hora}:" + (f"\n Docentes:"))
    #     for profesor, horas in horarios.items():
    #         if hora in horas:
    #             print(f"- {profesor}")

    # --- CÓDIGO CORREGIDO ---
    # conteo[franja] = cantidad de profesores que tienen clase en esa franja.
    # Se llena en una sola pasada por todos los horarios.
    conteo = {}
    for profesor, horas in horarios.items():
        for hora in horas:
            conteo[hora] = conteo.get(hora, 0) + 1

    # Si nadie tiene clases, no hay franja congestionada.
    if not conteo:
        return None

    maximo = max(conteo.values())

    # Entre las franjas que alcanzan el máximo, se elige la MENOR (desempate).
    return min(hora for hora, cantidad in conteo.items() if cantidad == maximo)


# PUNTO 1.3 (0.9): Franjas disponibles para una reunión
def franjas_reunion(horarios):
    """
    Retorna el CONJUNTO de franjas en las que NINGÚN profesor tiene clase,
    es decir, las franjas en que todos pueden reunirse.

    Reglas:
      - Solo se consideran franjas de TODAS_LAS_FRANJAS.
      - Si no hay ninguna franja disponible, retorna un conjunto vacío.

    Ejemplo:
        h = {"ana": {1, 2}, "luis": {2, 9}}
        franjas_reunion(h) -> {3, 4, 5, 6, 7, 8, 10}
        # la 1 y la 2 las ocupa ana, la 9 la ocupa luis
    """

    # --- CÓDIGO ORIGINAL (comentado, no se elimina) ---
    # Motivo: excluía a un docente en cada vuelta (el resultado dependía solo
    # del último), imprimía en vez de retornar, y la variable
    # horas_disponibles podía no existir si "horarios" estaba vacío.
    # La operación (unión + resta con TODAS_LAS_FRANJAS) era la correcta.
    #
    # for docente, horas in horarios.items():
    #     horas_reunion = set()
    #
    # for otro_docente, otros in horarios.items():
    #
    #     if otro_docente!= docente:
    #         horas_reunion = horas_reunion | otros
    #
    #     horas_disponibles = TODAS_LAS_FRANJAS - horas_reunion
    # if horas_disponibles:
    #         print(f"Las horas disponibles para reuniones  son {horas_disponibles}")
    # else:
    #         print(f"No hay horarios disponibles para reunion.")

    # --- CÓDIGO CORREGIDO ---
    # Unión de las franjas ocupadas por TODOS los profesores, sin excepciones.
    ocupadas = set()
    for horas in horarios.values():
        ocupadas = ocupadas | horas

    # Lo que queda libre de las 10 franjas. Si no queda nada, es set() vacío.
    return TODAS_LAS_FRANJAS - ocupadas


"""
═══════════════════════════════════════════════════════════════════════════════
                PARTE 2: INVENTARIO CON LISTAS ENLAZADAS (2.5)
═══════════════════════════════════════════════════════════════════════════════

Dos bodegas tienen productos almacenados como conjuntos con listas enlazadas.
Implementar operaciones para gestionar el inventario.
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

# PUNTO 2.1 (0.8): Productos en ambas bodegas (intersección)
def productos_en_ambas(bodega_a, bodega_b):
    """
    Retorna un NUEVO Conjunto con los productos que están en AMBAS bodegas.

    Recorrer bodega_a y agregar al resultado solo los que también
    están en bodega_b.

    Ejemplo:
        A = Conjunto(["arroz", "leche", "pan"])
        B = Conjunto(["leche", "huevos", "pan"])
        productos_en_ambas(A, B) -> {leche, pan}
    """
    # (Sin cambios: ya funcionaba correctamente.)
    pdtAmbas = Conjunto()

    actual = bodega_a.cabeza
    while actual:

        if bodega_b.pertenece(actual.dato):
                 pdtAmbas.agregar(actual.dato)

        actual = actual.siguiente

    return pdtAmbas

# PUNTO 2.2 (0.8): Productos exclusivos de una bodega (diferencia)

def productos_exclusivos(bodega_a, bodega_b):
    """
    Retorna un NUEVO Conjunto con productos que están en bodega_a
    pero NO en bodega_b.

    Ejemplo:
        A = Conjunto(["arroz", "leche", "pan"])
        B = Conjunto(["leche", "huevos", "pan"])
        productos_exclusivos(A, B) -> {arroz}
    """
    # La función diferencia estaba bien escrita y se conserva: recorre A y
    # agrega al resultado solo lo que NO pertenece a B (A - B).
    def diferencia(bodega_a, bodega_b):
            resultado = Conjunto()
            actual = bodega_a.cabeza
            while actual:
                if not bodega_b.pertenece(actual.dato):
                    resultado.agregar(actual.dato)
                actual = actual.siguiente
            return resultado

    # --- CÓDIGO ORIGINAL (comentado, no se elimina) ---
    # Motivo: "union" no se necesita (el punto pide solo A - B). Además tenía
    # un error: "actual = bodega_b.cabeza" estaba dentro del primer while,
    # así que cortaba el recorrido de A. Y el return original calculaba la
    # diferencia SIMÉTRICA y llamaba "diferencia"/"union" como métodos de
    # Conjunto, que no existen (son funciones locales) -> AttributeError.
    #
    # def union(bodega_a, bodega_b):
    #     resultado = Conjunto()
    #     actual =bodega_a.cabeza
    #     while actual:
    #         resultado.agregar(actual.dato)
    #         actual = actual.siguiente
    #         actual = bodega_b.cabeza
    #     while actual:
    #         resultado.agregar(actual.dato)
    #         actual = actual.siguiente
    #     return resultado
    # return bodega_a.diferencia(bodega_b).union(bodega_b.diferencia(bodega_a))

    # --- CÓDIGO CORREGIDO ---
    # Solo A - B: productos de A que no están en B.
    return diferencia(bodega_a, bodega_b)



# PUNTO 2.3 (0.9): Verificar si una bodega tiene todo lo de otra (subconjunto)
def bodega_contiene_todo(bodega_grande, bodega_chica):
    """
    Retorna True si bodega_grande tiene TODOS los productos de bodega_chica.
    Es decir: bodega_chica ⊆ bodega_grande

    Ejemplo:
        grande = Conjunto(["arroz", "leche", "pan", "huevos"])
        chica = Conjunto(["leche", "pan"])
        bodega_contiene_todo(grande, chica) -> True

        bodega_contiene_todo(chica, grande) -> False
    """
    # (Sin cambios: ya funcionaba correctamente.)
    actual = bodega_chica.cabeza
    while actual:

        if not bodega_grande.pertenece(actual.dato):
            return False
        actual = actual.siguiente

    return True


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":
    print("=" * 64)
    print("PARTE 1: GESTIÓN DE HORARIOS")
    print("=" * 64)

    print("\n  Horario ocupado de cada profesor:")
    for nombre, franjas in HORARIOS.items():
        print(f"    {nombre:<10} {sorted(franjas)}")

    print(f"\n  conflictos_globales(HORARIOS)")
    print(f"    -> {conflictos_globales(HORARIOS)}")

    print(f"\n  franja_mas_congestionada(HORARIOS)")
    print(f"    -> {franja_mas_congestionada(HORARIOS)}")

    print(f"\n  franjas_reunion(HORARIOS)")
    print(f"    -> {franjas_reunion(HORARIOS)}")

    print("\n" + "=" * 64)
    print("PARTE 2: INVENTARIO CON LISTAS ENLAZADAS")
    print("=" * 64)

    bodega_norte = Conjunto(["arroz", "leche", "pan", "aceite", "sal"])
    bodega_sur = Conjunto(["leche", "huevos", "pan", "azúcar", "sal"])

    print(f"\n  Bodega Norte: {bodega_norte}")
    print(f"  Bodega Sur:   {bodega_sur}")

    print(f"\n  productos_en_ambas(norte, sur)")
    print(f"    -> {productos_en_ambas(bodega_norte, bodega_sur)}")

    print(f"\n  productos_exclusivos(norte, sur)")
    print(f"    -> {productos_exclusivos(bodega_norte, bodega_sur)}")

    print(f"\n  productos_exclusivos(sur, norte)")
    print(f"    -> {productos_exclusivos(bodega_sur, bodega_norte)}")

    pedido = Conjunto(["leche", "sal"])
    print(f"\n  bodega_contiene_todo(norte, {pedido})")
    print(f"    -> {bodega_contiene_todo(bodega_norte, pedido)}")

    pedido2 = Conjunto(["leche", "huevos"])
    print(f"\n  bodega_contiene_todo(norte, {pedido2})")
    print(f"    -> {bodega_contiene_todo(bodega_norte, pedido2)}")
