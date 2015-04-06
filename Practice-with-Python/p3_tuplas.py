#encoding: utf-8

t = ("Vanessa", "Alvaro", "Juana", "Rocio")

def campanaNombres(var):
    for l in var:
        print "Estimad@",l+",","vote por mi"

if __name__ == "__main__":
    campanaNombres(t)

t = ("Vanessa", "Alvaro", "Juana", "Rocio")

def campanaNombresYPosicion(var, p):
    
    if p >= len(var):
        print "ERROR: Te has salido del tamaño"
        
    res= var[p:]
    
    for l in res:
            print "Estimad@",l+",","vote por mi"

if __name__ == "__main__":
    print "--------------------"
    campanaNombresYPosicion(t,2)

t = (("Vanessa","Mujer"), ("Alvaro","Hombre"), ("Juana","Mujer"), ("Rocio","Mujer"), ("Mario","Hombre"))


def campanaNombresPosicionYGenero(var, p):
  
    if p >= len(var):
        print "ERROR: Te has salido del tamaño"
        
    res= var[p:]
    
    for l in res:
            if l[1] == "Mujer":
                    print "Estimada",l[0]+",","vote por mi"
               
            elif l[1] == "Hombre":
                    print "Estimado",l[0]+",","vote por mi"

if __name__ == "__main__":
    print "--------------------"
    campanaNombresPosicionYGenero(t,2)