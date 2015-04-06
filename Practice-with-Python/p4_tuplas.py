'''
Created on 22/2/2015

@author: Vanessa
'''
t = [("Chipirras","Vanessa","N."), ("Neira","Alvaro","A."), ("Lopez","Juana","M."), ("Alonso","Rocio","V."), ("Garcia","Mario","G.")]

def campanaListas(var):

    for l in var:
        res= [l[1],l[2],l[0]]
        print res


if __name__ == "__main__":
    print "--------------------"
    campanaListas(t)
