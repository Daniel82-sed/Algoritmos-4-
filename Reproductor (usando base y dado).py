# ==========================================================================
# REPRODUCTOR DE MUSICA CON LISTA DOBLEMENTE ENLAZADA
# ==========================================================================
# Este archivo parte de la clase Cancion que ya tenias en tu REPRODUCTOR
# original, y le agrega una lista doblemente enlazada (basada en las ideas
# del algoritmo "Alg 4 - listas doblemente ligadas.py") para poder manejar
# varias canciones: agregar, eliminar, recorrer, avanzar y retroceder.
#
# No reproducimos audio real. "Reproducir" una cancion solo significa
# imprimir un mensaje con print(), ya que el objetivo es aprender la
# estructura de datos (la lista doblemente enlazada), no crear Spotify.
# ==========================================================================


# --------------------------------------------------------------------------
# CLASE Cancion (esta es la que ya tenias en tu REPRODUCTOR original)
# --------------------------------------------------------------------------
# Una "clase" es un molde para crear objetos. Cada vez que escribimos
# Cancion("titulo", "artista", 200) estamos creando un OBJETO (una cancion
# concreta) a partir de ese molde.
class Cancion:

    def __init__(self, titulo, artista, duracion):
        # __init__ se ejecuta automaticamente al crear una Cancion nueva.
        # "self" es una forma de decir "esta cancion en particular".
        # titulo, artista y duracion son parametros: valores que nos pasan
        # cuando se crea el objeto.
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion  # duracion en segundos (numero entero)

    def duracion_formateada(self):
        # // es la division entera: nos da solo la parte entera del resultado.
        # Por ejemplo, 200 // 60 = 3 (minutos completos).
        minutos = self.duracion // 60

        # % es el operador modulo: nos da el RESTO de una division.
        # Por ejemplo, 200 % 60 = 20 (los segundos que sobran).
        segundos = self.duracion % 60

        # Usamos :02 para que los segundos siempre se vean con 2 digitos,
        # por ejemplo "3:05" en vez de "3:5".
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        # __str__ es un metodo especial que Python usa automaticamente
        # cuando hacemos print(objeto). Asi, en vez de ver algo como
        # "<Cancion object at 0x...>", vemos un texto legible.
        return f"{self.titulo} - {self.artista} ({self.duracion_formateada()})"


# --------------------------------------------------------------------------
# CLASE Nodo (idea tomada del algoritmo de referencia)
# --------------------------------------------------------------------------
# En el algoritmo de referencia, cada Nodo guardaba un "dato" generico.
# Aqui hacemos lo mismo, pero el "dato" que guarda cada nodo es una Cancion.
# Cada nodo tambien conoce al nodo de al lado (siguiente) y al de atras
# (anterior), como un vagon de tren conectado a otros dos vagones.
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion    # Aqui guardamos el objeto Cancion.
        self.siguiente = None     # Referencia al nodo de adelante.
        self.anterior = None      # Referencia al nodo de atras.
        # None significa "todavia no hay ningun nodo conectado ahi".


# --------------------------------------------------------------------------
# CLASE ListaDoble (adaptada del algoritmo de referencia para manejar
# canciones en vez de datos genericos)
# --------------------------------------------------------------------------
# Mantenemos los nombres "cabeza" y "cola" del algoritmo de referencia,
# porque tu REPRODUCTOR original no tenia ninguna lista todavia (no hay
# conflicto de nombres). Ademas agregamos "actual", que es necesario para
# saber que cancion se esta reproduciendo en este momento.
class ListaDoble:
    def __init__(self):
        self.cabeza = None   # Primer nodo de la lista (como "head").
        self.cola = None     # Ultimo nodo de la lista (como "tail").
        self.actual = None   # Nodo de la cancion que esta sonando ahora.

        # Conexion final que buscamos lograr:
        # None <- Cancion 1 <-> Cancion 2 <-> Cancion 3 -> None

    def esta_vacia(self):
        # Tomado directamente del algoritmo de referencia: si "cabeza" es
        # None, entonces no hay ningun nodo, y la lista esta vacia.
        return self.cabeza is None

    # ----------------------------------------------------------------
    # AGREGAR CANCION (basado en insertar_final del algoritmo de referencia)
    # ----------------------------------------------------------------
    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)

        if self.esta_vacia():
            # Si no hay ninguna cancion todavia, el nodo nuevo es a la vez
            # la cabeza y la cola de la lista.
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.actual = nuevo_nodo  # Tambien se vuelve la cancion actual.
        else:
            # Igual que insertar_final en el algoritmo de referencia:
            # conectamos el nodo nuevo despues de la cola actual.
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

        print(f"Se agrego la cancion: {cancion.titulo}")

    # ----------------------------------------------------------------
    # ELIMINAR CANCION POR TITULO
    # ----------------------------------------------------------------
    # El algoritmo de referencia solo eliminaba al inicio o al final.
    # Aqui necesitamos eliminar una cancion por su titulo, sin importar
    # en que posicion este, asi que recorremos la lista para encontrarla.
    def eliminar_cancion(self, titulo):
        if self.esta_vacia():
            print("No hay canciones en la lista.")
            return

        nodo_actual = self.cabeza

        # "while" repite este bloque mientras nodo_actual no sea None,
        # es decir, mientras sigamos teniendo nodos por revisar.
        while nodo_actual is not None:
            if nodo_actual.cancion.titulo == titulo:
                anterior = nodo_actual.anterior
                siguiente = nodo_actual.siguiente

                # Reconectamos los vecinos del nodo que vamos a quitar,
                # igual que se hace en eliminar_inicio/eliminar_ultimo
                # del algoritmo de referencia, pero aqui puede pasar en
                # cualquier posicion de la lista.

                if anterior is None:
                    # El nodo a eliminar era la cabeza.
                    self.cabeza = siguiente
                else:
                    anterior.siguiente = siguiente

                if siguiente is None:
                    # El nodo a eliminar era la cola.
                    self.cola = anterior
                else:
                    siguiente.anterior = anterior

                # Si la cancion eliminada era la que sonaba, movemos
                # "actual" a otra cancion valida (o None si ya no queda nada).
                if self.actual == nodo_actual:
                    if siguiente is not None:
                        self.actual = siguiente
                    else:
                        self.actual = anterior

                print(f"Se elimino la cancion: {titulo}")
                return  # return corta la funcion aqui, ya terminamos.

            nodo_actual = nodo_actual.siguiente

        # Si el while termina sin encontrar la cancion, avisamos.
        print(f"No se encontro la cancion: {titulo}")

    # ----------------------------------------------------------------
    # MOSTRAR TODAS LAS CANCIONES
    # ----------------------------------------------------------------
    def mostrar_canciones(self):
        if self.esta_vacia():
            print("No hay canciones en la lista.")
            return

        print("----- Lista de canciones -----")
        nodo_actual = self.cabeza
        posicion = 1

        while nodo_actual is not None:
            marca = "  <-- sonando ahora" if nodo_actual == self.actual else ""
            print(f"{posicion}. {nodo_actual.cancion}{marca}")
            nodo_actual = nodo_actual.siguiente
            posicion = posicion + 1

        print("-------------------------------")

    # ----------------------------------------------------------------
    # BUSCAR CANCION POR TITULO
    # ----------------------------------------------------------------
    def buscar_cancion(self, titulo):
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            if nodo_actual.cancion.titulo == titulo:
                print(f"La cancion '{titulo}' SI esta en la lista.")
                return nodo_actual
            nodo_actual = nodo_actual.siguiente

        print(f"La cancion '{titulo}' NO esta en la lista.")
        return None

    # ----------------------------------------------------------------
    # SELECCIONAR CANCION (la convierte en la actual)
    # ----------------------------------------------------------------
    def seleccionar_cancion(self, titulo):
        nodo_encontrado = self.buscar_cancion(titulo)
        if nodo_encontrado is not None:
            self.actual = nodo_encontrado
            print(f"Ahora la cancion actual es: {titulo}")

    # ----------------------------------------------------------------
    # REPRODUCIR LA CANCION ACTUAL (simulado con print)
    # ----------------------------------------------------------------
    def reproducir_actual(self):
        if self.actual is None:
            print("No hay ninguna cancion para reproducir.")
        else:
            print(f"Reproduciendo: {self.actual.cancion}")

    # ----------------------------------------------------------------
    # SIGUIENTE CANCION
    # ----------------------------------------------------------------
    def siguiente_cancion(self):
        if self.actual is None:
            print("No hay canciones en la lista.")
        elif self.actual.siguiente is None:
            print("Ya estas en la ultima cancion de la lista.")
        else:
            self.actual = self.actual.siguiente
            print(f"Cancion actual: {self.actual.cancion}")

    # ----------------------------------------------------------------
    # CANCION ANTERIOR
    # ----------------------------------------------------------------
    def anterior_cancion(self):
        if self.actual is None:
            print("No hay canciones en la lista.")
        elif self.actual.anterior is None:
            print("Ya estas en la primera cancion de la lista.")
        else:
            self.actual = self.actual.anterior
            print(f"Cancion actual: {self.actual.cancion}")

    # ----------------------------------------------------------------
    # MOSTRAR LA CANCION ACTUAL
    # ----------------------------------------------------------------
    def mostrar_actual(self):
        if self.actual is None:
            print("No hay ninguna cancion seleccionada.")
        else:
            print(f"Cancion actual: {self.actual.cancion}")

    # ----------------------------------------------------------------
    # CONTAR CANCIONES
    # ----------------------------------------------------------------
    def contar_canciones(self):
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            contador = contador + 1
            nodo_actual = nodo_actual.siguiente
        print(f"Cantidad de canciones: {contador}")
        return contador


# ==========================================================================
# MENU DEL PROGRAMA
# ==========================================================================
def mostrar_menu():
    print("\n===== REPRODUCTOR DE MUSICA =====")
    print("1. Agregar cancion")
    print("2. Eliminar cancion")
    print("3. Mostrar todas las canciones")
    print("4. Buscar cancion")
    print("5. Seleccionar cancion")
    print("6. Reproducir cancion actual")
    print("7. Siguiente cancion")
    print("8. Cancion anterior")
    print("9. Mostrar cancion actual")
    print("10. Mostrar cantidad de canciones")
    print("0. Salir")


def main():
    playlist = ListaDoble()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            titulo = input("Titulo de la cancion: ")
            artista = input("Artista: ")

            # int() convierte el texto que escribe el usuario en un numero
            # entero, porque input() siempre devuelve texto (str).
            duracion = int(input("Duracion en segundos: "))

            nueva_cancion = Cancion(titulo, artista, duracion)
            playlist.agregar_cancion(nueva_cancion)

        elif opcion == "2":
            titulo = input("Titulo de la cancion a eliminar: ")
            playlist.eliminar_cancion(titulo)

        elif opcion == "3":
            playlist.mostrar_canciones()

        elif opcion == "4":
            titulo = input("Titulo de la cancion a buscar: ")
            playlist.buscar_cancion(titulo)

        elif opcion == "5":
            titulo = input("Titulo de la cancion a seleccionar: ")
            playlist.seleccionar_cancion(titulo)

        elif opcion == "6":
            playlist.reproducir_actual()

        elif opcion == "7":
            playlist.siguiente_cancion()

        elif opcion == "8":
            playlist.anterior_cancion()

        elif opcion == "9":
            playlist.mostrar_actual()

        elif opcion == "10":
            playlist.contar_canciones()

        elif opcion == "0":
            print("Cerrando el reproductor. Hasta luego!")
            break

        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()
