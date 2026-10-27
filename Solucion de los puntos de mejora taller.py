# punto 2.1 Ejercicio A 
def two_sum_ingenuo(nums, objetivo):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == objetivo:
                return (i, j)
    return None
# solucion propuesta por el profe 

def optimizado(nums, objetivo): # complejidad lineal, mejorado 
    vistos = {}
    for i, x in enumerate(nums):
        complemento = objetivo - x 
        if complemento in vistos: # hacer un in en una lista es lineal pero en diccionario es constante 
            return (vistos[complemento], i)
        vistos[x] = 1 
    return None


# pruebas 
import time 
inicio = time.time()
lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
optimizado(lista, 5)
print(inicio)

# punto 2.2 Ejercicio B 
def suma_maxima_ingenua(nums):
    n = len(nums)
    mejor = nums[0]
    for i in range(n):
        suma = 0
        for j in range(i, n):
            suma += nums[j]
            if suma > mejor:
                mejor = suma
    return mejor

def optimizadox2 (nums):
    actual = mejor = nums[0]

    for i in range (1, len(nums)):
        actual = max(nums[i], actual + nums[i])
        mejor = max(mejor, actual)
    return mejor


# pruebas 
nums1 = [ -2, 1, -3, 4, -1, 2 , 1 , -5, 4] 
print(suma_maxima_ingenua(nums1))
nums = [ -2, 1, -3, 4, -1, 2 , 1 , -5, 4] 
print(optimizadox2(nums))


# Fin del taller pero mas ejemplos 
"""codigos = [105, 203, 105, 410, 203, 520,105]

repetidos = []

for i in range (len(codigos)):
    for j in range (i+1, len(codigos)):
        if codigos[i] == codigos[j]:
            if codigos[i] not in repetidos:
                repetidos.append(codigos[i])
print("Codigos repetidos :", repetidos)""" # solución ineficiente cubico O (n ^ 3 )

"""codigos = [105, 203, 105, 410, 203, 520,105]
codigos = set(codigos)
repetidos = codigos & codigos
print( repetidos)""" # Mi intento 


#Solucion profe 
codigos = [105, 203, 105, 410, 203, 520,105]
vistos = set()
repetidos = set()

for codigo in codigos:
    if codigo in vistos:
        repetidos.add(codigo)
    else:
        vistos.add(codigo)

print(repetidos)

