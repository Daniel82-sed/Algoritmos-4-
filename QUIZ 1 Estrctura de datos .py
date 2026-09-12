"""
EXAMEN 1 - Estructuras de Datos
Sistema de Inventario de Productos
"""

# ─────────────────────────────────────────────────────────────
# PUNTO 1a: Clase Nodo (Producto)
# ─────────────────────────────────────────────────────────────
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre          # nombre del producto (clave para ordenar)
        self.categoria = categoria    # categoría a la que pertenece
        self.precio = precio          # precio unitario
        self.cantidad = cantidad      # cantidad en stock
        self.siguiente = None         # enlace al siguiente nodo


# ─────────────────────────────────────────────────────────────
# PUNTO 1b: Clase Lista (Inventario)
# ─────────────────────────────────────────────────────────────
class Inventario:
    def __init__(self):
        self.inicio = None   # referencia al primer producto (el más "pequeño" alfabéticamente)

    # ────────────────────────────────────────────────────────
    # PUNTO 2: Agregar producto en orden alfabético (RECURSIVO)
    # ────────────────────────────────────────────────────────
    # Si el nombre ya existe, solo se suma la cantidad.
    # Si no existe, se inserta en la posición correcta para
    # mantener el orden alfabético.
    def agregar(self, nombre, categoria, precio, cantidad):
        self.inicio = self._agregar_recursivo(self.inicio, nombre, categoria, precio, cantidad)

    def _agregar_recursivo(self, nodo, nombre, categoria, precio, cantidad):
        # caso base 1: llegamos al final de la lista (o lista vacía) -> aquí se inserta
        if nodo is None:
            return Producto(nombre, categoria, precio, cantidad)

        # caso base 2: el producto ya existe -> solo actualizamos cantidad
        if nodo.nombre == nombre:
            nodo.cantidad += cantidad
            return nodo

        # caso base 3: el nombre nuevo va alfabéticamente antes que el nodo actual
        # -> se inserta el nuevo producto ANTES del nodo actual
        if nombre < nodo.nombre:
            nuevo = Producto(nombre, categoria, precio, cantidad)
            nuevo.siguiente = nodo
            return nuevo

        # caso recursivo: el nombre va después, seguimos buscando su lugar
        nodo.siguiente = self._agregar_recursivo(nodo.siguiente, nombre, categoria, precio, cantidad)
        return nodo

    # ────────────────────────────────────────────────────────
    # PUNTO 3: Valor total del inventario (RECURSIVO)
    # ────────────────────────────────────────────────────────
    # valor total = (precio*cantidad) del nodo actual + valor total del resto
    def valor_total(self):
        return self._valor_total_recursivo(self.inicio)

    def _valor_total_recursivo(self, nodo):
        if nodo is None:      # caso base: no hay más productos
            return 0
        return (nodo.precio * nodo.cantidad) + self._valor_total_recursivo(nodo.siguiente)

    # ────────────────────────────────────────────────────────
    # PUNTO 4: Productos con bajo stock (RECURSIVO, no modifica original)
    # ────────────────────────────────────────────────────────
    def productos_bajo_stock(self, limite):
        resultado = Inventario()
        self._bajo_stock_recursivo(self.inicio, limite, resultado)
        return resultado

    def _bajo_stock_recursivo(self, nodo, limite, resultado):
        if nodo is None:      # caso base: fin de la lista original
            return
        if nodo.cantidad < limite:
            # se agrega directo al final de la nueva lista para conservar
            # el mismo orden en que aparecen (evita re-ordenar innecesariamente)
            resultado.inicio = self._insertar_al_final(resultado.inicio, nodo)
        self._bajo_stock_recursivo(nodo.siguiente, limite, resultado)

    def _insertar_al_final(self, nodo, producto_original):
        # crea una copia del producto para no compartir referencias con la lista original
        copia = Producto(producto_original.nombre, producto_original.categoria,
                          producto_original.precio, producto_original.cantidad)
        if nodo is None:
            return copia
        nodo.siguiente = self._insertar_al_final(nodo.siguiente, producto_original)
        return nodo

    # ────────────────────────────────────────────────────────
    # PUNTO 5: Eliminar producto por nombre (RECURSIVO)
    # ────────────────────────────────────────────────────────
    # Técnica clásica: la función devuelve el nodo que debe quedar
    # en el lugar del nodo recibido (None si se elimina).
    # Se usa una lista [False] como "bandera" mutable para poder
    # saber desde afuera si realmente se eliminó algo.
    def eliminar(self, nombre):
        eliminado = [False]
        self.inicio = self._eliminar_recursivo(self.inicio, nombre, eliminado)
        return eliminado[0]

    def _eliminar_recursivo(self, nodo, nombre, eliminado):
        if nodo is None:                  # caso base: no se encontró el producto
            return None

        if nodo.nombre == nombre:
            eliminado[0] = True
            return nodo.siguiente         # se "salta" el nodo eliminado

        nodo.siguiente = self._eliminar_recursivo(nodo.siguiente, nombre, eliminado)
        return nodo

    # ────────────────────────────────────────────────────────
    # Método extra para visualizar el inventario
    # ────────────────────────────────────────────────────────
    def mostrar(self):
        if self.inicio is None:
            print("   (inventario vacío)")
            return
        self._mostrar_recursivo(self.inicio)

    def _mostrar_recursivo(self, nodo):
        if nodo is None:
            return
        print(f"   - {nodo.nombre} | {nodo.categoria} | ${nodo.precio} | stock: {nodo.cantidad}")
        self._mostrar_recursivo(nodo.siguiente)


# ═══════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    inv = Inventario()

    inv.agregar("Pan", "Panadería", 2500, 50)
    inv.agregar("Leche", "Lácteos", 4500, 30)
    inv.agregar("Arroz", "Granos", 3200, 100)
    inv.agregar("Sal", "Condimentos", 1500, 5)
    inv.mostrar()

    print("Valor total:", inv.valor_total())

    bajo_stock = inv.productos_bajo_stock(40)
    bajo_stock.mostrar()

    print("Eliminar Sal:", inv.eliminar("Sal"))
    inv.mostrar()