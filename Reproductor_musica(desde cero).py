# ==========================================================================
# REPRODUCTOR DE MUSICA SIMPLE
# ==========================================================================
# Este programa es un proyecto educativo para aprender dos cosas al mismo
# tiempo:
#   1) Programacion basica en Python.
#   2) Como funciona una "lista doblemente enlazada" (una forma de guardar
#      datos conectados entre si, como si fueran vagones de un tren).
#
# No vamos a reproducir archivos MP3 de verdad. Cuando el programa "reproduce"
# una cancion, simplemente usamos print() para simular que se esta escuchando.
# ==========================================================================


# --------------------------------------------------------------------------
# QUE ES UNA CLASE Y QUE ES UN OBJETO
# --------------------------------------------------------------------------
# Una "clase" es como un molde o una plantilla para crear cosas.
# Por ejemplo, la clase "Nodo" es el molde para crear nodos.
# Un "objeto" es una cosa concreta creada a partir de ese molde.
# Si Nodo es el molde para hacer galletas, cada galleta que sale del molde
# es un objeto (una instancia) de esa clase.


class Nodo:
    # Esta clase representa UN nodo de la lista doblemente enlazada.
    # Un nodo es como un "vagon de tren": guarda informacion (la cancion)
    # y ademas sabe cual es el vagon anterior y cual es el vagon siguiente.

    def __init__(self, cancion):
        # __init__ es un metodo especial que se ejecuta automaticamente
        # cada vez que creamos un nodo nuevo. Sirve para darle sus
        # valores iniciales.
        #
        # "self" representa "este mismo objeto". Cuando escribimos
        # self.cancion, self.anterior, etc, estamos diciendo:
        # "guarda esto DENTRO de este nodo en particular".
        #
        # "cancion" es un parametro: es un valor que le pasamos a la
        # funcion cuando la llamamos, por ejemplo Nodo("Bohemian Rhapsody").

        self.cancion = cancion   # Guardamos el nombre de la cancion (un atributo).
        self.anterior = None     # Al principio no conocemos el nodo anterior, por eso None.
        self.siguiente = None    # Al principio no conocemos el nodo siguiente, por eso None.

        # None en Python significa "nada" o "vacio". Se usa para decir
        # que todavia no hay ningun valor real en esa variable.


# --------------------------------------------------------------------------
# LA LISTA DOBLEMENTE ENLAZADA
# --------------------------------------------------------------------------
class ListaDoble:
    # Esta clase maneja TODOS los nodos juntos, es decir, la playlist
    # completa. Es la que sabe donde empieza la lista, donde termina,
    # y cual es la cancion que se esta escuchando ahora mismo.

    def __init__(self):
        # Al crear la lista, todavia no hay ninguna cancion.
        self.head = None    # "head" (cabeza) es el PRIMER nodo de la lista.
        self.tail = None    # "tail" (cola) es el ULTIMO nodo de la lista.
        self.actual = None  # "actual" es el nodo que se esta reproduciendo ahora.

        # Ejemplo visual de como se van a conectar los nodos:
        # None <- Cancion 1 <-> Cancion 2 <-> Cancion 3 -> None
        #
        # Cada nodo apunta con "siguiente" hacia la derecha,
        # y con "anterior" hacia la izquierda.

    # ----------------------------------------------------------------
    # AGREGAR UNA CANCION AL FINAL DE LA LISTA
    # ----------------------------------------------------------------
    def agregar_cancion(self, nombre_cancion):
        nodo_nuevo = Nodo(nombre_cancion)  # Creamos un nodo nuevo con la cancion.

        # CASO 1: la lista esta vacia (no hay head todavia).
        if self.head is None:
            # Si no hay ninguna cancion, el nodo nuevo sera el primero
            # y tambien el ultimo al mismo tiempo.
            self.head = nodo_nuevo
            self.tail = nodo_nuevo
            self.actual = nodo_nuevo  # Tambien se convierte en la cancion actual.
        else:
            # CASO 2: ya hay canciones, entonces agregamos al final.
            # self.tail es el ultimo nodo que existia ANTES de agregar este.
            ultimo_nodo = self.tail

            # Conectamos el ultimo nodo viejo con el nodo nuevo.
            ultimo_nodo.siguiente = nodo_nuevo
            nodo_nuevo.anterior = ultimo_nodo

            # Ahora el nodo nuevo pasa a ser el ultimo (el nuevo tail).
            self.tail = nodo_nuevo

        print(f"Se agrego la cancion: {nombre_cancion}")

    # ----------------------------------------------------------------
    # ELIMINAR UNA CANCION POR NOMBRE
    # ----------------------------------------------------------------
    def eliminar_cancion(self, nombre_cancion):
        # Primero tenemos que ENCONTRAR el nodo que tiene esa cancion.
        # Para recorrer la lista, empezamos desde el head y avanzamos
        # usando "siguiente" hasta llegar a None (el final).

        nodo_actual = self.head

        while nodo_actual is not None:
            # "while" es un bucle que se repite mientras la condicion sea verdadera.
            # Aqui decimos: "mientras todavia haya un nodo para revisar".

            if nodo_actual.cancion == nombre_cancion:
                # Encontramos la cancion que queremos eliminar.

                nodo_anterior = nodo_actual.anterior
                nodo_siguiente = nodo_actual.siguiente

                # CASO A: el nodo a eliminar es el head (el primero).
                if nodo_anterior is None:
                    self.head = nodo_siguiente
                else:
                    nodo_anterior.siguiente = nodo_siguiente

                # CASO B: el nodo a eliminar es el tail (el ultimo).
                if nodo_siguiente is None:
                    self.tail = nodo_anterior
                else:
                    nodo_siguiente.anterior = nodo_anterior

                # Si la cancion eliminada era la que estaba sonando,
                # movemos "actual" a otra cancion valida (o a None si ya no queda nada).
                if self.actual == nodo_actual:
                    if nodo_siguiente is not None:
                        self.actual = nodo_siguiente
                    else:
                        self.actual = nodo_anterior

                print(f"Se elimino la cancion: {nombre_cancion}")
                return  # "return" termina la funcion aqui porque ya hicimos el trabajo.

            # Si esta no era la cancion buscada, avanzamos al siguiente nodo.
            nodo_actual = nodo_actual.siguiente

        # Si el bucle "while" termina y nunca hicimos "return",
        # significa que recorrimos toda la lista y no encontramos la cancion.
        print(f"No se encontro la cancion: {nombre_cancion}")

    # ----------------------------------------------------------------
    # MOSTRAR TODAS LAS CANCIONES
    # ----------------------------------------------------------------
    def mostrar_canciones(self):
        if self.head is None:
            # Manejamos el caso en que la lista esta vacia.
            print("No hay canciones en la lista.")
            return

        print("----- Lista de canciones -----")
        nodo_actual = self.head
        posicion = 1  # Usamos un contador para numerar las canciones.

        while nodo_actual is not None:
            # Si esta cancion es la que esta sonando, la marcamos.
            if nodo_actual == self.actual:
                print(f"{posicion}. {nodo_actual.cancion}  <-- sonando ahora")
            else:
                print(f"{posicion}. {nodo_actual.cancion}")

            nodo_actual = nodo_actual.siguiente
            posicion = posicion + 1

        print("-------------------------------")

    # ----------------------------------------------------------------
    # BUSCAR UNA CANCION
    # ----------------------------------------------------------------
    def buscar_cancion(self, nombre_cancion):
        nodo_actual = self.head

        while nodo_actual is not None:
            if nodo_actual.cancion == nombre_cancion:
                print(f"La cancion '{nombre_cancion}' SI esta en la lista.")
                return nodo_actual  # Devolvemos el nodo encontrado.
            nodo_actual = nodo_actual.siguiente

        print(f"La cancion '{nombre_cancion}' NO esta en la lista.")
        return None

    # ----------------------------------------------------------------
    # SELECCIONAR UNA CANCION (LA CONVIERTE EN LA ACTUAL)
    # ----------------------------------------------------------------
    def seleccionar_cancion(self, nombre_cancion):
        nodo_encontrado = self.buscar_cancion(nombre_cancion)

        if nodo_encontrado is not None:
            self.actual = nodo_encontrado
            print(f"Ahora la cancion actual es: {nombre_cancion}")

    # ----------------------------------------------------------------
    # REPRODUCIR LA CANCION ACTUAL (SIMULADO)
    # ----------------------------------------------------------------
    def reproducir_actual(self):
        if self.actual is None:
            print("No hay ninguna cancion para reproducir.")
        else:
            # Simulamos la reproduccion solo con un print.
            print(f"Reproduciendo: {self.actual.cancion}")

    # ----------------------------------------------------------------
    # AVANZAR A LA SIGUIENTE CANCION
    # ----------------------------------------------------------------
    def siguiente_cancion(self):
        if self.actual is None:
            print("No hay canciones en la lista.")
            return

        if self.actual.siguiente is None:
            # Ya estamos en la ultima cancion, no hay a donde avanzar.
            print("Ya estas en la ultima cancion de la lista.")
        else:
            self.actual = self.actual.siguiente
            print(f"Cancion actual: {self.actual.cancion}")

    # ----------------------------------------------------------------
    # RETROCEDER A LA CANCION ANTERIOR
    # ----------------------------------------------------------------
    def anterior_cancion(self):
        if self.actual is None:
            print("No hay canciones en la lista.")
            return

        if self.actual.anterior is None:
            # Ya estamos en la primera cancion, no hay a donde retroceder.
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
    # CONTAR CUANTAS CANCIONES HAY
    # ----------------------------------------------------------------
    def contar_canciones(self):
        contador = 0
        nodo_actual = self.head

        while nodo_actual is not None:
            contador = contador + 1
            nodo_actual = nodo_actual.siguiente

        print(f"Cantidad de canciones: {contador}")
        return contador


# ==========================================================================
# MENU DEL PROGRAMA (LA PARTE QUE VE EL USUARIO)
# ==========================================================================
def mostrar_menu():
    # Esta funcion solo imprime las opciones disponibles.
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
    # Creamos un objeto de tipo ListaDoble. Esta sera nuestra playlist.
    playlist = ListaDoble()

    # "True" hace que el bucle se repita para siempre, hasta que
    # usemos "break" para salir de el.
    while True:
        mostrar_menu()

        # input() muestra un mensaje y espera a que el usuario escriba algo.
        # Lo que el usuario escribe siempre llega como texto (str).
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            nombre = input("Nombre de la cancion a agregar: ")
            playlist.agregar_cancion(nombre)

        elif opcion == "2":
            nombre = input("Nombre de la cancion a eliminar: ")
            playlist.eliminar_cancion(nombre)

        elif opcion == "3":
            playlist.mostrar_canciones()

        elif opcion == "4":
            nombre = input("Nombre de la cancion a buscar: ")
            playlist.buscar_cancion(nombre)

        elif opcion == "5":
            nombre = input("Nombre de la cancion a seleccionar: ")
            playlist.seleccionar_cancion(nombre)

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
            break  # "break" corta el bucle "while True" y termina el programa.

        else:
            # Si el usuario escribe algo que no es ninguna opcion valida.
            print("Opcion invalida, intenta de nuevo.")


# --------------------------------------------------------------------------
# Este "if" es una convencion muy comun en Python.
# Significa: "si este archivo se esta ejecutando directamente
# (y no fue importado desde otro archivo), entonces ejecuta main()".
# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()
