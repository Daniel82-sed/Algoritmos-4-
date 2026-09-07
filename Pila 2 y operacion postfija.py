class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None 

class Pila :
    def __init__(self):
        self.tope = None
        self.tam = 0 #tamaño


    def esta_vacia(self):
        return self.tope is None

    def push(self, dato):# push ingresar un dato a la pila al inicio por lo que no se demora mas por el numero 
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tam += 1 

    def pop(self): # entregar lo del tope y entregar ese sacadolo de la lista 
        if self.esta_vacia():
            raise Exception("Error : No hay elementos en la pila ")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tam -= 1 
        return dato

    def peek(self): #muestra lo del tope pero no lo elimina como pop
        if self.esta_vacia():
            raise Exception("Error : No hay elementos en la pila ")
        return self.tope.dato

    def __len__(self): # tamaño de la pila 
        return self.tam

    def __str__(self):#elementos de la pila 
        if self.esta_vacia():
            return "Pila vacia"
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return "Tope -->" + "-->".join(elementos) + "--> None "

def evaluar_postfija(expresion):

    tokens = expresion.split()
    pila = Pila()

    operadores = {
        '+': lambda a,b : a+b,
        '-': lambda a,b : a-b,
        '*': lambda a,b : a*b,
        '/': lambda a,b : a/b
    }

    for token in tokens:
        if token.lstrip('-').replace('.',' ').isdigit():
            valor = float(token) if '.' in token else int(token)
            pila.push(valor)
        elif token in operadores:
            a = pila.pop()
            b = pila.pop()
            resultado = operadores[token](a,b)
            pila.push(resultado)
    return pila.pop()

evaluar_postfija("3 4 5 * +")

def imprimir():
    expresion = "3 4 5 * +"
    resultado = evaluar_postfija(expresion)
    print("Resultado : ", resultado)

imprimir()

