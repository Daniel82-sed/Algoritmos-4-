class Pagina: 
    def __init__(self, url, tiempo, titulo):
        self.url = url 
        self.tiempo = tiempo 
        self.titulo = titulo 
        self.siguiente = None  # Apunta a la siguiente página


class historial:
    def __init__(self):
        self.inicio = None  # Inicio de la lista


    def visitar(self, url, tiempo, titulo):
        nueva = Pagina(url, tiempo, titulo)
        nueva.siguiente = self.inicio  # Apunta al antiguo inicio
        self.inicio = nueva  # Nueva página pasa a ser el inicio


    def tiempo_total(self, nodo):

        if nodo is None:  # Si llega al final
            return 0 

        return nodo.tiempo + self.tiempo_total(nodo.siguiente)  # Suma y continúa


    def buscar_por_dominio(self, texto):
        resultado = []

        self.buscar(self.inicio, texto, resultado)  # Inicia la búsqueda

        return resultado


    def buscar(self, nodo, texto, resultado):

        if nodo is None:  # Caso base
            return None
        
        if texto in nodo.url:
            resultado.append((nodo.url, nodo.tiempo, nodo.titulo))  # Guarda coincidencia

        return self.buscar(nodo.siguiente, texto, resultado)  # Continúa


    def eliminar(self, nodo, minimo):

        if nodo is None:  # Caso base
            return None 
        
        nodo.siguiente = self.eliminar(nodo.siguiente, minimo)  # Revisa el siguiente

        if nodo.tiempo < minimo:
            return nodo.siguiente  # Elimina la página

        return nodo  # Conserva la página
"""# Falta crear eliminar_rapidas(), que llame a eliminar()
# y actualice self.inicio con el resultado de la recursividad.
def eliminar_rapidas(self, minimo):
    self.inicio = self.eliminar(self.inicio, minimo)
def eliminar_rapidas(self, minimo):
    self.inicio = self.eliminar(self.inicio, minimo)
"""