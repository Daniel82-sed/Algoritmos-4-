#clase 15 9 2026 
import re 

#programacion regular con expresiones regulares 
def validar_cont(password):
    if len(password) < 8 :
        return False, "Minimo 8 caracteres"
    if not re.search(r"[A-Z]", password):
        return False, "Falta mayúscula"

    if not re.search(r"[a-z]", password):
        return False, "Falta minúscula"

    if not re.search(r"\d", password):
        return False, "Falta número"

    if not re.search(r"[!@#$%&/-_]", password):
        return False, "Falta caracter especial"

    return True, "Contraseña Válida"

#continuacion del codigo de la validacion del correo (otra version mas completa o válida)
patron = r"^[\w.+-]+@[A-Za-z\d-]+(\.[a-zA-Z\d-]+)?\.[A-Za-z]{2,}$"#\. la ralla es escapeado para que el punto solo signifique punto 
correo = "perritofeliz85@magagas.edu.co"

print(bool(re.match(patron, correo)))

#Valide de una fecha en formato DD/MM/AAA o DD-MM-AAAA |(or)
#primer intento propio 
#patronFecha = r"^[\d{2,}]+/||[\d{2,}]+ /||[\d{4,}]$" # mi intento funciona pero no tiene limitacion ante fecha irreales 
#patronFecha = r"^(0[1-9]|[12]\d|3[01])([/|])(0[1-9]|1[0-2])\2\d{4}$" #patronn hecho por ia
#solucion profe 
patronFecha = r"^(0[1-9]|[12]\d|3[01])[-/|](0[1-9]|1[0-2])[-/|](19|20)\d{2}$" # patron del profe 
fecha = "15/09/2026"
fecha2 = "15|09|2026"
fechaExagerada = "39|08|3022"
print(bool(re.match(patronFecha, fecha)))
print(bool(re.match(patronFecha, fecha2)))
print(bool(re.match(patronFecha, fechaExagerada)))

""" # codigo que valida años viciestos y desde 1900 hasta 2099 
import re
from datetime import datetime

patron = r"^(0[1-9]|[12]\d|3[01])([/|])(0[1-9]|1[0-2])\2(19\d{2}|20\d{2})$"

fecha = "29/02/2028"

if re.match(patron, fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        print(True)
    except ValueError:
        print(False)
else:
    print(False)
"""