#encoding: utf-8
'''
Created on 19/2/2015

@author: Vanessa
'''
def separar(var, separador):
    print separador.join(var)

if __name__ == "__main__":
    separar("separacion",",")
    

def reemplazar(var, separador):
    lista = var.split()
    print lista
    print separador.join(lista)

if __name__ == "__main__":
    print "--------------------"
    reemplazar("mi archivo de texto.txt","_")
    
    
def reemplazar2(var):
    lista = ""
    for l in var:
        if l.isdigit():
            lista= lista + "X"
        else:
            lista = lista + l 
    return lista

if __name__ == "__main__":
    print "--------------------"
    print reemplazar2("Su clave es:1234")
    
def insertar(var):
    lista = ""
    cont = 0
    for l in var:
        if cont==2:
            lista= lista + l + "."
            cont = 0
        else:
            lista = lista + l
            cont =  cont + 1
        
    
    return lista

if __name__ == "__main__":
    print "--------------------"
    print insertar("2552552550")