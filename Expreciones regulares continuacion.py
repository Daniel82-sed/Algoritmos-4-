import re 


texto = "gato, geto, gito, goto, guto, g4to, g--too"

resultado = re.findall(r"g..to", texto) # el punto es un comodin o un metacaracter 
# la r significa buscar un patron no un texto literal como antes 
print(resultado)

texto2 = "Python es genial"

if re.search (r"^genial", texto2):# el ^ significa validar desde el inicio 
    print("Empieza con genial")
else: 
    print("No empieza con genial")

#r"^pyhton$" el signo $ significa validar desde el final 
# . --> Representa cualquier caracter solo una vez
#^ --> Al inicio del texto 
# $ --> Al final del texto 
# * --> Un caracter puede estar cero o mas veces 
# +  --> Un caracter puede estar una o mas veces 
# ? --> Un caracter puede estar cero y una vez 
#{} --> Un caracter puede estar un numero definido de veces 
#[] --> Interbal en el abecedario se puede mayuscula [A-Z] o minuscula [a-z]
# \w --> representa todas las letras todos los numeros y el guion bajo
#\s espacio -- \d cualquier digito de 0-9 (esto se investigo de forma independiente)
#  aunque luego lo confirmo el profe
texto3 = "ac abc"
resultado3 = re.findall(r"ab*c", texto3 )
print (resultado3)


texto4 = "ac abc abbc abbbbbc"
resultado4 = re.findall(r"ab+c", texto4 )
print (resultado4)

texto5 = "ac abc abbc abbbbbc"
resultado5 = re.findall(r"ab?c", texto5 )
print (resultado5)

texto6 = "ac abc abbc abbbbbc"
resultado6 = re.findall(r"ab{2,}c", texto6 )
print (resultado6)

texto7 = "ac abc abbc abbbbbc aeec aefc adefffc "
resultado7 = re.findall(r"[a-d]", texto7 )
print (resultado7)

texto8 = "elperrofeliz@magagas.com " # ejemplo de validacion correo
resultado8 = re.findall(r"[a-z]+@[a-z]+\.[a-z]{2,}", texto8 )# el () para agrupar 
print (resultado8)

texto9= "elperroyanotanfeliz78@magagas.com"
resultado9 = re.findall(r"\w+@\w+\.\w{2,}", texto9 )
print (resultado9)

texto10 = "https://www.google.com/search "# el ? significa el ultimo es opciona como la s en https 
patron = r"(https?)://(www\.)?([\w\.-]+)(/.)*" # expresion para validar un URL
resultado10 = re.search(patron, texto10)
print (bool(resultado10))

"""#Reto: Crear expresión regular para vaidar en celular en Colombia 
#Tener en cuenta que la gente lo escribe de diferentes formas . Ejemplos :
# 3001234567
# 300 123 45 67 
# 300-123-45-67
# intento de solucion mia
textoDeReto =  "300 263 78 99"
patron2 = r"(3)(..)( -*)(..)( -*)(..)" 
resultadoReto = re.search(patron2, textoDeReto)
print(bool(resultadoReto))"""
#solucion del reto profe
patron2 = r"^3\d{2}[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}$"#solucion profe \d{n} = numero de 0-9 n cantidad
resuladoReto = bool(re.search(patron2, "300-123-45 67"))
print(resuladoReto)