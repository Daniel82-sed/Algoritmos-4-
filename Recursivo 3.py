import  time


def factorial (n):
    if n <= 1 :
        return 1 

    return  n * factorial (n-1)
inicio = time.time()
print(f"El resultado es {factorial(35)}")
print (f"Se demoró: {time.time() - inicio}")


