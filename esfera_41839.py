'''
Created on Jul 5, 2015

@author: andre
'''

from cor_rgb_41839 import CorRGB

class Esfera:
    
    ##cor --> CorRGB
    def __init__(self, centro, raio, cor):
        self.centro = centro
        self.raio = raio
        self.cor = cor
    
    
    def intercepta(self, p):
        
        
         