#Hacer un algoritmo que valide ai una palabra es palindromo (se lea igual en los dos sentidos (reconocer ))
def palindromo (s): # para recibir un string 
    if len(s) <= 1 :
        return True 

    if s[0]  != s[-1]:
        return False 

    return palindromo(s[1: -1])
print (palindromo ("reconocer"))
"""palabra = "computador
print (palabra [1: -1])  #slicing 
Este código en Python asigna una cadena de texto a una variable y luego utiliza una técnica llamada slicing (rebanado) para extraer y mostrar una sección específica de dicha palabra.

Desglose del código

palabra = "computador": Crea una variable llamada palabra y le asigna el texto "computador".

print(palabra[1:-1]): Imprime una subcadena extrayendo los caracteres desde una posición inicial hasta una final, bajo las siguientes reglas de los índices en Python:

El índice 1 indica que se debe comenzar a partir de la segunda letra (en este caso, la o, ya que el conteo empieza en 0).

El índice -1 indica que se debe llegar hasta el penúltimo carácter, ya que el límite superior en el slicing siempre se excluye (en este caso, excluye la r final).
resultado consola = omputado """

