#Hacer un algoritmo recursivo que sume los digistos de un número 
#Ejemplo : 123 --> 1+2+3 = 6 
"""# /  → División normal: devuelve un número decimal (float)
10 / 3   # 3.3333

# // → División entera: devuelve solo la parte entera del resultado
10 // 3  # 3

# %  → Módulo: devuelve el resto de la división
10 % 3   # 1"""

def suma_digitos(n):
    if n // 10 == 0 :
        return n 

    return (n%10) + suma_digitos (n//10)
print(suma_digitos(123))