'''
Created on 21/3/2015

@author: Vanessa Chipirrás Navalón
'''
from bs4 import BeautifulSoup
import urllib
import sqlite3
import tkMessageBox
from Tkinter import *


def obtenerWeb(web,nombre):
    urllib.urlretrieve(web, nombre)
    webObtenida = open(nombre,"r")
    webLeida = webObtenida.read()
    webObtenida.close()
    return webLeida

def recorrerWeb():
    html = obtenerWeb("http://www.sevillaguia.com/sevillaguia/agendacultural/agendacultural.asp", "SevillaCategorias")
    soup = BeautifulSoup(html)
    tablasDeHtml = soup.find_all("table")
    trDeHtml = tablasDeHtml[4].find_all("tr")
    bd = sqlite3.connect('prueba.db')
    cursor_agenda = bd.cursor()
    bdCreada = False
    try:
        cursor_agenda.execute("CREATE TABLE categorias(ident INTEGER PRIMARY KEY,categoria VARCHAR(40),nombre VARCHAR(40),enlace VARCHAR(100))")
    except:
        bdCreada = True
        print "Ya existe la base de datos PRUEBA"        
    i = 0
    tituloTemporal=""   
    listafinal={}
    for s in trDeHtml:
        lista = []
        tituloCategoria = s.find("font",{"class":"TituloIndice"})
        nombreSubCategoria = s.find("a",{"class":"LinkIndice"})
        
        if tituloCategoria:
            if not listafinal.has_key(tituloCategoria.string):
                listafinal[tituloCategoria.string] = []
                tituloTemporal = tituloCategoria.string
            else:
                lista = listafinal.get(tituloCategoria.string)
                
        if nombreSubCategoria:
            enlace = nombreSubCategoria.attrs["href"]
            titulo = nombreSubCategoria.string
            
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
    
    cursor = bd.execute("SELECT COUNT(*) FROM categorias")
    tkMessageBox.showinfo( "Base Datos", "Base de datos creada correctamente \nHay " + str(cursor.fetchone()[0]) + " registros")
    bd.close()

    
def buscar_bd():
    def listar_busqueda(event):
        conn = sqlite3.connect('prueba.db')
        conn.text_factory = str
        s = "%"+en.get()+"%" 
        cursor = conn.execute("""SELECT categoria,nombre,enlace FROM categorias WHERE categoria LIKE ?""",(s,))
        imprimir_etiqueta(cursor)
        conn.close()
    
    vBuscar = Toplevel()
    lbBuscar = Label(vBuscar, text="Introduzca categoria: ")
    lbBuscar.pack(side = LEFT)
    en = Entry(vBuscar)
    en.bind("<Return>", listar_busqueda)
    en.pack(side = LEFT) 
      
def imprimir_etiqueta(cursor):
    v = Toplevel()
    sc = Scrollbar(v)
    sc.pack(side=RIGHT, fill=Y)
    lb = Listbox(v, width=150, yscrollcommand=sc.set)
    for s in cursor:
            lb.insert(END,s[0])
            lb.insert(END,s[1])
            lb.insert(END,s[2])
            lb.insert(END,'')
    
    lb.pack(side = LEFT, fill = BOTH)
    sc.config(command = lb.yview)        
    

def ventana_principal():
    top = Tk()
    almacenar = Button(top, text="Almacenar", command = recorrerWeb)
    almacenar.pack(side = LEFT)
    #obtenerEventos = Button(top, text="BuscarEvento", command = obtener_evento)
    #obtenerEventos.pack(side = LEFT)
    Buscar = Button(top, text="Buscar", command = buscar_bd)
    Buscar.pack(side = LEFT)
    top.mainloop()
    
'''def obtenerEvento():
    html = obtenerWeb("http://www.sevillaguia.com/sevillaguia/agendacultural/agendacultural.asp", "SevillaCategorias")
    soup = BeautifulSoup(html)
    tablasDeHtml = soup.find_all("table")
    trDeHtml = tablasDeHtml[7].find_all("tr")
    wer = BeautifulSoup(trDeHtml)
    bd = sqlite3.connect('prueba.db')
    cursor_agenda = bd.cursor()
    bdCreada = False
    try:
        cursor_agenda.execute("CREATE TABLE eventos(ident INTEGER PRIMARY KEY,texto VARCHAR(1000))")
    except:
        bdCreada = True
        print "Ya existe la base de datos PRUEBA"        
    i = 0
    for s in wer.stripped_strings:
        print s
        cursor_agenda.execute("INSERT INTO eventos VALUES(?,?)",i,s)    
        i = i + 1
    bd.commit()
    bd.close()

'''  
if __name__ == '__main__':
    ventana_principal()
    #obtenerEvento()
