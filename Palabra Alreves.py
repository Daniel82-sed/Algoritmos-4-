#palabra alreves 
def invetir (s):
    if len (s) <= 1 :
        return s 

    return invetir(s[1:]) + s[0]