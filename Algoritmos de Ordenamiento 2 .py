#Clase 23 | 11 | 2026 
"""
QUICKSORT
Funciona con ayuda de un pivote de referencia , un numero y organiza los mayores a  la derecha 
y los menores a la izquierda y lo repite con todos hasta que queda organizado del todo 
- organiza uno por uno 
-el pivote es la ulltima posicion ya sea del arreglo o del sub arreglo generado despues de una ejecucion
-cuando se organizan datos semiorganizados o organizados es cuadratico 
-si es completamente aleatorio es n log n 
- no es estable ( no garantiza que respete el orden de dos que ya venian ordenados y eran iguales)
"""
"""
COUNTINGSORT
es para SOLO listas de numeros enteros
no compara 
complejidad lineal (super rapido pára arreglar una lista) = Temporal 
Tiene estabilidad 
1) encuentra el numero mayor y menor 
2) Encuentra un rango (numeros entre el menor y el mayor contandolos tambien a los dos)
3) Conteo : crea una lista de ceros de las mismas posiciones del rango ( entre 1 - 9 , rang 9 , cont = 9 posiciones)
"Cuenta los numeros repetidos cuantas veces se repite el 3 de las pos de la list conteo"
4) Por cada que haya un numero cuenta uno si encuentra el numero (Cantidad de veces que este en el arreglo original)
"Si hay numeros con mucha diferencia pero pocos no usar (mucho rango pocos numeros en el arreglo)
5)Acumulación: Empieza en la segunda posicion y le da el que hay ahi y le suma el anterior y sigue haciendolo 
6) Crea un arreglo de salida igual al de la entrada 
7) Recorre el arreglo original de derecha izquierda y es el numero menos el valor minimo  y esa posicion menos 1 y lo pone 
en esa posicion del arreglo de salida y le merma uno a la lista conteo en esa posicion 
 """

"""
RadixSort
"Es el countingSort pero mejorada la deficiecia del rango grande con pocos digitos " 
Cuenta con los digitos osea del 0 - 9 por lo que el counting siempre tiene 10 posiciones
1) saca el dif de 1 "Cuenta cuantas veces se repite cada ultimo digito ( para eso utiliza el mod 10 "el mod 10 siempre da el ultimo digito")
va primero en unidades luego decenas y centenas y asi ) 
2)Luego acumula y comienza a ordenarlos de acuerdo a sus unidades 
3) Queda organizado por las unidades y luego se vuelve al ciclo anterior pero ahora con dif 10 osea con las decenas
4) Vuelve a acumular y organiza por decenas 
5) lo mismo pero por dif 100 

"""