import time 

def fibonacci (n):
    if n <= 1:
        return n 
    return fibonacci(n -1) + fibonacci (n-2)

inicio = time.time()
print(f"El resultado es {fibonacci(35)}")
print (f"Se demoró: {time.time() - inicio}")