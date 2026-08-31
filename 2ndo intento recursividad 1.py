#SEGUNDO INTENTO YA VOLVIENDO EFICIENTE EL MALO usando memorizacion 
import time
def fibonacci (n): 
    if n <= 1:
        return n 
    return fibonacci(n -1) + fibonacci (n-2)

def fibonacci_memo(n, cache={}): # diccionario en python 
    if n in cache:
        return cache [n]

    if n <=1 :
        return n 


    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]



inicio = time.time()
print(f"El resultado es {fibonacci(45)}")
print (f"Se demoró: {time.time() - inicio}")

    