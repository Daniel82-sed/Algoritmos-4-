#Tema nuevo ejemplo de complejidad de un sistemas : inicio de ejemplo en codigo
def ejemplo(n):
    print(n)
#f(n) = 1  # entrada 1 , algoritmos constante muy eficiciente pero poco real
#operación elemental 

def ejemplo2 (n):
    if n > 10 :
        print (n)
    else:
        print(n + 1)
#f(n) = 1 + 1 + 1 + 1 = 4 
#Sigue siendo un algoritmo constate  == > complejidad :     O(1) 
#no importa el numero ya que igual son constantes pero ojo misma complejidad no significa mismo tiempo
# Operaciones elementales son las que cuestan 1 

def ejemplo3 (n):
    for i in range(10):
        print(n)

#F(n) = 1 * 10 = 10 ==> O(1) 

def ejemplo4 (n):
    for i in range(n):
        print(n)
#F(n) = 1 * n = n ==> O(n) Complejidad n osea lineal 