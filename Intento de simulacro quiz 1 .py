"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN A
                    Sistema de Historial de Navegador Web
═══════════════════════════════════════════════════════════════════════════════
"""

# ─────────────────────────────────────────────────────────────────────────────
# PUNTO 1a: Clase Nodo (Pagina)
# ─────────────────────────────────────────────────────────────────────────────
# Cada Pagina es un "nodo" de la lista enlazada.
# Guarda los datos de la página visitada y un puntero (siguiente) hacia
# el próximo nodo de la lista.
class Pagina:
    def __init__(self, url, titulo, tiempo):
        self.url = url            # dirección de la página
        self.titulo = titulo      # nombre/título de la página
        self.tiempo = tiempo      # segundos que el usuario estuvo en la página
        self.siguiente = None     # enlace al siguiente nodo (al principio no apunta a nada)


# ─────────────────────────────────────────────────────────────────────────────
# PUNTO 1b: Clase Lista (Historial)
# ─────────────────────────────────────────────────────────────────────────────
class Historial:
    def __init__(self):
        # inicio guarda la referencia a la primera página de la lista
        # (la página más reciente siempre estará aquí)
        self.inicio = None

    # ────────────────────────────────────────────────────────────────────
    # PUNTO 2: Agregar página (visitar) - O(1)
    # ────────────────────────────────────────────────────────────────────
    # Como las páginas más recientes van al INICIO, solo necesitamos
    # crear el nodo nuevo y hacer que apunte a lo que antes era el inicio.
    # Esto no recorre la lista, por eso es O(1).
    def visitar(self, url, titulo, tiempo):
        nueva_pagina = Pagina(url, titulo, tiempo)   # creamos el nodo nuevo
        nueva_pagina.siguiente = self.inicio         # apunta a la vieja "cabeza"
        self.inicio = nueva_pagina                   # la nueva página es la cabeza

    # ────────────────────────────────────────────────────────────────────
    # PUNTO 3: Tiempo total de navegación (RECURSIVO)
    # ────────────────────────────────────────────────────────────────────
    # Idea: el tiempo total = tiempo de la página actual + tiempo total
    # del resto de la lista (lo que sigue después).
    # Caso base: si el nodo es None (llegamos al final), sumamos 0.
    def tiempo_total(self):
        # método "público" que el usuario llama, arranca la recursión desde el inicio
        return self._tiempo_total_recursivo(self.inicio)

    def _tiempo_total_recursivo(self, nodo):
        if nodo is None:              # caso base: ya no hay más páginas
            return 0
        # caso recursivo: tiempo de esta página + suma del resto
        return nodo.tiempo + self._tiempo_total_recursivo(nodo.siguiente)

    # ────────────────────────────────────────────────────────────────────
    # PUNTO 4: Buscar por dominio (RECURSIVO) - no modifica la original
    # ────────────────────────────────────────────────────────────────────
    # Recorremos la lista original nodo por nodo (recursivamente).
    # Si la url del nodo actual contiene el texto buscado, lo agregamos
    # a la NUEVA lista de resultados usando visitar (así queda O(1) por página
    # y no recorremos la lista de resultados cada vez).
    def buscar_por_dominio(self, texto):
        resultado = Historial()  # nueva lista vacía donde guardamos coincidencias
        self._buscar_recursivo(self.inicio, texto, resultado)
        return resultado

    def _buscar_recursivo(self, nodo, texto, resultado):
        if nodo is None:              # caso base: se acabó la lista original
            return
        if texto in nodo.url:         # si coincide, se agrega a la nueva lista
            resultado.visitar(nodo.url, nodo.titulo, nodo.tiempo)
        # seguimos con el siguiente nodo (avanzamos solo "la cabeza", sin recorrer doble)
        self._buscar_recursivo(nodo.siguiente, texto, resultado)

    # ────────────────────────────────────────────────────────────────────
    # PUNTO 5: Eliminar páginas rápidas (RECURSIVO) - modifica la original
    # ────────────────────────────────────────────────────────────────────
    # Truco clásico de listas enlazadas recursivas para eliminar nodos:
    # la función recibe un nodo y devuelve cuál debe quedar en su lugar
    # (el mismo nodo si se conserva, o el resultado de procesar el
    # siguiente si el nodo actual se elimina).
    def eliminar_rapidas(self, x):
        self.inicio = self._eliminar_recursivo(self.inicio, x)

    def _eliminar_recursivo(self, nodo, x):
        if nodo is None:                       # caso base: fin de la lista
            return None

        # primero resolvemos el resto de la lista (recursión)
        nodo.siguiente = self._eliminar_recursivo(nodo.siguiente, x)

        if nodo.tiempo < x:
            # esta página se elimina: la "saltamos" devolviendo lo que sigue
            return nodo.siguiente
        else:
            # esta página se conserva, ya con su "siguiente" corregido
            return nodo

    # ────────────────────────────────────────────────────────────────────
    # Método extra para poder ver el contenido del historial
    # ────────────────────────────────────────────────────────────────────
    def mostrar(self):
        if self.inicio is None:
            print("   (historial vacío)")
            return
        self._mostrar_recursivo(self.inicio)

    def _mostrar_recursivo(self, nodo):
        if nodo is None:      # caso base: no hay más nodos que mostrar
            return
        print(f"   - {nodo.titulo} | {nodo.url} | {nodo.tiempo}s")
        self._mostrar_recursivo(nodo.siguiente)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL HISTORIAL DE NAVEGACIÓN")
    print("=" * 60)

    # Crear historial
    historial = Historial()

    # Agregar páginas (la más reciente queda primero)
    historial.visitar("https://www.google.com/search", "Búsqueda Google", 15)
    historial.visitar("https://www.youtube.com/watch", "Video YouTube", 300)
    historial.visitar("https://www.github.com/repo", "GitHub Repo", 180)
    historial.visitar("https://www.youtube.com/home", "YouTube Home", 45)
    historial.visitar("https://www.google.com/maps", "Google Maps", 5)

    print("\n📋 Historial inicial:")
    historial.mostrar()

    # Prueba tiempo total
    print("\n⏱️ Tiempo total:", historial.tiempo_total(), "segundos")
    print("   Esperado: 545 segundos")

    # Prueba buscar por dominio
    print("\n🔍 Páginas de YouTube:")
    youtube = historial.buscar_por_dominio("youtube")
    youtube.mostrar()

    # Prueba eliminar rápidas
    print("\n🗑️ Eliminando páginas < 30 segundos...")
    historial.eliminar_rapidas(30)
    historial.mostrar()
    print("   (Google Maps y Búsqueda Google deberían estar eliminadas)")
