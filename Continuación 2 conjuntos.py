#clase martes 22 09 2026 , mezcla de conjuntos y otras cosas 
catalogo = { # es un diccionerio con conjuntos adentro
    "Inception": {"ciencia ficción", "accción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic"  : {"romance", "drama", "histórica"}, 
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "Toy story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"}
}

#INDICE DE JACCARD = (A & B) / (A | B) # determina la similitud entre conjuntos entre 0 - 1
def similitud_jaccard(pelicula1, pelicula2):
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]

    # Obtiene la cantidad de géneros que tienen en común
    interseccion = len(g1 & g2)

    # Obtiene la cantidad total de géneros diferentes entre ambas
    union = len(g1 | g2)

    # Calcula la similitud: géneros en común / géneros totales
    return interseccion / union if union > 0 else 0


pares = [
    ("Inception", "The Matrix"),
    ("Inception", "Titanic"),
    ("Toy story", "Shrek"),
    ("Avengers", "John Wick")
]


for p1, p2 in pares:
    # Calcula la similitud entre cada par de películas
    sim = similitud_jaccard(p1, p2)

    # Convierte el resultado a porcentaje y lo muestra
    print(f"Índice Jaccard entre {p1} y {p2} es {round(sim * 100, 2)}%")

print("------------------ 2nda parte ---------------")
#dicciionarios y conjuntos 
roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"},
}
usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}

#crear un método que recibe un conjunto de acciones y usuario, y retorne True o False
#dependiendo si el usuario puede o no realizar todo ese conjunto de acciones

"""#SOLUCION DE IA
# Verifica si el usuario tiene permiso para realizar todas las acciones
def validar_acciones(usuario, acciones):

    # Obtiene el rol que tiene asignado el usuario
    rol = usuarios[usuario]

    # Obtiene las acciones permitidas para ese rol
    permisos = roles[rol]

    # Comprueba que todas las acciones solicitadas estén permitidas
    return acciones.issubset(permisos)"""
#SOLUCIÓN PROFE
def validar_acciones(usuario, acciones):
    # Obtiene el rol asignado al usuario
    rol = usuarios.get(usuario)

    # Si el usuario no existe, no tiene permisos
    if not rol:
        return False

    # Obtiene los permisos del rol; si no existe, usa un conjunto vacío
    permisos = roles.get(rol, set())

    # Verifica que todas las acciones solicitadas estén permitidas
    return acciones <= permisos


print(validar_acciones("Ana", {"leer", "ver_logs", "exportar_reportes"}))


print("------------------2nda parte ejm2 --------------------")
#Determinar permisos exclusivos de cada rol
"""def permisos_exclusivos(roles): # SOLUCIÓN DE LA IA 
    # Verifica si existen roles
    if not roles:
        return "No hay roles registrados"

    for rol, permisos in roles.items():

        # Verifica si el rol no tiene permisos
        if not permisos:
            print(f"{rol}: no tiene permisos")
            continue

        otros_permisos = set()

        # Reúne los permisos de todos los demás roles
        for otro_rol, permisos_rol in roles.items():
            if otro_rol != rol:
                otros_permisos.update(permisos_rol)

        # Permisos que pertenecen únicamente a este rol
        exclusivos = permisos - otros_permisos

        if exclusivos:
            print(f"{rol}: {exclusivos}")
        else:
            print(f"{rol}: no tiene permisos exclusivos")
            
#ejemplos de funcionamiento 
# Ejemplo 1: revisar todos los roles
print("Ejemplo 1:")
permisos_exclusivos(roles)


# Ejemplo 2: agregar un rol sin permisos
print("\nEjemplo 2:")

roles_prueba = roles.copy()
roles_prueba["invitado"] = set()

permisos_exclusivos(roles_prueba)


# Ejemplo 3: probar un conjunto de roles vacío
print("\nEjemplo 3:")

roles_vacios = {}

permisos_exclusivos(roles_vacios)"""

#Solución de profe
for nombre, permisos in roles.items():  # Recorre todos los roles y sus permisos
    otros_permisos = set()  # Guarda los permisos que tienen los demás roles

    for otro_nombre, otros in roles.items():
        # Evita comparar el rol consigo mismo
        if otro_nombre != nombre:
            otros_permisos = otros_permisos | otros  # Une los permisos de los otros roles

        # Obtiene los permisos que solo pertenecen a este rol
        exclusivos = permisos - otros_permisos

    if exclusivos:
        print(f"Los permisos exclusivos del rol {nombre} son {exclusivos}")
    else:
        print(f"El rol {nombre} no tiene permisos exclusivos")


#tercera parte : listas y conjuntos 
print("-------------------3era parte----------------------")
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        # Cada nodo guarda un dato y una referencia al siguiente nodo


class Conjunto:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0
        # La cabeza apunta al primer elemento del conjunto
        # tamaño indica cuántos elementos hay actualmente

    def esta_vacio(self):
        # Si la cabeza es None, significa que no hay ningún nodo
        return self.cabeza is None

    def cardinalidad(self):
        # Retorna la cantidad de elementos que tiene el conjunto
        return self.tamaño

    def pertenece(self, x):
        # Comenzamos a recorrer desde el primer nodo
        actual = self.cabeza

        while actual:
            # Comparamos el dato del nodo actual con el elemento buscado
            if actual.dato == x:
                return True

            # Pasamos al siguiente nodo
            actual = actual.siguiente

        # Si recorremos todos los nodos y no lo encontramos
        return False

    def agregar(self, x):
        # Primero verificamos que el elemento no exista
        # para evitar elementos repetidos
        if self.pertenece(x):
            return False

        # Creamos un nuevo nodo con el elemento
        nuevo = Nodo(x)

        # El nuevo nodo apunta a la cabeza actual
        nuevo.siguiente = self.cabeza

        # Ahora el nuevo nodo se convierte en la cabeza
        self.cabeza = nuevo

        # Aumentamos la cantidad de elementos
        self.tamaño += 1

        return True

    def eliminar(self, x):
        # Si el conjunto está vacío, no hay nada que eliminar
        if self.esta_vacio():
            return False

        # Caso especial: el elemento que queremos eliminar
        # se encuentra en el primer nodo
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True

        # Comenzamos a recorrer desde la cabeza
        actual = self.cabeza

        # Buscamos el nodo que está antes del elemento que queremos eliminar
        while actual.siguiente:

            if actual.siguiente.dato == x:
                # Saltamos el nodo que queremos eliminar
                # y lo conectamos directamente con el siguiente
                actual.siguiente = actual.siguiente.siguiente

                self.tamaño -= 1
                return True

            # Avanzamos al siguiente nodo
            actual = actual.siguiente

        # Si llegamos aquí, el elemento no existe en el conjunto
        return False

    def mostrar(self): #para que se vea mejor la impresion 
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("{" + ",".join(elementos) + "}")


    def union(self, otro):
        # Creamos un conjunto vacío para guardar el resultado
        resultado = Conjunto()

        # Recorremos el primer conjunto
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        # Recorremos el segundo conjunto
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado


    def interseccion(self, otro):
        # Creamos un conjunto para guardar los elementos en común
        resultado = Conjunto()

        # Recorremos el conjunto actual
        actual = self.cabeza
        while actual:
            # Verificamos si el elemento también está en el otro conjunto
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)

            actual = actual.siguiente

        return resultado


    def diferencia(self, otro):
        # Creamos un conjunto para guardar la diferencia
        resultado = Conjunto()

        # Comenzamos desde el primer elemento
        actual = self.cabeza

        while actual:
            # Agregamos los elementos que no están en el otro conjunto
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)

            actual = actual.siguiente

        return resultado


    def diferencia_simetrica(self, otro):
        # Obtiene los elementos exclusivos de cada conjunto
        # y luego une ambos resultados
        return self.diferencia(otro).union(otro.diferencia(self))
 

"""A = Conjunto() #prueba 2 
B = Conjunto()
A.agregar(10)
A.agregar(20)
A.agregar(30)
B.agregar(30)
B.agregar(40)
B.agregar(50)

C = A.union(B)
D = A.interseccion(B)
"""

"""c = Conjunto() #prueba 1 
c.agregar(10)
c.agregar(20)
c.agregar(30)
c.agregar(40)
c.mostrar()

c.eliminar(20)
c.eliminar(50)
c.mostrar()"""
    