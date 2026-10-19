"""
═══════════════════════════════════════════════════════════════════════════════
            GESTIÓN DE PACIENTES EN URGENCIAS (LISTA ENLAZADA + RECURSIVIDAD)
═══════════════════════════════════════════════════════════════════════════════

Sistema de gestión de pacientes en urgencias.
Cada paciente tiene: nombre, edad, nivel de urgencia (1-5) y si fue atendido.
Los pacientes se almacenan en una lista enlazada.

───────────────────────────────────────────────────────────────────────────────
ÍNDICE DE BÚSQUEDA RÁPIDA (usa Ctrl+F con el texto entre corchetes)
───────────────────────────────────────────────────────────────────────────────
[CLASE_PACIENTE]              Nodo de la lista (datos + puntero "siguiente").
[CLASE_LISTA]                 Lista enlazada con cabeza.
[PUNTO_1_AGREGAR]             Inserción ordenada recursiva (mayor urgencia primero).
[PATRON_INSERTAR_RECURSIVO]   Función auxiliar reutilizable: insertar ordenado.
[PUNTO_2_CONTAR]              Conteo de pacientes críticos no atendidos.
[PATRON_CONTAR_RECURSIVO]     Función auxiliar reutilizable: contar con condición.
[PUNTO_3_FILTRAR]             Filtrado por edad devolviendo una lista NUEVA.
[PATRON_FILTRAR_RECURSIVO]    Función auxiliar reutilizable: filtrar copiando nodos.
[PRUEBAS]                     Bloque de pruebas con resultados esperados.

IDEA CLAVE DE LA RECURSIVIDAD EN LISTAS ENLAZADAS (para el examen):
Toda función recursiva sobre una lista tiene SIEMPRE dos partes:
  1) CASO BASE:      el nodo es None (llegamos al final de la lista).
  2) CASO RECURSIVO: se procesa el nodo actual y se llama a la función con
                     nodo.siguiente (la "lista más corta" que queda).
Si olvidas el caso base, la recursión no termina (RecursionError).
"""


# ═══════════════════════════════════════════════════════════════════════════════
# [CLASE_PACIENTE] Nodo de la lista enlazada
# ═══════════════════════════════════════════════════════════════════════════════

class Paciente:
    """
    Nodo de la lista enlazada. Guarda los datos del paciente y el enlace
    al siguiente nodo.

    Reutilizable: cualquier ejercicio de lista enlazada usa un nodo así
    (cambian los campos de datos, el campo "siguiente" siempre existe).
    """

    def __init__(self, nombre, edad, urgencia, atendido=False):
        self.nombre = nombre        # str: nombre del paciente
        self.edad = edad            # int: edad en años
        self.urgencia = urgencia    # int: 1=baja ... 5=crítica
        self.atendido = atendido    # bool: True si ya fue atendido
        self.siguiente = None       # Paciente o None: siguiente nodo (None = fin)

    def __str__(self):
        # ✓ si ya fue atendido, ○ si sigue esperando
        estado = "✓" if self.atendido else "○"
        return f"[{estado}] {self.nombre} (edad:{self.edad}) - Urgencia:{self.urgencia}"


# ═══════════════════════════════════════════════════════════════════════════════
# [CLASE_LISTA] Lista enlazada de pacientes
# ═══════════════════════════════════════════════════════════════════════════════

class ListaPacientes:
    def __init__(self):
        self.cabeza = None  # primer nodo; None significa lista vacía

    def mostrar(self):
        # Recorrido ITERATIVO de la lista (código base): se avanza con
        # "actual" hasta que se acaba la lista (actual = None).
        actual = self.cabeza
        if actual is None:
            print("  Sin pacientes")
            return
        while actual:
            print(f"  {actual}")
            actual = actual.siguiente

    # ───────────────────────────────────────────────────────────────────────
    # [PUNTO_1_AGREGAR] Agregar paciente ordenado por urgencia - RECURSIVO
    # ───────────────────────────────────────────────────────────────────────
    def agregar(self, nombre, edad, urgencia):
        """
        Agrega un paciente ORDENADO por urgencia (mayor urgencia primero).
        Si tienen la misma urgencia, el nuevo va después de los existentes.
        OBLIGATORIO usar recursividad.

        Ejemplo:
            Si la lista tiene urgencias [5, 3, 1] y agregas urgencia 4
            Debe quedar [5, 4, 3, 1]

        Recibe:   nombre (str), edad (int >= 0), urgencia (int entre 1 y 5).
        Devuelve: nada; modifica la lista (self.cabeza).
        Lanza:    ValueError si la urgencia no está en 1-5 o la edad es negativa.

        Reutilizable: sirve para cualquier "lista enlazada ordenada". Para
        ordenar de menor a mayor, o por otro campo, solo cambia la comparación
        dentro de _insertar_ordenado.
        """
        # Validaciones mínimas: el enunciado define urgencia 1-5; una edad
        # negativa no tiene sentido. Se valida ANTES de crear/tocar nada, así
        # un dato inválido nunca deja la lista a medias.
        if not 1 <= urgencia <= 5:
            raise ValueError("La urgencia debe estar entre 1 y 5")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")

        nuevo = Paciente(nombre, edad, urgencia)

        # La función recursiva DEVUELVE la nueva cabeza de la lista. Se
        # reasigna siempre: si el nuevo queda de primero, la cabeza cambia;
        # si no, devuelve la misma cabeza de antes.
        self.cabeza = self._insertar_ordenado(self.cabeza, nuevo)

    # [PATRON_INSERTAR_RECURSIVO]
    def _insertar_ordenado(self, nodo, nuevo):
        """
        Inserta "nuevo" en la sublista que empieza en "nodo" y devuelve la
        cabeza de esa sublista ya actualizada.

        Parámetros:
            nodo  -> Paciente o None: primer nodo de la sublista actual.
            nuevo -> Paciente: nodo que se quiere insertar.

        Lógica (caso base / caso recursivo):
          CASO BASE: nodo es None (fin de la lista) O el nuevo tiene MAYOR
                     urgencia que el nodo actual -> aquí va el nuevo:
                     se engancha delante del nodo actual y se devuelve.
          RECURSIVO: el nodo actual tiene urgencia >= la del nuevo, así que
                     el nuevo va más adelante: se inserta en la sublista
                     nodo.siguiente y se reconecta el resultado.

        Por qué ">" estricto: si la urgencia es IGUAL no se cumple el caso
        base y se sigue avanzando, así el nuevo queda DESPUÉS de los
        existentes con su misma urgencia (requisito del enunciado).

        Ejemplo: lista [5, 3, 1], insertar urgencia 4
          nodo=5: 4 > 5? No -> 5.siguiente = insertar(nodo=3, ...)
          nodo=3: 4 > 3? Sí -> nuevo.siguiente = 3; devuelve nuevo(4)
          nodo=5 recibe 4 como su siguiente; devuelve 5
          Resultado: [5, 4, 3, 1]
        """
        # CASO BASE: final de la lista o posición correcta encontrada.
        if nodo is None or nuevo.urgencia > nodo.urgencia:
            nuevo.siguiente = nodo   # el nuevo apunta al resto de la lista
            return nuevo             # el nuevo pasa a ser la cabeza de esta sublista

        # CASO RECURSIVO: el nuevo va más adelante. Se reconecta el enlace
        # porque la sublista siguiente puede tener una cabeza nueva.
        nodo.siguiente = self._insertar_ordenado(nodo.siguiente, nuevo)
        return nodo

    # ───────────────────────────────────────────────────────────────────────
    # [PUNTO_2_CONTAR] Contar pacientes críticos - RECURSIVO
    # ───────────────────────────────────────────────────────────────────────
    # ───────────────────────────────────────────────────────────────────────
    # CÓMO USAR Y ENTENDER: contar_criticos() + _contar_criticos_rec()
    # ───────────────────────────────────────────────────────────────────────
    # ¿Qué problema resuelve? Contar cuántos pacientes tienen urgencia >= 4
    # y todavía NO han sido atendidos.
    #
    # Son DOS funciones que trabajan juntas:
    #
    #   contar_criticos(self)          -> la que TÚ llamas desde afuera:
    #                                     total = lista.contar_criticos()
    #                                     No recibe parámetros y solo arranca
    #                                     la recursión pasándole la cabeza.
    #
    #   _contar_criticos_rec(self, nodo) -> la que HACE el trabajo. Nunca la
    #                                     llamas tú; la llama contar_criticos
    #                                     y ella misma. Necesita el parámetro
    #                                     "nodo" para saber en qué paciente
    #                                     está parada y poder avanzar.
    #
    # Flujo: contar_criticos -> _rec(cabeza) -> _rec(siguiente) -> ... -> _rec(None)
    # Al llegar a None (caso base) devuelve 0 y las sumas pendientes se
    # resuelven de atrás hacia adelante.
    #
    # Qué devuelve: un entero (0 si la lista está vacía o nadie cumple).
    #
    # Para REUTILIZAR en otro ejercicio ("contar nodos que cumplen algo"):
    # copia ambas funciones y cambia SOLO la condición de la línea
    # "suma = 1 if (...) else 0".
    def contar_criticos(self):#Solo hace la recepcion de datos 
        """
        Retorna la cantidad de pacientes con urgencia >= 4 que NO han sido
        atendidos.
        OBLIGATORIO usar recursividad.

        Ejemplo:
            Paciente1 (urgencia 5, no atendido) + Paciente2 (urgencia 4, atendido)
            + Paciente3 (urgencia 4, no atendido)
            -> Retorna 2

        Recibe:   nada (usa self.cabeza).
        Devuelve: int con la cantidad. Lista vacía -> 0.

        Reutilizable: "contar los nodos que cumplen una condición". Para otro
        ejercicio solo cambia la condición booleana de _contar_criticos_rec.
        """
        return self._contar_criticos_rec(self.cabeza)

    # [PATRON_CONTAR_RECURSIVO]
    def _contar_criticos_rec(self, nodo):# Hace el conteo oficial
        """
        Cuenta, desde "nodo" hasta el final, los pacientes críticos no atendidos.

        CASO BASE:     nodo es None -> no quedan pacientes -> 0.
        RECURSIVO:     (1 si el nodo actual cumple, 0 si no) + lo que
                       cuente el resto de la lista.

        Ejemplo con urgencias/atendido: (5,no) -> (4,sí) -> (4,no)
          cuenta(5,no) = 1 + cuenta(4,sí)
          cuenta(4,sí) = 0 + cuenta(4,no)     (atendido: no suma)
          cuenta(4,no) = 1 + cuenta(None)
          cuenta(None) = 0
          Se resuelve de atrás hacia adelante: 1 + (0 + (1 + 0)) = 2
        """
        # CASO BASE: fin de la lista.
        if nodo is None:
            return 0

        # Condición del problema: urgencia >= 4 Y no atendido.
        # (Se evalúa solo para el nodo actual; el resto lo cubre la recursión.)
        suma = 1 if (nodo.urgencia >= 4 and not nodo.atendido) else 0

        # CASO RECURSIVO: el resultado del nodo actual + el del resto.
        return suma + self._contar_criticos_rec(nodo.siguiente)

    # ───────────────────────────────────────────────────────────────────────
    # [PUNTO_3_FILTRAR] Filtrar por edad - RECURSIVO
    # ───────────────────────────────────────────────────────────────────────
    # ───────────────────────────────────────────────────────────────────────
    # CÓMO USAR Y ENTENDER: filtrar_mayores() + _filtrar_mayores_rec()
    # ───────────────────────────────────────────────────────────────────────
    # ¿Qué problema resuelve? Obtener una lista NUEVA solo con los pacientes
    # de edad >= edad_minima, sin tocar la lista original.
    #
    # Son DOS funciones que trabajan juntas:
    #
    #   filtrar_mayores(self, edad_minima) -> la que TÚ llamas desde afuera:
    #                                     mayores = lista.filtrar_mayores(60)
    #                                     Crea la ListaPacientes vacía del
    #                                     resultado y le asigna como cabeza lo
    #                                     que devuelva la función recursiva.
    #
    #   _filtrar_mayores_rec(self, nodo, edad_minima) -> la que HACE el trabajo.
    #                                     Recorre la lista original y construye
    #                                     los nodos de la lista nueva. Recibe
    #                                     "nodo" para avanzar paciente por
    #                                     paciente y "edad_minima" para decidir.
    #
    # Flujo: primero baja hasta el final de la lista (caso base None) y luego,
    # al regresar, decide nodo por nodo: si cumple, crea una COPIA y la
    # engancha al resto ya filtrado; si no cumple, la descarta.
    #
    # Por qué copiar: si reutilizara el mismo nodo, al cambiarle el "siguiente"
    # dañaría la lista original, y el enunciado dice que no se debe modificar.
    #
    # Qué devuelve: un objeto ListaPacientes (puede quedar vacío) que
    # conserva el orden de la original.
    #
    # Para REUTILIZAR en otro ejercicio ("filtrar sin modificar"): copia ambas
    # funciones, cambia la condición "nodo.edad >= edad_minima" y, si tu nodo
    # tiene otros campos, ajusta la creación de la copia (Paciente(...)).
    def filtrar_mayores(self, edad_minima):
        """
        Retorna una NUEVA ListaPacientes con pacientes de edad >= edad_minima.
        OBLIGATORIO usar recursividad.
        No modificar la lista original.

        Ejemplo:
            filtrar_mayores(60) -> nueva lista solo con pacientes de 60+ años

        Recibe:   edad_minima (int).
        Devuelve: ListaPacientes nueva (puede quedar vacía). Se conserva el
                  orden relativo, así que si la original estaba ordenada por
                  urgencia, la filtrada también lo está.

        Reutilizable: "filtrar una lista enlazada sin modificarla". Para otro
        criterio cambia la condición en _filtrar_mayores_rec.
        """
        resultado = ListaPacientes()
        # La recursión devuelve la cabeza de la lista filtrada ya armada.
        resultado.cabeza = self._filtrar_mayores_rec(self.cabeza, edad_minima)
        return resultado

    # [PATRON_FILTRAR_RECURSIVO]
    def _filtrar_mayores_rec(self, nodo, edad_minima):
        """
        Devuelve la cabeza de una lista NUEVA con los pacientes de la sublista
        que empieza en "nodo" cuya edad es >= edad_minima.

        Se construye "de atrás hacia adelante": primero se resuelve el resto
        de la lista y luego se decide si el nodo actual se antepone o no.
        Así NO hace falta recorrer la lista nueva para hallar su final
        (evita un bucle extra, cada nodo se visita una sola vez).

        CASO BASE:  nodo es None -> la lista filtrada está vacía -> None.
        RECURSIVO:  1) resto = filtrado del resto de la lista.
                    2) Si el nodo cumple: se crea una COPIA, se engancha al
                       resto y se devuelve la copia como nueva cabeza.
                    3) Si no cumple: se devuelve el resto tal cual.

        Por qué se COPIA el nodo: si se reutilizara el mismo objeto, cambiar
        su "siguiente" rompería la lista original (el enunciado prohíbe
        modificarla).

        Ejemplo: edades 70 -> 30 -> 65, edad_minima = 60
          filtrar(70) -> resto = filtrar(30)
          filtrar(30) -> resto = filtrar(65)
          filtrar(65) -> resto = None; 65 cumple -> copia(65) -> None
          filtrar(30) -> 30 no cumple -> devuelve copia(65)
          filtrar(70) -> 70 cumple -> copia(70) -> copia(65)
          Resultado: 70 -> 65
        """
        # CASO BASE: fin de la lista.
        if nodo is None:
            return None

        # Primero se resuelve todo lo que viene después.
        resto = self._filtrar_mayores_rec(nodo.siguiente, edad_minima)

        if nodo.edad >= edad_minima:
            # Copia independiente (conserva también el estado "atendido").
            copia = Paciente(nodo.nombre, nodo.edad, nodo.urgencia, nodo.atendido)
            copia.siguiente = resto   # la copia apunta al resto ya filtrado
            return copia

        # El nodo no cumple: se descarta y se devuelve solo el resto.
        return resto


# ═══════════════════════════════════════════════════════════════════════════════
# [PRUEBAS] Código de prueba con resultados esperados
# ═══════════════════════════════════════════════════════════════════════════════

def _nombres(lista):
    """Auxiliar SOLO para pruebas: devuelve los nombres de la lista en orden."""
    resultado = []
    actual = lista.cabeza
    while actual:
        resultado.append(actual.nombre)
        actual = actual.siguiente
    return resultado


if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBA 1: agregar() ordenado por urgencia")
    print("=" * 60)
    lista = ListaPacientes()
    lista.agregar("Ana", 70, 3)
    lista.agregar("Luis", 25, 5)
    lista.agregar("Sara", 40, 1)
    lista.agregar("Mario", 65, 4)       # debe quedar entre Luis(5) y Ana(3)
    lista.agregar("Eva", 30, 4)         # misma urgencia que Mario -> va DESPUÉS
    lista.mostrar()
    # Orden esperado: Luis(5), Mario(4), Eva(4), Ana(3), Sara(1)
    assert _nombres(lista) == ["Luis", "Mario", "Eva", "Ana", "Sara"]

    print("\n" + "=" * 60)
    print("PRUEBA 2: contar_criticos()")
    print("=" * 60)
    print(f"  Críticos sin atender: {lista.contar_criticos()}")  # 3 (Luis, Mario, Eva)
    assert lista.contar_criticos() == 3
    lista.cabeza.siguiente.atendido = True      # Mario (4) pasa a atendido
    print(f"  Tras atender a Mario: {lista.contar_criticos()}")  # 2
    assert lista.contar_criticos() == 2
    assert ListaPacientes().contar_criticos() == 0              # lista vacía

    print("\n" + "=" * 60)
    print("PRUEBA 3: filtrar_mayores(60)")
    print("=" * 60)
    mayores = lista.filtrar_mayores(60)
    print("  Filtrada:")
    mayores.mostrar()
    print("  Original (debe seguir completa):")
    lista.mostrar()
    assert _nombres(mayores) == ["Mario", "Ana"]                # 65 y 70
    assert _nombres(lista) == ["Luis", "Mario", "Eva", "Ana", "Sara"]
    assert mayores.cabeza is not lista.cabeza.siguiente         # son copias
    assert _nombres(lista.filtrar_mayores(200)) == []           # nadie cumple
    assert _nombres(ListaPacientes().filtrar_mayores(10)) == [] # lista vacía
    assert _nombres(lista.filtrar_mayores(65)) == ["Mario", "Ana"]  # 65 incluido

    print("\n" + "=" * 60)
    print("PRUEBA 4: entradas inválidas")
    print("=" * 60)
    for datos in [("X", 20, 6), ("X", 20, 0), ("X", -1, 3)]:
        try:
            lista.agregar(*datos)
            print(f"  {datos}: NO lanzó error (incorrecto)")
        except ValueError as error:
            print(f"  {datos}: ValueError -> {error}")
    assert _nombres(lista) == ["Luis", "Mario", "Eva", "Ana", "Sara"]  # intacta

    print("\n✔ Todas las pruebas pasaron")
