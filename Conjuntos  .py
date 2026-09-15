# Tema de cnjuntos 15 09 2026
print ("---------------Primera parte-------------- ")
elemento = 5
lista = [5, 6, 7, 8, 9]
if elemento in lista:
    print("Esta en la lista")#O(n) complejidad lineal 
#print (lista[2])


#conjunto solo tiene elementos no tiene orden ni elemetos repetidos ya que solo los vale una vez
conjunto = {5, 4, 3, 6, 8, 8} 
if elemento in conjunto:
    print("Esta en el conjunto")#O(1) complejidad constante (es mas eficiente al no tener que recorrer)


#print (conjunto)
#conjunto = set (lista)  # asi se pasa una lista a conjunto 
#b = list(set(a)) convierte de forma temporal en conjunto para eliminar los duplicados con la propiedad de los conjuntos 
#b = set(a) para que se convierta en conjunto 
#conjunto = set()  # esto es un conjunto vacio 
#diccionario = {}
# print (type(conjunto))# para saber que es algo 
"""
conjunto.add(5)
conjunto.remove(5) elimina pero si no esta muestra error
conjunto.discard(5) elimina pero si no esta no muestra error
conjunto.pop() elimina cualquiera  a la azar 

for num in comjunto :# sirve para iterar cada nuevo numero 
    print (num)
    
_---______----__--__----__-_-_--__---_-- # convertir un conjunto en lista
conjunto = {1, 2, 3, 4, 5}

lista = list(conjunto)

print(lista)

    """
print ("-------------Segunda Parte ---------------")
#reto sacar duplicados 
a = [5, 6, 7, 8, 9, 7, 4, 3, 2, 2]
b1 = list(set(a))
b = set(a)
print ( b, b1)

print ("-------------Tercera Parte ---------------")
# problema para aplicar de forma real 
print("----------------Ejemplo 1 _---------------")
# talleres estudiantes y disponibilidad de horario
taller1 = {"Ana", "Carlos", "Javier", "Lucia"}
taller2 = {"Lucia", "Maria", "Carlos", "Miguel"}
taller3 = {"Ana", "Javier", "José", "Miguel"}

"""estanVarios = taller1 & taller2 & taller3 
print (estanVarios)"""#muestra solo la interseccion en los tres como nadie esta en los tres pues no muestra nada
conflictos = (taller1 & taller2) | (taller2 & taller3) | (taller1 & taller3) # muestra quienes esta en minimo dos 
print(conflictos)

print ("---------------Ejemplo 2 ---------------")
#IPs sospechosas que se conectaron hoy fuera de la VPN 
#IPs  de la VPN que también están en lista sospechosa 
ips_sospechosas = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "10.0.0.1"}
ips_conectadas_hoy = {"1.1.1.1", "4.4.4.4", "10.0.0.1"}
ips_vpn_empresa = {"10.0.0.1", "10.0.0.2"}

sospechosas_fuera_vpn = (ips_sospechosas & ips_conectadas_hoy) - ips_vpn_empresa
sospechosas_en_vpn = ips_vpn_empresa & ips_sospechosas

print(sospechosas_fuera_vpn, sospechosas_en_vpn)
""""ips_hoy = {# ejemplo de ia 
    "192.168.1.10",
    "192.168.1.20",
    "10.0.0.5",
    "172.16.0.8"
}

ips_vpn = {
    "10.0.0.5",
    "172.16.0.8",
    "192.168.1.30"
}

ips_sospechosas = {
    "192.168.1.10",
    "10.0.0.5",
    "8.8.8.8"
}
ips_sospechosas_hoy_fuera_vpn = (
    ips_sospechosas & ips_hoy
) - ips_vpn

print(ips_sospechosas_hoy_fuera_vpn)
ips_vpn_sospechosas = ips_vpn & ips_sospechosas

print(ips_vpn_sospechosas)"""
print ("---------------Ejemplo 3 ---------------")
#Determinar si un rol en un subconjunto de otro 1 
#Calcular permisos minimos comunes a todos 2
#Permisos exclusivos del rol admin  3
rol_basico = {"Leer"}
rol_editor = {"Leer", "Crear", "Editar"}
rol_admmin  = {"Leer", "Crear", "Editar", "Eliminar", "Auditar"}

es_editor_sub_admin = rol_editor.issubset(rol_admmin)#1
print(es_editor_sub_admin) #1
print(rol_basico & rol_editor & rol_admmin)#2
print(rol_admmin - (rol_editor - rol_basico)) #3 


print ("----------------Ejemplo 4 --------------")
#Conjunto total de archivos activos 1
#2  Archivos presentes en todos los módulos (criticos)
#recordatorio
modA = {"app.py", "utils.py", "db.py"}
modB = {"db.py", "etl.py", "scheduler.py"}
modC = {"app.py", "cli.py", "db.py"}

print(modA | modB | modC)#1
print(modA & modB & modC)#2
# ============================================================
# OPERACIONES DE CONJUNTOS
# ============================================================
#
# En matemáticas, un conjunto es una colección de elementos.
# Por ejemplo:
#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# En Python podemos representar conjuntos usando set():
#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
#
# 1. UNIÓN
# ------------------------------------------------------------
# Matemáticamente:
#
# A ∪ B
#
# Contiene todos los elementos de A y B, sin repetir.
#
# A ∪ B = {1, 2, 3, 4, 5, 6}
#
# En Python:
#
# A | B
# A.union(B)
#
#
# 2. INTERSECCIÓN
# ------------------------------------------------------------
# Matemáticamente:
#
# A ∩ B
#
# Contiene únicamente los elementos que pertenecen a ambos
# conjuntos.
#
# A ∩ B = {3, 4}
#
# En Python:
#
# A & B
# A.intersection(B)
#
#
# 3. DIFERENCIA
# ------------------------------------------------------------
# Matemáticamente:
#
# A - B
#
# Contiene los elementos que están en A pero NO están en B.
#
# A - B = {1, 2}
#
# En Python:
#
# A - B
# A.difference(B)
#
# También podemos hacer B - A:
#
# B - A = {5, 6}
#
#
# 4. DIFERENCIA SIMÉTRICA
# ------------------------------------------------------------
# Matemáticamente:
#
# A △ B
#
# Contiene los elementos que pertenecen a A o a B,
# pero NO a ambos al mismo tiempo.
#
# A △ B = {1, 2, 5, 6}
#
# En Python:
#
# A ^ B
# A.symmetric_difference(B)
#
#
# 5. COMPLEMENTO / DIFERENCIA RESPECTO A UN UNIVERSO
# ------------------------------------------------------------
# Si tenemos un conjunto universal U:
#
# U = {1, 2, 3, 4, 5, 6, 7}
# A = {1, 2, 3, 4}
#
# El complemento de A se representa como:
#
# Aᶜ = U - A
#
# Aᶜ = {5, 6, 7}
#
# En Python podemos hacerlo mediante:
#
# U - A
#
#
# 6. SUBCONJUNTO
# ------------------------------------------------------------
# A es subconjunto de B si TODOS los elementos de A
# pertenecen también a B.
#
# Matemáticamente:
#
# A ⊆ B
#
# En Python:
#
# A.issubset(B)
# A <= B
#
#
# 7. SUPERCONJUNTO
# ------------------------------------------------------------
# B es superconjunto de A si contiene todos los elementos
# de A.
#
# Matemáticamente:
#
# B ⊇ A
#
# En Python:
#
# B.issuperset(A)
# B >= A
#
#
# 8. PERTENENCIA
# ------------------------------------------------------------
# Para saber si un elemento pertenece a un conjunto:
#
# Matemáticamente:
#
# x ∈ A
#
# En Python:
#
# x in A
#
# Para saber si NO pertenece:
#
# x ∉ A
#
# En Python:
#
# x not in A
#
#
# EJEMPLO COMPLETO
# ============================================================
#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# print(A | B)   # Unión:                {1, 2, 3, 4, 5, 6}
# print(A & B)   # Intersección:         {3, 4}
# print(A - B)   # Diferencia:           {1, 2}
# print(B - A)   # Diferencia:           {5, 6}
# print(A ^ B)   # Diferencia simétrica: {1, 2, 5, 6}
#
# print(2 in A)          # True
# print(7 in A)          # False
# print(A.issubset(B))   # False
#
# ============================================================
# ============================================================
# SUBCONJUNTOS Y RELACIONES ENTRE CONJUNTOS
# ============================================================
#
# A = {1, 2}
# B = {1, 2, 3, 4}
#
# SUBCONJUNTO:
# A ⊆ B → todos los elementos de A están en B.
# Python: A.issubset(B)  o  A <= B
#
# SUPERCONJUNTO / CONJUNTO MADRE:
# B ⊇ A → B contiene todos los elementos de A.
# Python: B.issuperset(A)  o  B >= A
#
# IGUALDAD:
# A = B → ambos conjuntos tienen exactamente los mismos elementos.
# Python: A == B
#
# DIFERENTES:
# A ≠ B → los conjuntos no tienen exactamente los mismos elementos.
# Python: A != B
#
# DISJUNTOS:
# A ∩ B = ∅ → no tienen ningún elemento en común.
# Python: A.isdisjoint(B)
#
# PERTENENCIA:
# x ∈ A → x pertenece al conjunto A.
# Python: x in A
#
# NO PERTENENCIA:
# x ∉ A → x no pertenece al conjunto A.
# Python: x not in A
#
# EJEMPLO:
# A = {1, 2}
# B = {1, 2, 3, 4}
# C = {5, 6}
#
# A <= B              # True → A es subconjunto de B
# B >= A              # True → B es superconjunto de A
# A == B              # False → son diferentes
# A.isdisjoint(C)     # True → no tienen elementos en común
# 2 in A              # True → 2 pertenece a A
# ============================================================
