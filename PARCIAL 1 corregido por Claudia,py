"""
═══════════════════════════════════════════════════════════════════════════════
        PARCIAL ALGORITMOS Y PROGRAMACIÓN 4 - REGEX + LISTA RECURSIVA + CONJUNTOS
═══════════════════════════════════════════════════════════════════════════════

ÍNDICE DE BÚSQUEDA RÁPIDA (usa Ctrl+F con el texto entre corchetes)
───────────────────────────────────────────────────────────────────────────────
[PUNTO_1_1_CORREO]            Validar correo institucional (regex + fullmatch).
[PUNTO_1_2_MENCIONES]         Extraer menciones tipo @usuario (regex + findall).
[CLASE_PEDIDO]                Nodo de la lista enlazada de pedidos.
[CLASE_LISTA_PEDIDOS]         Lista enlazada con cabeza.
[PUNTO_2_1_AGREGAR]           Inserción ordenada recursiva (tiempo MENOR primero).
[PATRON_INSERTAR_RECURSIVO]   Auxiliar reutilizable: insertar ordenado.
[PUNTO_2_2_RETRASO]           Contar pedidos en retraso (recursivo).
[PATRON_CONTAR_RECURSIVO]     Auxiliar reutilizable: contar con condición.
[PUNTO_2_3_FILTRAR]           Filtrar por cliente -> lista NUEVA (recursivo).
[PATRON_FILTRAR_RECURSIVO]    Auxiliar reutilizable: filtrar copiando nodos.
[PUNTO_3_1_COMUN]             Intersección de tres conjuntos.
[PUNTO_3_2_RECOMENDAR]        Unión menos un conjunto.
[PUNTO_3_3_EXCLUSIVAS]        Diferencia de cada conjunto contra la unión de los otros.
[PRUEBAS]                     Bloque de pruebas con resultados esperados.

NOTA SOBRE EL ENUNCIADO (copiado desde el PDF):
El PDF traía dos problemas de formato/código que se corrigieron SIN cambiar lo
que pide el enunciado. Están marcados en el código con "CORRECCIÓN DEL BASE":
  1) __str__ usaba self.ingredientes_str (atributo que NO existe) -> error al
     mostrar un pedido. Debe ser la variable local ingredientes_str.
  2) La indentación del PDF estaba rota (el "# TODO" quedaba más metido que el
     docstring y filtrar_por_cliente quedaba anidada dentro de otro método).
     Python lo rechaza, así que se dejó cada método a 4 espacios.
"""

import re


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 1: EXPRESIONES REGULARES (20%)
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# [PUNTO_1_1_CORREO] Validar correo institucional
# ───────────────────────────────────────────────────────────────────────────────
def validar_correo_institucional(correo):
    """
    Valida si un correo es institucional del Politécnico.

    Formato válido: nombre.apellido@elpoli.edu.co
    - nombre y apellido solo letras minúsculas (mínimo 2 cada uno)
    - separados por punto
    - dominio exacto: @elpoli.edu.co

    Ejemplos:
      validar_correo_institucional("juan.perez@elpoli.edu.co") -> True
      validar_correo_institucional("j.perez@elpoli.edu.co") -> False (nombre muy corto)
      validar_correo_institucional("juan.perez@gmail.com") -> False
      validar_correo_institucional("Juan.Perez@elpoli.edu.co") -> False (mayúsculas)

    Recibe:   correo (str).
    Devuelve: True si TODO el texto cumple el formato, False en caso contrario
              (también False si no es un str, para no romper con TypeError).

    Reutilizable: cualquier validación de "formato exacto" (cédula, placa,
    código de curso...). Se cambia solo el patrón.
    """
    # Un valor que no es texto (None, número...) hace que re lance TypeError.
    # Para una función de validación lo natural es responder "no es válido".
    if not isinstance(correo, str):
        return False

    # PATRÓN, pieza por pieza:
    #   [a-z]{2,}      nombre: SOLO minúsculas, 2 o más (excluye "j", "Juan", "juan2")
    #   \.             el punto literal (sin la barra, "." significaría "cualquier
    #                  carácter" y "juan_perez" también pasaría)
    #   [a-z]{2,}      apellido: mismas reglas que el nombre
    #   @              la arroba literal
    #   elpoli\.edu\.co  dominio EXACTO; cada punto escapado por la misma razón
    #
    # POR QUÉ re.fullmatch: exige que el patrón cubra TODA la cadena.
    #   - re.match solo ancla al INICIO: "juan.perez@elpoli.edu.com" también
    #     daría True porque "...edu.co" coincide al comienzo.
    #   - re.match con "$" al final casi sirve, pero "$" acepta un salto de línea
    #     final ("juan.perez@elpoli.edu.co\n" pasaría). fullmatch no.
    #   (re guarda en caché los patrones ya compilados, así que llamar a
    #   re.fullmatch muchas veces no recompila el patrón cada vez.)
    patron = r"[a-z]{2,}\.[a-z]{2,}@elpoli\.edu\.co"
    return re.fullmatch(patron, correo) is not None


# ───────────────────────────────────────────────────────────────────────────────
# [PUNTO_1_2_MENCIONES] Extraer menciones de usuario
# ───────────────────────────────────────────────────────────────────────────────
def extraer_menciones(texto):
    """
    Extrae todas las menciones de usuario de un texto (estilo Twitter/X).
    Una mención empieza con @ seguido de letras, números o guion bajo.

    Ejemplo:
      extraer_menciones("Hola @juan_dev y @maria99, miren esto @python")
      -> ["@juan_dev", "@maria99", "@python"]

    Recibe:   texto (str).
    Devuelve: lista de str con cada mención (incluye la "@"), en el orden en
              que aparecen. Lista vacía si no hay menciones.

    Reutilizable: cualquier "extraer todos los X de un texto" (hashtags con
    r"#\\w+", números con r"\\d+", etc.). findall devuelve TODAS las coincidencias.
    """
    # PATRÓN:
    #   @     la arroba literal que inicia la mención
    #   \w+   uno o más caracteres "de palabra": letras, dígitos y guion bajo
    #         (justo lo que pide el enunciado). Como "," o " " NO son \w, la
    #         mención se corta sola en "@maria99," -> "@maria99" (sin la coma).
    #   El "+" exige al menos un carácter: una "@" suelta no cuenta.
    #
    # findall devuelve una lista de str porque el patrón NO tiene grupos ( ).
    # Si tuviera grupos, devolvería solo lo capturado por el grupo, no la
    # coincidencia completa (error muy común en exámenes).
    #
    # Detalle: \w en Python 3 también acepta letras con tilde y ñ ("@josé"
    # sale completo). Si solo quisieras ASCII, usa [A-Za-z0-9_]+ .
    return re.findall(r"@\w+", texto)


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 2: LISTA ENLAZADA DE PEDIDOS - RECURSIVIDAD (40%)
# ═══════════════════════════════════════════════════════════════════════════════
"""
CONTEXTO DEL PROBLEMA:
Un restaurante necesita gestionar los pedidos que llegan a la cocina.
Cada pedido tiene:
  • cliente: nombre de quien pidió
  • mesa: número de mesa
  • tiempo_estimado: minutos que tarda en prepararse (1-30)
  • estado: 'pendiente', 'preparando', 'listo'
  • ingredientes: lista de ingredientes principales

Los PEDIDOS DEBEN ESTAR ORDENADOS por tiempo estimado (MENOR primero):
  Si llega pedido con tiempo 20 y hay pedidos [5, 10, 30] -> [5, 10, 20, 30]

IDEA CLAVE DE LA RECURSIVIDAD EN LISTAS ENLAZADAS (para el examen):
Toda función recursiva sobre una lista tiene SIEMPRE dos partes:
  1) CASO BASE:      el nodo es None (llegamos al final de la lista).
  2) CASO RECURSIVO: se procesa el nodo actual y se llama a la función con
                     nodo.siguiente (la "lista más corta" que queda).
Como el método público no recibe el nodo (el enunciado fija su firma), se usa
el patrón WRAPPER + AUXILIAR: el público solo arranca con self.cabeza y el
auxiliar "_rec" (con prefijo _) hace la recursión de verdad.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# [CLASE_PEDIDO] Nodo de la lista enlazada
# ═══════════════════════════════════════════════════════════════════════════════

class Pedido:
    """Representa un pedido en el restaurante (y a la vez un NODO de la lista)."""

    def __init__(self, cliente, mesa, tiempo_estimado, ingredientes=None,
                 estado="pendiente"):
        self.cliente = cliente                  # str: quién pidió
        self.mesa = mesa                        # int: número de mesa
        self.tiempo_estimado = tiempo_estimado  # int: minutos (1-30)
        self.estado = estado                    # str: 'pendiente', 'preparando', 'listo'
        self.ingredientes = ingredientes if ingredientes else []  # list de str
        self.siguiente = None                   # Pedido o None: siguiente nodo

    def __str__(self):
        # Símbolo según estado (el PDF traía esta línea partida en varias; se
        # junta en una sola para que Python la entienda).
        simbolo = "⏳" if self.estado == "pendiente" else "👨‍🍳" if self.estado == "preparando" else "✓"

        ingredientes_str = ", ".join(self.ingredientes) if self.ingredientes else "sin especificar"

        # CORRECCIÓN DEL BASE: el original decía {self.ingredientes_str}, pero
        # "ingredientes_str" es una variable LOCAL, no un atributo del objeto:
        # eso lanzaba AttributeError al imprimir cualquier pedido.
        # return f"[{simbolo}] Mesa {self.mesa} ({self.cliente}) - {self.tiempo_estimado}min - {self.ingredientes_str} ({self.estado})"
        return f"[{simbolo}] Mesa {self.mesa} ({self.cliente}) - {self.tiempo_estimado}min - {ingredientes_str} ({self.estado})"


# ═══════════════════════════════════════════════════════════════════════════════
# [CLASE_LISTA_PEDIDOS] Lista enlazada de pedidos
# ═══════════════════════════════════════════════════════════════════════════════

class ListaPedidos:
    """Gestiona la cola de pedidos en lista enlazada"""

    def __init__(self):
        self.cabeza = None  # primer nodo; None significa lista vacía

    def mostrar(self):
        """Muestra todos los pedidos en la cola"""
        # Recorrido ITERATIVO (código base): avanza con "actual" hasta None.
        actual = self.cabeza
        if actual is None:
            print(" 🍽️ No hay pedidos en la cola")
            return

        print(" 📋 PEDIDOS EN COLA:")
        while actual:
            print(f"    {actual}")
            actual = actual.siguiente

    # ───────────────────────────────────────────────────────────────────────
    # [PUNTO_2_1_AGREGAR] MÉTODO 1: Agregar pedido ORDENADO - RECURSIVO
    # ───────────────────────────────────────────────────────────────────────
    def agregar(self, cliente, mesa, tiempo_estimado, ingredientes=None):
        """
        Agrega un NUEVO PEDIDO ordenado por tiempo_estimado (MENOR primero).

        Los pedidos se ordenan por urgencia:
        - Tiempo MENOR = más urgente (va primero)
        - Tiempo MAYOR = menos urgente (va después)

        Si dos pedidos tienen el MISMO tiempo, el nuevo va DESPUÉS del existente.

        OBLIGATORIO usar RECURSIVIDAD.
          EJEMPLO:
              Cola actual: [10 min, 15 min, 30 min]
              Agregar: 5 min -> Nueva cola: [5, 10, 15, 30]
              Agregar: 12 min -> Nueva cola: [5, 10, 12, 15, 30]
              Agregar: 15 min -> Nueva cola: [5, 10, 12, 15, 15, 30]

          PARÁMETROS:
              cliente (str): nombre del cliente
              mesa (int): número de mesa
              tiempo_estimado (int): minutos de preparación (1-30)
              ingredientes (list): lista de ingredientes [opcional]

        Devuelve: nada; modifica la lista (self.cabeza).
        Lanza:    ValueError si tiempo_estimado no está entre 1 y 30.

        Reutilizable: cualquier "lista enlazada ordenada". Para orden de mayor
        a menor, o por otro campo, solo cambia la comparación en
        _insertar_ordenado.
        """
        # El enunciado define el rango 1-30; se valida ANTES de crear el nodo
        # para que un dato inválido nunca deje la lista a medias.
        if not 1 <= tiempo_estimado <= 30:
            raise ValueError("El tiempo estimado debe estar entre 1 y 30 minutos")

        nuevo = Pedido(cliente, mesa, tiempo_estimado, ingredientes)

        # La recursión DEVUELVE la nueva cabeza y siempre se reasigna: si el
        # nuevo queda de primero la cabeza cambia; si no, es la misma de antes.
        self.cabeza = self._insertar_ordenado(self.cabeza, nuevo)

    # [PATRON_INSERTAR_RECURSIVO]
    def _insertar_ordenado(self, nodo, nuevo):
        """
        Inserta "nuevo" en la sublista que empieza en "nodo" y devuelve la
        cabeza de esa sublista ya actualizada.

        Parámetros:
            nodo  -> Pedido o None: primer nodo de la sublista actual.
            nuevo -> Pedido: el nodo que se quiere insertar.

        CASO BASE:  nodo es None (fin de la lista) O el nuevo es MÁS RÁPIDO
                    (tiempo menor) que el nodo actual -> aquí va el nuevo.
        RECURSIVO:  el nodo actual es igual o más rápido -> el nuevo va más
                    adelante: se inserta en nodo.siguiente y se reconecta.

        Por qué "<" estricto: con tiempos IGUALES no se cumple el caso base, se
        sigue avanzando y el nuevo queda DESPUÉS del existente (lo que pide
        el enunciado). Con "<=" quedaría ANTES: error típico.

        Ejemplo: [10, 15, 30], insertar 12
          nodo=10: 12 < 10? No -> 10.siguiente = insertar(nodo=15, ...)
          nodo=15: 12 < 15? Sí -> nuevo.siguiente = 15; devuelve nuevo(12)
          nodo=10 recibe 12 como su siguiente; devuelve 10
          Resultado: [10, 12, 15, 30]

        (Es la misma función del ejercicio de pacientes: allí era ">" porque
        la urgencia mayor iba primero; aquí es "<" porque el tiempo menor va
        primero. Solo se invierte la comparación.)
        """
        # CASO BASE: final de la lista o posición correcta encontrada.
        if nodo is None or nuevo.tiempo_estimado < nodo.tiempo_estimado:
            nuevo.siguiente = nodo   # el nuevo apunta al resto de la lista
            return nuevo             # y pasa a ser la cabeza de esta sublista

        # CASO RECURSIVO: se reconecta porque la sublista siguiente puede
        # tener una cabeza nueva (el nodo recién insertado).
        nodo.siguiente = self._insertar_ordenado(nodo.siguiente, nuevo)
        return nodo

    # ───────────────────────────────────────────────────────────────────────
    # [PUNTO_2_2_RETRASO] MÉTODO 2: Contar pedidos en retraso - RECURSIVO
    # ───────────────────────────────────────────────────────────────────────
    # CÓMO USAR: lista.contar_en_retraso()  -> int
    #   contar_en_retraso(self)        = WRAPPER: lo llamas tú; solo arranca.
    #   _contar_en_retraso_rec(nodo)   = AUXILIAR: hace el conteo real.
    def contar_en_retraso(self):
        """
        Cuenta los pedidos que están en RETRASO:

          Un pedido está en RETRASO si:
            - Su estado es 'pendiente' O 'preparando'
            - Y su tiempo_estimado es > 20 minutos

          (Los pedidos largos que aún no se han servido son prioritarios)

          OBLIGATORIO usar RECURSIVIDAD.

          EJEMPLO:
              Pedido 1: 25 min, estado 'pendiente'      ✓ cuenta (>20, no listo)
              Pedido 2: 18 min, estado 'pendiente'      ✗ no cuenta (<= 20)
              Pedido 3: 25 min, estado 'listo'          ✗ no cuenta (ya está listo)
              Pedido 4: 22 min, estado 'preparando'     ✓ cuenta (>20, en progreso)

              Retorna: 2

          RETORNA:
              int: cantidad de pedidos en retraso (0 si la lista está vacía)

        Reutilizable: "contar los nodos que cumplen una condición". Para otro
        ejercicio cambia SOLO la condición de _contar_en_retraso_rec.
        """
        return self._contar_en_retraso_rec(self.cabeza)

    # [PATRON_CONTAR_RECURSIVO]
    def _contar_en_retraso_rec(self, nodo):
        """
        Cuenta, desde "nodo" hasta el final, los pedidos en retraso.

        CASO BASE:  nodo es None -> no quedan pedidos -> 0.
        RECURSIVO:  (1 si el nodo actual cumple, 0 si no) + lo que cuente el
                    resto de la lista.

        Ejemplo: (25,pendiente) -> (18,pendiente) -> (25,listo) -> (22,preparando)
          cuenta(25,pend) = 1 + cuenta(18,pend)
          cuenta(18,pend) = 0 + cuenta(25,listo)     (18 no es > 20)
          cuenta(25,listo)= 0 + cuenta(22,prep)      (ya está listo)
          cuenta(22,prep) = 1 + cuenta(None)
          cuenta(None)    = 0
          Se resuelve de atrás hacia adelante: 1 + (0 + (0 + (1 + 0))) = 2
        """
        # CASO BASE: fin de la lista.
        if nodo is None:
            return 0

        # Condición del problema (se evalúa solo en el nodo actual):
        #   - "in (...)" evita escribir dos comparaciones con "or" y deja claro
        #     que "listo" (y cualquier otro estado) queda excluido.
        #   - "> 20" ESTRICTO: un pedido de exactamente 20 min NO cuenta.
        en_retraso = nodo.estado in ("pendiente", "preparando") and nodo.tiempo_estimado > 20
        suma = 1 if en_retraso else 0

        # CASO RECURSIVO: resultado del nodo actual + el del resto de la lista.
        return suma + self._contar_en_retraso_rec(nodo.siguiente)

    # ───────────────────────────────────────────────────────────────────────
    # [PUNTO_2_3_FILTRAR] MÉTODO 3: Filtrar por cliente - RECURSIVO
    # ───────────────────────────────────────────────────────────────────────
    # CÓMO USAR: juan = lista.filtrar_por_cliente("Juan")  -> ListaPedidos NUEVA
    #   filtrar_por_cliente(self, nombre)        = WRAPPER: crea la lista
    #                                              resultado y le asigna la cabeza.
    #   _filtrar_por_cliente_rec(nodo, nombre)   = AUXILIAR: construye los nodos.
    #
    # CORRECCIÓN DEL BASE: en el PDF esta función aparecía con 8 espacios de
    # indentación (anidada dentro de contar_en_retraso, así que nunca existía
    # como método de la clase). Debe ir a 4 espacios, como los demás métodos.
    def filtrar_por_cliente(self, nombre_cliente):
        """
        Retorna una NUEVA ListaPedidos con solo los pedidos de UN CLIENTE.

        NO modifica la lista original.

        OBLIGATORIO usar RECURSIVIDAD.

        EJEMPLO:
            Lista original: [Mesa 1 (Juan), Mesa 2 (María), Mesa 3 (Juan), Mesa 4 (Carlos)]
            filtrar_por_cliente("Juan")
            -> Nueva lista: [Mesa 1 (Juan), Mesa 3 (Juan)]

        PARÁMETROS:
            nombre_cliente (str): nombre del cliente a buscar

        RETORNA:
            ListaPedidos: nueva lista con solo los pedidos del cliente
            (puede quedar vacía). Conserva el orden relativo de la original,
            así que sigue ordenada por tiempo.

        Reutilizable: "filtrar una lista enlazada sin modificarla". Para otro
        criterio (por mesa, por estado...) cambia la condición en el auxiliar.
        """
        resultado = ListaPedidos()
        # La recursión devuelve la cabeza de la lista filtrada ya armada.
        resultado.cabeza = self._filtrar_por_cliente_rec(self.cabeza, nombre_cliente)
        return resultado

    # [PATRON_FILTRAR_RECURSIVO]
    def _filtrar_por_cliente_rec(self, nodo, nombre_cliente):
        """
        Devuelve la cabeza de una lista NUEVA con los pedidos de la sublista
        que empieza en "nodo" cuyo cliente es "nombre_cliente".

        Se construye "de atrás hacia adelante": primero se resuelve el resto y
        luego se decide si el nodo actual se antepone o no. Así NO hace falta
        recorrer la lista nueva para encontrar su final: cada nodo se visita
        una sola vez (O(n) en vez de O(n²)).

        CASO BASE:  nodo es None -> lista filtrada vacía -> None.
        RECURSIVO:  1) resto = filtrado del resto de la lista.
                    2) Si el nodo cumple: se crea una COPIA, se engancha al
                       resto y se devuelve como nueva cabeza.
                    3) Si no cumple: se devuelve el resto tal cual.

        Por qué se COPIA el nodo: si se reutilizara el mismo objeto, cambiar su
        "siguiente" rompería la lista ORIGINAL (el enunciado lo prohíbe).
        Por qué list(nodo.ingredientes): "ingredientes" es una lista (mutable);
        sin copiarla, original y copia compartirían la misma lista y editar los
        ingredientes de una cambiaría la otra.

        Ejemplo: clientes Juan -> María -> Juan, filtrar "Juan"
          filtrar(Juan1) -> resto = filtrar(María)
          filtrar(María) -> resto = filtrar(Juan2)
          filtrar(Juan2) -> resto = None; cumple -> copia(Juan2) -> None
          filtrar(María) -> no cumple -> devuelve copia(Juan2)
          filtrar(Juan1) -> cumple -> copia(Juan1) -> copia(Juan2)
          Resultado: Juan1 -> Juan2

        Nota: la comparación "==" distingue mayúsculas ("juan" != "Juan"). El
        enunciado no dice lo contrario, así que no se asume nada más.
        """
        # CASO BASE: fin de la lista.
        if nodo is None:
            return None

        # Primero se resuelve todo lo que viene después.
        resto = self._filtrar_por_cliente_rec(nodo.siguiente, nombre_cliente)

        if nodo.cliente == nombre_cliente:
            # Copia independiente (conserva estado y tiempo del original).
            copia = Pedido(nodo.cliente, nodo.mesa, nodo.tiempo_estimado,
                           list(nodo.ingredientes), nodo.estado)
            copia.siguiente = resto   # la copia apunta al resto ya filtrado
            return copia

        # El nodo no cumple: se descarta y se devuelve solo el resto.
        return resto


# ═══════════════════════════════════════════════════════════════════════════════
# PARTE 3: OPERACIONES DE CONJUNTOS (30%)
# ═══════════════════════════════════════════════════════════════════════════════
"""
Una plataforma de streaming tiene datos de qué películas vieron 3 usuarios.
Responde las preguntas usando operaciones de conjuntos.

TABLA DE OPERADORES (lo que más se pregunta en examen):
    a & b   intersección  -> elementos en AMBOS
    a | b   unión         -> elementos en AL MENOS UNO
    a - b   diferencia    -> elementos de a que NO están en b
    a ^ b   dif. simétrica-> elementos en UNO SOLO de los dos
"""

peliculas_juan = {"Inception", "Matrix", "Interstellar", "Avengers", "Dune"}
peliculas_maria = {"Matrix", "Avengers", "Titanic", "Dune", "Coco"}
peliculas_pedro = {"Inception", "Titanic", "Coco", "Matrix", "Parasite"}


# ───────────────────────────────────────────────────────────────────────────────
# [PUNTO_3_1_COMUN] Películas que vieron los tres
# ───────────────────────────────────────────────────────────────────────────────
def peliculas_en_comun():
    """
    Retorna el conjunto de películas que los TRES usuarios han visto.
    (Intersección de los tres)

    Resultado con los datos del examen: {"Matrix"}
    """
    # "&" deja solo lo que está en los tres a la vez. Se encadena porque
    # (juan & maria) ya es un conjunto y se vuelve a intersectar con pedro.
    return peliculas_juan & peliculas_maria & peliculas_pedro


# ───────────────────────────────────────────────────────────────────────────────
# [PUNTO_3_2_RECOMENDAR] Películas que Juan no ha visto pero otros sí
# ───────────────────────────────────────────────────────────────────────────────
def recomendar_a_juan():
    """
    Retorna películas que María o Pedro vieron pero Juan NO.
    (Películas que Juan no ha visto pero otros sí)

    Esperado: {"Titanic", "Coco", "Parasite"}
    """
    # Paso 1: (maria | pedro) = todo lo que ve AL MENOS UNO de los dos
    #         (la palabra "o" del enunciado = unión).
    # Paso 2: "- peliculas_juan" quita lo que Juan ya vio ("pero Juan NO").
    # Los paréntesis son obligatorios: sin ellos "-" se evalúa antes que "|"
    # y el resultado sería otro (error típico).
    return (peliculas_maria | peliculas_pedro) - peliculas_juan


# ───────────────────────────────────────────────────────────────────────────────
# [PUNTO_3_3_EXCLUSIVAS] Películas que solo vio cada usuario
# ───────────────────────────────────────────────────────────────────────────────
def exclusivas_de_cada_uno():
    """
    Retorna un diccionario con las películas que SOLO vio cada usuario
    (que ninguno de los otros dos vio).

    Ejemplo de retorno:
      {
         "Juan": {"Interstellar"},
         "María": set(),
         "Pedro": {"Parasite"}
      }
    """
    # Para cada usuario: sus películas MENOS la unión de las de los otros dos.
    # Ejemplo con Juan: peliculas_juan - (maria | pedro)
    #   Inception -> la vio Pedro (se quita); Matrix -> la ven todos (se quita);
    #   Avengers y Dune -> las vio María (se quitan); Interstellar -> nadie
    #   más la vio -> QUEDA.
    #
    # María devuelve set() VACÍO (no None ni se omite): el ejemplo del
    # enunciado pide que aparezca con conjunto vacío.
    #
    # PARA ADAPTAR a N usuarios (si el examen te da un diccionario):
    #   for nombre, vistas in usuarios.items():
    #       otros = set().union(*(v for n, v in usuarios.items() if n != nombre))
    #       resultado[nombre] = vistas - otros
    return {
        "Juan": peliculas_juan - (peliculas_maria | peliculas_pedro),
        "María": peliculas_maria - (peliculas_juan | peliculas_pedro),
        "Pedro": peliculas_pedro - (peliculas_juan | peliculas_maria),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# [PRUEBAS] Código de prueba con resultados esperados
# ═══════════════════════════════════════════════════════════════════════════════

def _tiempos(lista):
    """Auxiliar SOLO para pruebas: devuelve los tiempos de la lista en orden."""
    resultado = []
    actual = lista.cabeza
    while actual:
        resultado.append(actual.tiempo_estimado)
        actual = actual.siguiente
    return resultado


def _clientes(lista):
    """Auxiliar SOLO para pruebas: devuelve los clientes de la lista en orden."""
    resultado = []
    actual = lista.cabeza
    while actual:
        resultado.append(actual.cliente)
        actual = actual.siguiente
    return resultado


if __name__ == "__main__":
    print("=" * 64)
    print("PARTE 1: EXPRESIONES REGULARES")
    print("=" * 64)
    casos_correo = [
        ("juan.perez@elpoli.edu.co", True),
        ("j.perez@elpoli.edu.co", False),        # nombre muy corto
        ("juan.perez@gmail.com", False),         # dominio incorrecto
        ("Juan.Perez@elpoli.edu.co", False),     # mayúsculas
        ("juan.perez@elpoli.edu.com", False),    # dominio más largo
        ("juan.perez@elpoli.edu.co\n", False),   # salto de línea final
        ("juan.perez@elpoliXedu.co", False),     # punto sin escapar aceptaría esto
        ("juan2.perez@elpoli.edu.co", False),    # número en el nombre
        ("juan.perez.lopez@elpoli.edu.co", False),
        ("", False),
        (None, False),                           # no es texto
    ]
    for correo, esperado in casos_correo:
        obtenido = validar_correo_institucional(correo)
        print(f"  {str(correo)!r:<38} -> {obtenido}")
        assert obtenido == esperado, f"falló con {correo!r}"

    menciones = extraer_menciones("Hola @juan_dev y @maria99, miren esto @python")
    print(f"\n  extraer_menciones(ejemplo) -> {menciones}")
    assert menciones == ["@juan_dev", "@maria99", "@python"]
    assert extraer_menciones("sin menciones aquí") == []
    assert extraer_menciones("") == []
    assert extraer_menciones("solo una @ suelta") == []

    print("\n" + "=" * 64)
    print("PARTE 2.1: agregar() ordenado por tiempo")
    print("=" * 64)
    cola = ListaPedidos()
    cola.agregar("A", 1, 10)
    cola.agregar("B", 2, 15)
    cola.agregar("C", 3, 30)
    cola.agregar("D", 4, 5)                  # va de primero
    cola.agregar("E", 5, 12)                 # entre 10 y 15
    cola.agregar("F", 6, 15, ["pollo", "arroz"])  # igual que B -> va DESPUÉS de B
    cola.mostrar()
    assert _tiempos(cola) == [5, 10, 12, 15, 15, 30]
    assert _clientes(cola) == ["D", "A", "E", "B", "F", "C"]   # B antes que F
    assert ListaPedidos().cabeza is None
    for t in (0, 31, -5):
        try:
            cola.agregar("X", 9, t)
            raise AssertionError(f"no lanzó error con tiempo {t}")
        except ValueError:
            pass
    assert _tiempos(cola) == [5, 10, 12, 15, 15, 30]          # intacta

    print("\n" + "=" * 64)
    print("PARTE 2.2: contar_en_retraso()")
    print("=" * 64)
    retraso = ListaPedidos()
    retraso.agregar("P1", 1, 25)             # pendiente  -> cuenta
    retraso.agregar("P2", 2, 18)             # 18 <= 20   -> no
    retraso.agregar("P3", 3, 25)             # se pondrá listo -> no
    retraso.agregar("P4", 4, 22)             # se pondrá preparando -> cuenta
    retraso.agregar("P5", 5, 20)             # exactamente 20 -> no (es > 20)
    actual = retraso.cabeza
    while actual:                            # ajustar estados de prueba
        if actual.cliente == "P3":
            actual.estado = "listo"
        if actual.cliente == "P4":
            actual.estado = "preparando"
        actual = actual.siguiente
    print(f"  En retraso: {retraso.contar_en_retraso()}")
    assert retraso.contar_en_retraso() == 2
    assert ListaPedidos().contar_en_retraso() == 0

    print("\n" + "=" * 64)
    print("PARTE 2.3: filtrar_por_cliente()")
    print("=" * 64)
    mesas = ListaPedidos()
    mesas.agregar("Juan", 1, 10, ["pasta"])
    mesas.agregar("María", 2, 12)
    mesas.agregar("Juan", 3, 14)
    mesas.agregar("Carlos", 4, 16)
    filtrada = mesas.filtrar_por_cliente("Juan")
    print("  Filtrada (Juan):")
    filtrada.mostrar()
    print("  Original (debe seguir completa):")
    mesas.mostrar()
    assert _clientes(filtrada) == ["Juan", "Juan"]
    assert _clientes(mesas) == ["Juan", "María", "Juan", "Carlos"]
    assert filtrada.cabeza is not mesas.cabeza                 # son copias
    filtrada.cabeza.ingredientes.append("queso")               # editar la copia...
    assert mesas.cabeza.ingredientes == ["pasta"]              # ...no toca el original
    assert _clientes(mesas.filtrar_por_cliente("Nadie")) == []
    assert _clientes(ListaPedidos().filtrar_por_cliente("Juan")) == []

    print("\n" + "=" * 64)
    print("PARTE 3: CONJUNTOS")
    print("=" * 64)
    print(f"  peliculas_en_comun()      -> {peliculas_en_comun()}")
    print(f"  recomendar_a_juan()       -> {recomendar_a_juan()}")
    print(f"  exclusivas_de_cada_uno()  -> {exclusivas_de_cada_uno()}")
    assert peliculas_en_comun() == {"Matrix"}
    assert recomendar_a_juan() == {"Titanic", "Coco", "Parasite"}
    assert exclusivas_de_cada_uno() == {
        "Juan": {"Interstellar"}, "María": set(), "Pedro": {"Parasite"}
    }

    print("\n✔ Todas las pruebas pasaron")