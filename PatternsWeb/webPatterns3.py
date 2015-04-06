'''
Created on 5/3/2015

@author: Vanessa
'''
import urllib
import re

diccionario = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

def cargaPagina():
    
    f = urllib.urlretrieve("http://www.us.es/rss/feed/portada", "dato.us")
    a = open("dato.us","r")
    s = a.read()
    a.close()
    datos = re.findall(r'\s*<title>(.*)</title>\s*<link>(.*)</link>\s*.*\s*.*\s*(<category>.*</category>)?\s*.*\s*<pubDate>(.*)</pubDate>\s*',s)
    del datos[0]
    return datos

def sacarDatos(datos):
    for d in datos:
            
            datoF = "Fecha: "
            datoT = "Titulo: "
            datoL = "Link: "
            datoT = datoT + d[0]
            datoL = datoL + d[1]
            
            '''Imprimo por pantalla Titulo y Link'''
            
            print datoT
            print datoL
     
            '''Encuentro solo la fecha en la lista, me quedo con los numeros que quiero, busco en el diccionario el mes para pasarlo a numero e imprimo'''
        
            Dfecha = d[3]
            fecha = re.match(r'\s*...,\s*(\d\d)\s*(...)\s*(\d\d\d\d)\s*.*\s*', Dfecha)
            datoF = datoF + str(fecha.group(1))
            for l in diccionario:
                if l.count(fecha.group(2)) == 1:
                    datoF = datoF + "/" +diccionario[l]
                    datoF = datoF + "/" + str(fecha.group(3))
                    print datoF+"\n"
                    
'''ejercicio 1B'''
                    
def sacarFechaPedida(fecha,datos):
    FechaP = fecha.split("-")
    FechaN = FechaP[0] + "/" + FechaP[1] + "/" + FechaP[2]
    existeONo = False
    
    
    for d in datos:
        '''Encuentro solo la fecha en la lista, me quedo con los numeros que quiero, busco en el diccionario el mes para pasarlo a numero e imprimo'''
        datoF = "Fecha: "
        Dfecha = d[3]
        fecha = re.match(r'\s*...,\s*(\d\d)\s*(...)\s*(\d\d\d\d)\s*.*\s*', Dfecha)
        datoF = datoF + str(fecha.group(1))
            
        for l in diccionario:
            if l.count(fecha.group(2)) == 1:
                
                datoF = datoF + "/" +diccionario[l]
                datoF = datoF + "/" + str(fecha.group(3))

                if datoF.count(FechaN)== 1:
                    '''Imprimo por pantalla Titulo, Link y Fecha correspondiente si es la pedida'''
                    datoT = "Titulo: "
                    datoL = "Link: "
                    datoT = datoT + d[0]
                    datoL = datoL + d[1]
                    print datoT
                    print datoL
                    print datoF+"\n"
                    existeONo = True
    if existeONo == False:
        print "No existe fecha en nuestros datos"
    
def RequestDateUser():
    n = raw_input("Introduzca el mes (dd-mm-aaaa):")
    return n
     
if __name__ == '__main__':
    #sacarDatos(cargaPagina())
    sacarFechaPedida(RequestDateUser(), cargaPagina())