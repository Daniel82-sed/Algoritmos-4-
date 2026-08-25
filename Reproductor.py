class Cancion:

    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo 
        self.artista = artista
        self.duracion = duracion

    def duracion_formateada(self):
        minutos = self.duracion // 60 # dif o diff  operacion para que solo entregue entero 
        segundos = self.duracion % 60 # mod operacion para que 