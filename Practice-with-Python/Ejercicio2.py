#encoding: utf-8

'''
Created on 1/3/2015

@author: Vanessa
'''
t= (1,3,6,7,15,16,17)

def ordenadosOno(t):
    esOrd = True
    cont = 0
    while cont < len(t)-1:
        if (t[cont] > t[cont+1]):
            esOrd =  False
            if esOrd == False:
                print("No esta ordenado")
                break
        cont = cont + 1
    if(esOrd == True):
        print("Esta ordenado de menor a mayor")
    
if __name__ == "__main__":
    ordenadosOno(t)
            