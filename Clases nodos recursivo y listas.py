#Creacion de nodos
class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Creacion de lista
class Lista:
    def __init__(self):
        self.cabeza = None

    #Agregar un nuevo nodo al !FINAL¡
    def agregar(self, dato):
        nuevo = Node(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def contar_nodos(self, nodo = None):

        if nodo is None:
            return 0

        return 1 + self.contar_nodos(nodo.siguiente)

    def buscar (self, dato, nodo=None):
        if nodo is None:
            return False

        if nodo.dato == dato:
            return True
        return self.buscar(dato, nodo.siguiente)
