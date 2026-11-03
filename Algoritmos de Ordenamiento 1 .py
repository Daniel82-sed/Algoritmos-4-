#Siempre saber tres cosas 
#Complejidad Espacial | Complejidad Temporal y 
#Estabilidad guardad el orden de las cosas iguales 
#----------------------------------------------------------
# ALGORITMO: Bubble Sort (Ordenamiento Burbuja)
# Consiste en comparar elementos adyacentes e intercambiarlos cuando
# están en el orden incorrecto. Este proceso se repite hasta que
# todos los elementos quedan ordenados de menor a mayor.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Los últimos i elementos ya están en su posición correcta.
        for j in range(0, n-i-1):
            # Compara dos elementos consecutivos.
            # Intercambia si el elemento actual es mayor que el siguiente.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1], arr[j]
    return arr

# COMPLEJIDAD ESPACIAL: O(1) - Utiliza memoria adicional constante.
# COMPLEJIDAD TEMPORAL:
# Mejor caso: O(n²).
# Caso promedio: O(n²).
# Peor caso: O(n²).
# ESTABILIDAD: ESTABLE - Conserva el orden relativo de los elementos iguales.
#------------------------------------------------------------------------------

# ALGORITMO: Insertion Sort (Ordenamiento por Inserción)
# Consiste en recorrer los elementos del arreglo e ir insertando cada uno
# en su posición correcta dentro de la parte que ya está ordenada.
# Funciona de manera similar a ordenar cartas en la mano.

def insertion_sort(arr):
    # Recorre desde el segundo elemento hasta el final.
    for i in range(1, len(arr)):

        # Guarda el elemento que se va a insertar en su posición correcta.
        key = arr[i]

        # Comienza a comparar con el elemento anterior.
        j = i - 1

        # Desplaza los elementos mayores que key una posición a la derecha.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Inserta key en su posición correspondiente.
        arr[j + 1] = key

    return arr

# COMPLEJIDAD ESPACIAL: O(1) - Utiliza memoria adicional constante.
#
# COMPLEJIDAD TEMPORAL:
# Mejor caso: O(n) - Cuando el arreglo ya está ordenado.
# Caso promedio: O(n²) - Cuando los elementos están desordenados.
# Peor caso: O(n²) - Cuando el arreglo está ordenado de mayor a menor.
#
# ESTABILIDAD: ESTABLE - Conserva el orden relativo de los elementos
# iguales, ya que solo desplaza elementos estrictamente mayores que key.

#--------------------------------------------------------------------------
# ALGORITMO: Merge Sort (Ordenamiento por Mezcla)
# Consiste en dividir el arreglo en partes cada vez más pequeñas
# hasta obtener elementos individuales. Luego, combina esas partes
# ordenándolas hasta formar nuevamente un arreglo completamente ordenado.

def merge_sort(arr):

    # Verifica si el arreglo tiene uno o ningún elemento.
    # En ese caso, ya está ordenado.
    if len(arr) <= 1:
        return arr

    # Encuentra el punto medio del arreglo.
    mid = len(arr) // 2

    # Divide el arreglo en dos mitades.
    izquierda = arr[:mid]
    derecha = arr[mid:]

    # Ordena recursivamente cada una de las mitades.
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Combina las dos mitades ordenadas.
    return merge(izquierda, derecha)


# FUNCIÓN AUXILIAR: MERGE
# Combina dos listas ordenadas en una sola lista ordenada.

def merge(izquierda, derecha):

    resultado = []

    # Índices para recorrer ambas listas.
    i = 0
    j = 0

    # Compara los elementos de ambas listas y agrega
    # el menor al resultado.
    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agrega los elementos restantes de la lista izquierda.
    resultado.extend(izquierda[i:])

    # Agrega los elementos restantes de la lista derecha.
    resultado.extend(derecha[j:])

    # Retorna la lista combinada y ordenada.
    return resultado


# COMPLEJIDAD ESPACIAL: O(n) - Necesita memoria adicional
# para almacenar las listas divididas y combinadas.

# COMPLEJIDAD TEMPORAL:
# Mejor caso: O(n log n).
# Caso promedio: O(n log n).
# Peor caso: O(n log n).

# ESTABILIDAD: ESTABLE - Conserva el orden relativo de los
# elementos iguales porque utiliza <= al realizar las comparaciones.

"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izq = merge_sort(arr[:medio])
    der = merge_sort(arr[medio:])
    return mezclar(izq, der)
 
def mezclar(a, b):
    resultado, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i]); i += 1
        else:
            resultado.append(b[j]); j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado
"""
#-------------------------
# ALGORITMO: Bucket Sort (Ordenamiento por Cubetas)
# Consiste en distribuir los elementos de un arreglo en diferentes
# cubetas según sus valores. Después, se ordena cada cubeta por separado
# y finalmente se unen todas para obtener el arreglo ordenado.

def bucket_sort(arr):

    # Verifica si el arreglo está vacío.
    if len(arr) == 0:
        return arr

    # Encuentra el valor mínimo y máximo del arreglo.
    minimo = min(arr)
    maximo = max(arr)

    # Define la cantidad de cubetas que se utilizarán.
    cantidad = len(arr)

    # Crea las cubetas vacías.
    buckets = [[] for _ in range(cantidad)]

    # Distribuye los elementos en sus respectivas cubetas.
    for num in arr:

        # Calcula la posición de la cubeta según el valor del elemento.
        indice = int((num - minimo) / (maximo - minimo + 1) * cantidad)

        # Evita que el índice supere la cantidad de cubetas.
        indice = min(indice, cantidad - 1)

        # Agrega el elemento a su cubeta correspondiente.
        buckets[indice].append(num)

    # Ordena individualmente cada cubeta.
    # Aquí se puede utilizar cualquier otro algoritmo de ordenamiento,
    # como Insertion Sort, Bubble Sort o Quick Sort.
    # La complejidad temporal dependerá del algoritmo seleccionado.
    for bucket in buckets:
        bucket.sort()

    # Une todas las cubetas ordenadas en el arreglo original.
    resultado = []

    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


# COMPLEJIDAD ESPACIAL: O(n + k) - Necesita memoria adicional
# para almacenar los elementos distribuidos en las cubetas.
# n = cantidad de elementos y k = cantidad de cubetas.

# COMPLEJIDAD TEMPORAL:
# Mejor caso: O(n + k) - Cuando los elementos se distribuyen
# uniformemente y las cubetas contienen pocos elementos.
# Caso promedio: O(n + k) - Bajo una distribución uniforme,
# utilizando un algoritmo eficiente para ordenar cada cubeta.
# Peor caso: O(n²) - Si todos los elementos caen en una sola
# cubeta y se utiliza un algoritmo como Insertion Sort.

# ESTABILIDAD: DEPENDE DEL ALGORITMO UTILIZADO.
# Bucket Sort puede ser estable si conserva el orden de los elementos
# iguales al distribuirlos y utiliza un algoritmo estable para ordenar
# cada cubeta. También debe mantener el orden al unirlas.