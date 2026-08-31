import time 
def factorial (n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i #resultado es igual a resultado por i , acumulado de i (resultado = resultado * i)

    return resultado 

inicio = time.time()
print(f"El resultado es {factorial(35)}")
print (f"Se demoró: {time.time() - inicio}")
