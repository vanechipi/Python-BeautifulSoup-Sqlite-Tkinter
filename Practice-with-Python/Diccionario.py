#encoding: utf-8

'''
Created on 22/2/2015

@author: Vanessa
'''
#a= {"Vanessa Chipirras Navalon" : [657313509,954061150], "Mar Chipirras Navalon" : 635839757, "Carlos Falgueras Garcia" : 644595399}
a= {"Vanessa Chipirras Navalon" : 657313509, "Mar Chipirras Navalon" : 635839757, "Carlos Falgueras Garcia" : 644595399}

def agendaContinue(nombre, agenda):
    lista= []
    for l in agenda:
        if l.count(nombre) == 1:
            lista.append(l)
            lista.append(agenda[l])
    return lista   
    

def mostrar():

    l1 = raw_input("Introduzca nombre: ")
    if l1 != "*":
        res= agendaContinue(l1,a)
        print res
        if not res:
            print "Esta vacio"
            n = raw_input("Introduzca nombre y numero:")
            if n != "*":
                nombreynum= n.split(",")
                a[nombreynum[0]]= nombreynum[1]
                print a
        else: 
            print "Puedes modificarlo"
            #n = raw_input("Introduzca nuevo numero y posicion del que va a ser reemplazado:")
            n = raw_input("Introduzca nuevo numero:")
            if n != "*":
                #separar= n.split(" ")
                #indice= int(separar[1])
                telefonos =  res[1]
                #telefonos[indice]= separar[0]
                telefonos= n
                a[res[0]]=telefonos
                print a
        
        
if __name__=="__main__":
    mostrar()
