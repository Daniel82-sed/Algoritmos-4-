"""
═══════════════════════════════════════════════════════════════════════════════
                    QUIZ - ANÁLISIS DE ALGORITMOS
                    Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
- Responder directamente en este archivo, donde dice ___ o TODO.
- En el punto 1 no hay que ejecutar nada: hay que LEER el código y analizarlo.
- En el punto 2 sí hay que escribir código y dejarlo funcionando.
- Permitido: diccionarios y conjuntos de Python.
- Prohibido: `sorted()`, `max()`, `min()` sobre la lista completa en el
  punto 2. La idea es que recorran ustedes.

DISTRIBUCIÓN:
   Punto 1 - Determinar la complejidad ..... 2.0
   Punto 2 - De fuerza bruta a eficiente ... 3.0
                                             ───
                                             5.0


═══════════════════════════════════════════════════════════════════════════════
PUNTO 1 (2.0): DETERMINAR LA COMPLEJIDAD
═══════════════════════════════════════════════════════════════════════════════

Para cada función, escribe su complejidad Big-O **temporal** y una
justificación corta. No basta con el resultado: la justificación es la mitad
del puntaje.

Si la complejidad depende de más de un tamaño, nómbralos (n, m, ...) y di
qué es cada uno.
"""


# ─────────────────────────────────────────────────────────────────────────────
# 1a (0.6)
# ─────────────────────────────────────────────────────────────────────────────
def resumen_ventas(ventas):
    """
    Recibe una lista de ventas del mes (asume que no está vacía).
    Retorna el total, el promedio, cuántas ventas superan el promedio
    y las 3 ventas más grandes.
    """
    total = 0
    for v in ventas: # 1n = n 
        total += v

    promedio = total / len(ventas)

    sobre_promedio = 0
    for v in ventas: # n
        if v > promedio:
            sobre_promedio += 1

    top = []
    copia = list(ventas)
    for i in range(3): # 2 (n3) = 2 3 = 6 = 1 
        mayor = copia[0]
        for c in copia:
            if c > mayor:
                mayor = c
        top.append(mayor) 
        copia.remove(mayor)

    return total, promedio, sobre_promedio, top


# Sea n = cantidad de ventas
#
# Complejidad temporal: O(n)
#
# Justificación: varios de los ciclos for estan seguidos lo que los suma ya al final daria 3n que
#es n por simplificacion aunque tiene un for doble el exterior esta limitado a un rango de entrada 
#3 lo que en si lo convierte en un constante por lo cual solo queda el n interior 



# ─────────────────────────────────────────────────────────────────────────────
# 1b (0.7)
# ─────────────────────────────────────────────────────────────────────────────
def verificar_inventario(codigos_bodega, codigos_pedido):
    """
    `codigos_bodega` es una lista YA ORDENADA con los códigos de producto
    que hay en la bodega.
    `codigos_pedido` es la lista de códigos que pide un cliente.
    Retorna cuántos códigos del pedido existen en la bodega.
    """
    encontrados = 0
    for codigo in codigos_pedido: # m
        izq = 0 # 1 
        der = len(codigos_bodega) - 1 # n
        while izq <= der:
            medio = (izq + der) // 2 # n / 2 = log 2 
            if codigos_bodega[medio] == codigo:
                encontrados += 1
                break
            elif codigos_bodega[medio] < codigo:
                izq = medio + 1
            else:
                der = medio - 1
    return encontrados


# Sea n = len(codigos_bodega) y m = len(codigos_pedido)
#
# Complejidad temporal: n + 1 + 1 + 1 + 1 + 1 * log(2)  = 5n * log n = O(n log n) = O ( m log n )
#
# Justificación: Al principio llegue a la conclucion de que era un log n por lo de que el funcionamiento
#es muy parecido a la busqueda binaria la cual es log n pero , si eso esta dentro de un for es una lineal 
# que se debe multiplica por lo de por si esta adentro asi que por eso es 
# O( n log n )



# ─────────────────────────────────────────────────────────────────────────────
# 1c (0.7)
# ─────────────────────────────────────────────────────────────────────────────
def clientes_nuevos(pedidos_hoy, clientes_antiguos):
    """
    `pedidos_hoy` es una LISTA con las cédulas de quienes pidieron hoy.
    `clientes_antiguos` es una LISTA con las cédulas de todos los clientes
    que ya habían comprado antes.
    Retorna la lista de cédulas que están comprando por primera vez.
    """
    nuevos = []
    for cedula in pedidos_hoy: # n 
        if cedula not in clientes_antiguos: # m 
            nuevos.append(cedula) # 1 
    return nuevos


# Sea n = len(pedidos_hoy) y m = len(clientes_antiguos)
#
# Complejidad temporal:  n *  ( m  + 2 ) = n * m =O(n * m)
#
# Justificación:un solo ciclo lineal con otro adentro encargado de hacer una busqueda en una lista 
# y devolver un condicional que se utiliza para llenar una nueva lista al ser un lineal dentro de 
#otro lineal se multiplica si fuera la misma variable seria O(n ^ 2) pero al ser bases separadas 
# sin posibilidad de union o simplificacion seria n * m 


"""
═══════════════════════════════════════════════════════════════════════════════
PUNTO 2 (3.0): DE FUERZA BRUTA A EFICIENTE
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
─────────
Una tienda registra el precio de un producto día por día:

    precios = [7, 1, 5, 3, 6, 4]
               ^día 0          ^día 5

Queremos saber la MAYOR GANANCIA posible comprando en un día y vendiendo en
un día POSTERIOR. No se puede vender antes de comprar.

En el ejemplo: comprar el día 1 a 1 y vender el día 4 a 6 → ganancia 5.
Esa es la mayor posible.

Si el precio solo baja (por ejemplo [9, 7, 4, 2]), la respuesta es 0:
lo mejor es no hacer el negocio.

La versión de FUERZA BRUTA ya está escrita y funciona. Es correcta, pero
lenta.
"""


def mayor_ganancia_lento(precios):
    """Fuerza bruta: prueba TODAS las parejas (compra, venta)."""
    mejor = 0
    for i in range(len(precios)):
        for j in range(i + 1, len(precios)):
            ganancia = precios[j] - precios[i]
            if ganancia > mejor:
                mejor = ganancia
    return mejor


"""
─────────────────────────────────────────────────────────────────────────────
"""


"""
─────────────────────────────────────────────────────────────────────────────
2a (1.6): ESCRIBIR LA VERSIÓN EFICIENTE
─────────────────────────────────────────────────────────────────────────────

Escribe una versión que recorra la lista UNA SOLA VEZ: O(n).

No se trata de usar un diccionario ni un conjunto. Se trata de darse cuenta
de algo sobre el problema:

    Si yo voy avanzando día por día y estoy parado en el día j,
    ¿necesito volver a mirar todos los días anteriores
    para saber cuál era el mejor día para haber comprado?
    ¿O hay UN SOLO dato del pasado que me basta recordar?

Piensa cuál es ese dato antes de escribir código.

RESTRICCIONES:
  - Un solo ciclo. Nada de ciclos anidados.
  - No usar `min()` ni `max()` sobre la lista.
  - Debe funcionar con lista vacía y con lista de un solo día (retorna 0).
"""


def mayor_ganancia_rapido(precios):
    mejor = []
    actual = 0 
    for i in range(len(precios)):
        pass
    """actual = mejor = precios[0] # int 4 
    for i , x  in enumerate(precios):
        actual = x + 1 
        ganancias = actual - precios[i]
        if ganancias > mejor :
            mejor = ganancias 

    return mejor """
    """mejor = 0 intento 3 
    for i, x in enumerate(precios):
        x = i + 1 
        ganancia = x - precios[i]
        if ganancia > mejor :
            mejor = ganancia 
    return mejor """
    """mejor = 0 # intento  2 
     
    for i in range(len(precios)):
        actual = i +  1
        ganancia = actual - i
        if ganancia > mejor:
            mejor = ganancia 
    return mejor"""

    
    """mejor = 0  # intento 1 
    for i  in range(len(precios)):
        actual = i + 1 
        ganancia = actual - precios[i] 
        if ganancia > mejor:
            mejor = ganancia
    return mejor """


    
    
   
    pass



"""
─────────────────────────────────────────────────────────────────────────────
2c (0.4): COMPLEJIDAD ESPACIAL
─────────────────────────────────────────────────────────────────────────────

Complejidad ESPACIAL de `mayor_ganancia_lento`: O(?)
Respuesta: ___

Complejidad ESPACIAL de `mayor_ganancia_rapido`: O(?)
Respuesta: ___

"""


"""
─────────────────────────────────────────────────────────────────────────────
2d (0.4): VERIFICAR Y MEDIR
─────────────────────────────────────────────────────────────────────────────

Ejecuta este archivo. El bloque de abajo comprueba que las dos versiones
dan el mismo resultado y mide cuánto tardan.

Después de correrlo, responde:

¿Cuántas veces más rápida fue tu versión con 20.000 días?
Respuesta: ___

Si duplicaras los días a 40.000, ¿cuánto esperarías que aumente el tiempo
de cada versión? (no lo midas, predícelo con la Big-O)
  - La lenta: ___
  - La rápida: ___
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import random
    import time

    print("=" * 64)
    print("PUNTO 2 - VERIFICACIÓN")
    print("=" * 64)

    casos = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([9, 7, 4, 2], 0),          # solo baja -> no hacer el negocio
        ([1, 2, 3, 4, 5], 4),       # solo sube
        ([5], 0),                   # un solo día
        ([], 0),                    # lista vacía
        ([3, 3, 3], 0),             # todo igual
        ([2, 10, 1, 9], 8),         # el mejor par NO está en los extremos
    ]

    correctos = 0
    for precios, esperado in casos:
        try:
            obtenido = mayor_ganancia_rapido(precios)
        except Exception as exc:
            obtenido = f"error: {type(exc).__name__}"
        ok = obtenido == esperado
        correctos += ok
        print(f"   {'OK ' if ok else 'MAL'}  {str(precios):<22} obtuvo={obtenido}")

    print(f"\n   {correctos}/{len(casos)} casos correctos")

    print("\n" + "=" * 64)
    print("MEDICIÓN")
    print("=" * 64)

    for n in (2000, 5000, 20000):
        datos = [random.randint(1, 1000) for _ in range(n)]

        inicio = time.perf_counter()
        r_lento = mayor_ganancia_lento(datos)
        t_lento = time.perf_counter() - inicio

        inicio = time.perf_counter()
        r_rapido = mayor_ganancia_rapido(datos)
        t_rapido = time.perf_counter() - inicio

        iguales = "sí" if r_lento == r_rapido else "NO (revisa tu código)"
        veces = f"{t_lento / t_rapido:.0f}x" if t_rapido > 0 else "—"

        print(f"\n   n = {n}")
        print(f"      lenta:  {t_lento:.4f} s")
        print(f"      rápida: {t_rapido:.6f} s")
        print(f"      ¿mismo resultado? {iguales}")
        print(f"      la rápida fue {veces} más rápida")
