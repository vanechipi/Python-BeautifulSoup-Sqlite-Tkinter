'''
Created on 9/3/2015

@author: Vanessa Chipirrás Navalón
'''
import urllib
import re
 
def obtenerWeb(web,nombre):
    urllib.urlretrieve(web, nombre)
    
def abrirArchivo(nombre):    
    f = open(nombre,"r")
    return f

def leerArchivo(archivo):
    res = archivo.read()
    return res

def cerrarArchivo(archivo):
    archivo.close()

def recorrerArchivo(archivo):
    lista = re.findall(r'\s*<div class="prod_name"><a href="(.*)">(.*)</a></div>\s*<div class="productprice">\s*(<font class="strike">(.*)</font>)?(.*)\s*.*' ,archivo)
    return lista

def encontrarProducto(lista, nombre):
    for e in lista:
        if nombre in e[1]:
            print 'Titulo: ' + e[1]
            print 'Link: ' + e[0]
            print 'Precio: '+ e[4] + '\n'
            

    
def formatearDatos(lista):
    for e in lista:
        if e[2] and e[3]:
            print 'Titulo: ' + e[1]
            print 'Link: ' + e[0]
            print 'Precio: '+ e[4] + '\n'
        
def introduceDatos():
    nombre = raw_input('Introduzca nombre producto: ')
    return nombre

if __name__ == '__main__':
    obtenerWeb("http://www.shoporganic.com/prod_detail_list/organic-gourmet-view-all/a","PORTADA")
    a = abrirArchivo("PORTADA")
    leido = leerArchivo(a)
    cerrarArchivo(a)
    print "------------------------- PARTE 1 ------------------------"
    listaDeDatos = recorrerArchivo(leido)
    formatearDatos(listaDeDatos)
    print "------------------------- PARTE 2 ------------------------"
    nombre = introduceDatos()
    encontrarProducto(listaDeDatos, nombre)
     
