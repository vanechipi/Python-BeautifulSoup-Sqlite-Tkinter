'''
Created on 21/3/2015

@author: Vanessa Chipirrás Navalón
'''
from bs4 import BeautifulSoup
import urllib
import sqlite3

def obtenerWeb(web,nombre):
    urllib.urlretrieve(web, nombre)
    webObtenida = open(nombre,"r")
    webLeida = webObtenida.read()
    webObtenida.close()
    return webLeida

def recorrerWeb(html, nombreBd):
    soup = BeautifulSoup(html)
    tablasDeHtml = soup.find_all("table")
    trDeHtml = tablasDeHtml[4].find_all("tr")
    bd = sqlite3.connect(nombreBd + '.db')
    cursor_agenda = bd.cursor()
    bdCreada = False
    try:
        cursor_agenda.execute("CREATE TABLE categorias(ident INTEGER PRIMARY KEY,categoria VARCHAR(40),nombre VARCHAR(40),enlace VARCHAR(100))")
    except:
        bdCreada = True
        print "Ya existe la base de datos " + nombreBd.upper()        
    i = 0
    tituloTemporal=""   
    listafinal={}
    for s in trDeHtml:
        lista = []
        tituloCategoria = s.find("font",{"class":"TituloIndice"})
        nombreSubCategoria = s.find("a",{"class":"LinkIndice"})
        
        if tituloCategoria:
            #print "Categoria: " + tituloCategoria.string
            if not listafinal.has_key(tituloCategoria.string):
                listafinal[tituloCategoria.string] = []
                tituloTemporal = tituloCategoria.string
            else:
                lista = listafinal.get(tituloCategoria.string)
                
        if nombreSubCategoria:
            enlace = nombreSubCategoria.attrs["href"]
            titulo = nombreSubCategoria.string
            #print "\t" + "Seccion: " + titulo
            #print "\t" + "Enlace: " + enlace
            
            if not bdCreada:
                reg = (i, tituloTemporal, titulo, enlace)
                cursor_agenda.execute("INSERT INTO categorias VALUES(?,?,?,?)", reg)
                i = i + 1
                if listafinal.has_key(tituloTemporal):
                    lista = listafinal.get(tituloTemporal)
                    lista.append((titulo, enlace))
                    listafinal.update({tituloTemporal:lista})
                    
    if not bdCreada:
        bd.commit()
    
    print "Busca por categoria: "
    busqueda = raw_input()
    pr = cursor_agenda.execute("SELECT * FROM categorias")
    for s in pr:
        if busqueda.capitalize() == s[1]:
            print "Categoria: " + busqueda.capitalize()
            print "\t" + "Seccion: " + s[2]
            print "\t" + "Enlace: " + s[3] + "\n"
    bd.close()

if __name__ == '__main__':
    HTMLdeLaWeb = obtenerWeb("http://www.sevillaguia.com/sevillaguia/agendacultural/agendacultural.asp", "SevillaCategorias")
    recorrerWeb(HTMLdeLaWeb, 'prueba')
