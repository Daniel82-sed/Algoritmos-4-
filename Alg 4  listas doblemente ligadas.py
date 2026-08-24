class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None 

    def esta_vacia(self):
        return self.cabeza is None #para ahorrar un if else 

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza  #se trabaja de manera constante con la cabeza por lo cual no es necesario recorrer lista 
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar_incio(self):
        if self.esta_vacia(): #si la lista está vacía 
            return None

        dato = self.cabeza.dato

        if self.cabeza == self.cola: #eliminar dato pero si solo es un dato
            self.cabeza = None
            self.cola = None 
        else:
            self.cabeza = self.cabeza.siguiente # pasar la cabeza para no borrar la referencia 
            self.cabeza.anterior = None 

        return dato 

    def eliminar_ultimo(self):
        # 1. Primero validamos si está vacía
        if self.esta_vacia():
            return None 

        # 2. Guardamos el dato que vamos a retornar
        dato = self.cola.dato

        # 3. Si solo hay un nodo en la lista
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None 
        # 4. Si hay más de un nodo
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None # Corregido el typo 'sieguiente'

        return dato

        

        


