from vetor_41839 import Vetor3D

class Ponto3D:
    
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        
    def get_x(self):
        
        return self.x
    
    def get_y(self):
        
        return self.y
    
    def get_z(self):
        
        return self.z
    
    def __str__(self):
        
        return "Ponto3D(" + str(self.get_x()) + ", " + str(self.get_y()) + ", " + str(self.get_z()) + ")"
        
    def adiciona_vetor(self, um_vetor):
        
        x = self.x + um_vetor.get_x()
        y = self.y + um_vetor.get_y()
        z = self.z + um_vetor.get_z()
        
        return Ponto3D(x, y, z)
    
    def __add__(self, um_vetor):
        
        return self.adiciona_vetor(um_vetor)
    
    def subtrai_ponto(self, ponto_inicial):
    
        x = self.x - ponto_inicial.get_x()
        y = self.y - ponto_inicial.get_y()
        z = self.z - ponto_inicial.get_z()
        
        return Vetor3D(x, y, z)
    
    def __sub__(self, ponto_inicial):
        
        return self.subtrai_ponto(ponto_inicial)
        