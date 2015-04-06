'''
Created on 24/2/2015

@author: Vanessa
'''

class Corcho():
    '''
    classdocs
    '''
    def __init__(self, bodega):
        '''
        Constructor
        '''
        self.bodega= bodega
        print "El nombre de la bodega es:", bodega
        
class Botella():
    '''
    classdocs
    '''
    def __init__(self, Corcho):
        '''
        Constructor
        '''
        self.corcho = Corcho

class SacaCorcho():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.corcho = None
        
    def destapar(self,Botella):
        '''ni idea. Preguntar!!!'''
        '''mi_corcho = Corcho()'''
        self.corcho = Botella.corcho
        Botella.corcho = None
            
    def limpiar(self):
        self.corcho = None
            
            
            
if __name__ == "__main__":
    micorcho = Corcho("Vane")
    mibotella = Botella(micorcho)
    misacacorcho = SacaCorcho()
    print "mi botella aun tapada",mibotella.corcho
    misacacorcho.destapar(mibotella)
    print("la botella esta destapada:",mibotella.corcho)
    print "El corcho del sacacorcho:", misacacorcho.corcho
    misacacorcho.limpiar()
    print("El sacacorcho esta limpio:",misacacorcho.corcho)