'''
Created on 22/2/2015

@author: Vanessa
'''
a= [("Vanessa Chipirras Navalon",657313509),("Mar Chipirras Navalon",635839757),("Carlos Falgueras Garcia",644595399),("Vanessa Chipirras Navalon",954061150),("Vanessa Chipirras Navalon",695426587)]

def agendaSimplificada(nombre, agenda):
    lista= ()
    for l in agenda:
        if l[0].count(nombre) == 1:
            lista= lista + l
    return lista
if __name__ == "__main__":
    print agendaSimplificada("Ca", a)
    print agendaSimplificada("Vanessa", a)
    print agendaSimplificada("Mar Chipirras Navalon", a)