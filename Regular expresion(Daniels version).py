import re 

texto = " holaaaa y wasaaaaaa"

resultado = re.match("holaaaa", texto)#encontrar al inicio 
print(resultado)

resultado = re.search("holaaaa", texto) # busca la palabra en todo el texto y devuelve la posicion 
print (resultado) 

resultado = re.findall("holaaaa", texto)#cuantas veces lo encontro 
print (resultado )