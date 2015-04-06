#encoding: utf-8

'''
Created on 1/3/2015

@author: Vanessa
'''
cadena = "Esto es una cadena"

def ej1a(cadena):
    contador = 0
    
    for e in cadena:
        if contador < 2:
            print(e)
            contador = contador + 1
            
def ej1aop2(cadena):
    contador = 0
    nuevaCadena = ""
    
    for e in cadena:
        if contador < 2:
            nuevaCadena = nuevaCadena + e
            contador = contador + 1
    print("los dos primeros caracteres son: "+ nuevaCadena)
    
def ej1b(cadena):
    contador = 0
    nuevaCadena = ""
    for e in cadena:
        if len(cadena)-3 <= contador:
            nuevaCadena = nuevaCadena + e
        contador = contador + 1
    print("Los ultimos tres caracteres son: "+ nuevaCadena)
    
def ej1c(cadena):
    contador = 0
    nuevaCadena = ""
    
    for e in cadena:
        if contador%2 == 0:
            nuevaCadena = nuevaCadena + e
        contador =  contador + 1
    print("Estas son cada dos caracteres: "+ nuevaCadena)
    
def ej1d(cadena):
    contador = len(cadena)-1
    nuevacadena = ""
    while contador >= 0:
        nuevacadena = nuevacadena + cadena[contador]
        contador = contador - 1
    return nuevacadena

def ej1e(cadena):
    nuevaCadena=""
    
    for e in cadena:
        nuevaCadena = nuevaCadena + e
    nuevaCadena = nuevaCadena + ej1d(cadena)
    return nuevaCadena
            
if __name__ == "__main__":
    ej1a(cadena)
    ej1aop2(cadena)
    ej1b(cadena)
    ej1c(cadena)
    print("Cadena inversa: "+ ej1d(cadena))
    print("Cadena con reflejo: "+ ej1e(cadena))