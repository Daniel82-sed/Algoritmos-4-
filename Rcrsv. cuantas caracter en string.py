"""hacer un algoritmo recursivo que reciba string y un caracter 
deber devolver el numero de veces que el caracter está en el string 
Ejemplo : alicia , catracter --> a, resultado = 2 """

def contar_caracter (s, c):
    if len(s) == 0:
        return 0 
    
    cuenta = 1 if s[0] == c else 0 

    return cuenta + contar_caracter(s[1:], c)# 1: --> significa desde la posicion 1 en adelante 
contar_caracter("alicia", "a")
print (contar_caracter("alicia", "a"))
"""def contar(lista, caracter):
    # Caso base: si la lista está vacía, ya no quedan
    # caracteres por revisar, así que devolvemos 0.
    if len(lista) == 0:
        return 0

    # Revisamos el primer elemento de la lista.
    # Si es igual al carácter que estamos buscando,
    # sumamos 1 y seguimos buscando en el resto de la lista.
    if lista[0] == caracter:
        return 1 + contar(lista[1:], caracter)

    # Si el primer elemento NO es el carácter que buscamos,
    # simplemente seguimos buscando en el resto de la lista.
    return contar(lista[1:], caracter)


# Palabra que queremos analizar
palabra = "banana"

# Convertimos el string en una lista de caracteres
lista = list(palabra)

# Llamamos a la función para contar cuántas "a" hay
resultado = contar(lista, "a")

# Mostramos el resultado
print(resultado)
 # ejemplo recursivo desde ia
"""