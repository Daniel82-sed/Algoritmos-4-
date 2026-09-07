class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None 

class Pila:
    def __init__(self):
        self.tope = None
        self.tam = 0 # tamaño


    def esta_vacia(self):
        return self.tope is None

    def push(self, dato): # push ingresar un dato a la pila al inicio por lo que no se demora mas por el numero
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tam += 1 

    def pop(self): # entregar lo del tope y entregar ese sacandolo de la lista
        if self.esta_vacia():
            raise Exception("Error : No hay elementos en la pila ")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tam -= 1 
        return dato

    def peek(self): # muestra lo del tope pero no lo elimina como pop
        if self.esta_vacia():
            raise Exception("Error : No hay elementos en la pila ")
        return self.tope.dato

    def __len__(self): # tamaño de la pila
        return self.tam

    def __str__(self): # elementos de la pila
        if self.esta_vacia():
            return "Pila vacia"
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "Tope --> " + "-->".join(elementos) + "--> None "

pila = Pila()
print(len(pila)) # imprimir tamaño pila
pila.push(10)
pila.push(20)
pila.push(30)
pila.push(50)
pila.peek()
print(pila) # imprimir pila
