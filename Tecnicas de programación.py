#Tecnicas de progrmación para mejorar codigos que tienen una complejidad grande 
#Aplicamos la memorización para que no calcule lo que ya calculo (fibonacci)
#Nos ayudamos de diccionarios debido a su complejidad O(1)
import time 


def fibonacci (n, memo={}): # memo = diccionario vacio
    if n <= 1:
        return n 
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
    
    
    

inicio = time.time()
print(f"El resultado es {fibonacci(45)}")
print (f"Se demoró: {time.time() - inicio}")