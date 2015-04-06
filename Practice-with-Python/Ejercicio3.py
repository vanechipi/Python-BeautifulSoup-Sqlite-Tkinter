'''
Created on 2/3/2015

@author: Vanessa
'''
l=["Hola",3,10,7,"o","Hola",3,3]

def ej3a(lista, elemento):
    contador = 0
    
    for l in lista:
        if l == elemento:
            contador = contador + 1
               
    return contador

def eje3b(lista, elemento):
    contador = 0
    for l in lista:
        if l == elemento:
            break
        contador = contador + 1
    print "La posicion del elemento encontrado es: ",contador
    
def eje3c(l,elemento):
    nuevalista = []
    for e in l:
        nuevalista = nuevalista + eje3b(e, elemento)
    print"lista de posiciones de los elementos encontrados",nuevalista
    

if __name__ == "__main__":
    print"Cantidad de coincidencias encontradas:",ej3a(l, "Hola")
    eje3b(l, 7)
    eje3c(l, "Hola")