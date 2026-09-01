def busqueda_binaria(lista, objetivo, inicio, fin):
    if inicio > fin:# si es asi es por que no se encontro 
        return -1
    medio = (inicio + fin) // 2 

    if objetivo == lista [medio]: # segundo caso base donde lo encuentra 
        return medio 
    elif objetivo < lista [medio]: #es como tener un if dentro de un else # lado izquierdo 
        return busqueda_binaria(lista, objetivo, inicio, medio -1)# lado izquierdo
    else:
        return busqueda_binaria(lista, objetivo, medio +1, fin )#lado derecho 
    
lista_nueva = [5, 7, 9, 12, 15, 20]# siempre tiene que estar en orden 
print(busqueda_binaria(lista_nueva, 15 , 0 , 5))#len(lista_nueva) en caso de no saber el tamaño exacto 
