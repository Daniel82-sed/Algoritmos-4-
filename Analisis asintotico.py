#Lunes 19 | 10 | 2026 
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

#Martes 20 | 10 | 2026 
def funcion (n):
    for i in range(n):
        print(n) # 1
        a = 1 + n  # 1 
        b = a + 2 # 1 
        print (b) # 1 
#f(n)= (1 + 1 + 1 + 1 ) * n = 4n # las operaciones elementales valen como uno 
# f (n) = 4n ==> O(n) # Las constantes desaparecen a la hora de que ya es complejidad lineal 
#Regla clave : en notación Big O las constantes se eliminan 

def funcion2(n):
    for i in range(n):
        print(n) # 1
        a = 1 + n  # 1 
        b = a + 2 # 1 
        print (b) # 1
    for j in range(n + 10):
        print(n)
        d = a + n 
#f(n) = 4n + 2(n+10) = 4n + 2n = 6n ==> O(n) mientras sean dos ciclos separados sus procesos se suman 
# si es un ciclo dentro de otro se multiplica

def funcion3(n):
    for i in range(100000):
        for j in range(n):
            print (j)
#f(n) = (1 * n)*100000 = 100000n ==> O(n)
# si depende de una entrada constante al final es contante 

def funcion4(n):
     a = n * 2 
     b = a + 1  
     for i in range(b):
         for j in range(n):
             print(j)
#f(n) = O(b*n) o tambien puede ser O(n^2)
# Aunque las constantes se ignoren para encontrar la complejidad no significa el mismo tiempo 
# las constantes cambian las vaces que se ejecuta un codigo 
# tener cuidado con lo que se demora despues de que dependa de una constante
# y cuando la constante depende de red o paralelismo 
# Big(O) en teoria  ignora las constantes pero en  el tiempo de carga las constantes no se pueden ignorar 
#Si tengo dos funciones seguidas se suman las dos complejidades 
# Si tengo dos se deja solo la mayor : Ejemplo : n^2 + n = O(n^2) Tomar la mayor en las sumas
def funcionLogaritmo(n):
    i = 1 
    while i < n:
        i = i * 2  # esta funcion es logaritmo por que cada vez que se ejecuta se reduce por 2
        # o por lo que se este multiplicando 
        #Cada iteración salta exponencialmente hacia arriba 
        # f(n) = O(log n)


