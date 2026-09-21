#Clase Lunes 21 09 2026
#primera parte 
print ("------------------1ra parte ---------------------")
algoritmos = {"Ana", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena", "Ivan"}

bases_datos = {"Carlos", "Diana", "Juan", "Karen", "Gabriel", "Luis", "Maria"}

redes = {"Diana", "Eduardo", "Gabriel", "Karen", "Natalia", "Oscar", "Ivan"}

#estudiantes en una sola materia
print ((algoritmos - bases_datos - redes)| (bases_datos - algoritmos - redes) | (redes - algoritmos - bases_datos))

# segunda parte
print ("------------------ 2nda parte ---------------------")

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

# imprimir las peliculas con al menos 2 generos en comun 

# Primero, se obtiene una lista con los nombres de todas las películas
# que están almacenadas como claves en el diccionario "catalogo".
peliculas = list(catalogo.keys())

# Se recorre cada película para compararla con las demás.
for i in range(len(peliculas)):

    # Se recorre nuevamente la lista empezando desde la película
    # siguiente a la actual, evitando comparar una película consigo misma
    # y evitando repetir comparaciones.
    for j in range(i + 1, len(peliculas)):

        # Se guardan los nombres de las dos películas que se van a comparar.
        p1, p2 = peliculas[i], peliculas[j]

        # Se obtiene la intersección de los conjuntos de géneros de ambas
        # películas. Esto permite saber qué géneros tienen en común.
        comunes = catalogo[p1] & catalogo[p2]

        # Si las dos películas tienen al menos 2 géneros en común,
        # se muestran sus nombres y los géneros que comparten.
        if len(comunes) >= 2:
            print(f"  {p1} <---> {p2}")
            print(f"Géneros en común:{comunes}")

# 3ra parte 
#ahora suponemos que tengo generos favoritos , porcentaje recomendacion de cada pelicula del catalogo
print(" ------------------- 3era parte --------------")
"""# Conjunto de géneros que le gustan al usuario # RESPUESTA DE UNA IA
favoritos = {"acción", "ciencia ficción", "aventura"}

# Recorremos cada película del catálogo junto con sus géneros
for pelicula, generos in catalogo.items():

    # Buscamos cuáles de los géneros favoritos están presentes
    # en los géneros de la película
    comunes = favoritos & generos

    # Calculamos el porcentaje de coincidencia.
    # Dividimos la cantidad de géneros en común entre la cantidad
    # total de géneros favoritos y multiplicamos por 100.
    porcentaje = (len(comunes) / len(favoritos)) * 100

    # Mostramos el nombre de la película y su porcentaje de coincidencia.
    # :.0f hace que el porcentaje aparezca sin decimales.
    print(f"{pelicula}: {porcentaje:.0f}%")
"""
#SOLUCIÓN DEL PROFE 
favoritos = {"acción", "ciencia ficción", "aventura"}

recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = favoritos & generos 

    if coincidencias:
        puntaje = len(coincidencias) / len(favoritos)
        recomendaciones.append((pelicula, puntaje * 100, coincidencias))

recomendaciones.sort(key=lambda x:x[1], reverse=True)
print(recomendaciones)

#   COMO SABER TODOS LOS GENEROS DEL CATALOGO
