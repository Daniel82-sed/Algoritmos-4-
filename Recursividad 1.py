import time 

def fibonnaci (n):
    if n <= 1:
        return n 
    return fibonnaci(n -1) + fibonnaci (n-2)

inicio = time.time()
print(f"El resultado es {fibonnaci(35)}")
print (f"Se demoró: {time.time() - inicio}")