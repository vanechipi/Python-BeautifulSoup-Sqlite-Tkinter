'''
Created on 3/3/2015

@author: Vanessa
'''
    
def tuplas_a_diccionario(listaTuplas):
    diccionario = {}
    tupla = []
    for l in listaTuplas:
        clave = l[0]
        if diccionario.has_key(clave):
            tupla = diccionario[clave] + l[1]
            diccionario[clave] = tupla
        else:
            diccionario[clave] = l[1]
    print diccionario
        

if __name__ == "__main__":
    listaTuplas = [ ("Hola", "don Pepito"), ("Hola", "don Jose"), ("Buenos", "dias") ]
    tuplas_a_diccionario(listaTuplas)