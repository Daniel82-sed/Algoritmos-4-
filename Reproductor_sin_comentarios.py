class Cancion:

    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def duracion_formateada(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion_formateada()})"


class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.actual = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

        print(f"Se agrego la cancion: {cancion.titulo}")

    def eliminar_cancion(self, titulo):
        if self.esta_vacia():
            print("No hay canciones en la lista.")
            return

        nodo_actual = self.cabeza

        while nodo_actual is not None:
            if nodo_actual.cancion.titulo == titulo:
                anterior = nodo_actual.anterior
                siguiente = nodo_actual.siguiente

                if anterior is None:
                    self.cabeza = siguiente
                else:
                    anterior.siguiente = siguiente

                if siguiente is None:
                    self.cola = anterior
                else:
                    siguiente.anterior = anterior

                if self.actual == nodo_actual:
                    if siguiente is not None:
                        self.actual = siguiente
                    else:
                        self.actual = anterior

                print(f"Se elimino la cancion: {titulo}")
                return

            nodo_actual = nodo_actual.siguiente

        print(f"No se encontro la cancion: {titulo}")

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

    def buscar_cancion(self, titulo):
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            if nodo_actual.cancion.titulo == titulo:
                print(f"La cancion '{titulo}' SI esta en la lista.")
                return nodo_actual
            nodo_actual = nodo_actual.siguiente

        print(f"La cancion '{titulo}' NO esta en la lista.")
        return None

    def seleccionar_cancion(self, titulo):
        nodo_encontrado = self.buscar_cancion(titulo)
        if nodo_encontrado is not None:
            self.actual = nodo_encontrado
            print(f"Ahora la cancion actual es: {titulo}")

    def reproducir_actual(self):
        if self.actual is None:
            print("No hay ninguna cancion para reproducir.")
        else:
            print(f"Reproduciendo: {self.actual.cancion}")

    def siguiente_cancion(self):
        if self.actual is None:
            print("No hay canciones en la lista.")
        elif self.actual.siguiente is None:
            print("Ya estas en la ultima cancion de la lista.")
        else:
            self.actual = self.actual.siguiente
            print(f"Cancion actual: {self.actual.cancion}")

    def anterior_cancion(self):
        if self.actual is None:
            print("No hay canciones en la lista.")
        elif self.actual.anterior is None:
            print("Ya estas en la primera cancion de la lista.")
        else:
            self.actual = self.actual.anterior
            print(f"Cancion actual: {self.actual.cancion}")

    def mostrar_actual(self):
        if self.actual is None:
            print("No hay ninguna cancion seleccionada.")
        else:
            print(f"Cancion actual: {self.actual.cancion}")

    def contar_canciones(self):
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            contador = contador + 1
            nodo_actual = nodo_actual.siguiente
        print(f"Cantidad de canciones: {contador}")
        return contador


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
