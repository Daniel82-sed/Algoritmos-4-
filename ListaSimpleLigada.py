class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print ("Nodo agregado exitosamente")
    def mostrar_lista(self):
        actual = self.cabeza
        if actual != None :
            while actual != None:
                print (f"{actual.dato} -->")
                actual = actual.siguiente
            print ("fin")
        else:
            print("Lista vacia")
    def __str__(self):
        if self.cabeza == None:
            return "[]"

        elementos = []
        actual = self.cabeza
        while actual != None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente 
        return "[" + "-->" .join(elementos) + "]"
    def insertar_inicio(self, dato):
        nuevo_nodo = Node(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print ("Nodo insertado exitosamente ")



            

        


lista_ligada = Lista()
lista_ligada.agregar_nodo("Primer Nodo")
lista_ligada.agregar_nodo("Segundo Nodo")
print(lista_ligada)
lista_ligada.mostrar_lista()
