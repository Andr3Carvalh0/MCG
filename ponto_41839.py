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
    
    
    
    
if __name__ == "__main__":
    # teste ao construtor
    p1 = Ponto3D(1.0, 2.0, 3.0)
    
    # teste a get_x
    print("coordenada x de p1 = ")
    print(p1.get_x())

    # teste a get_y
    print("coordenada y de p1 = ")
    print(p1.get_y())
    
    # teste a get_z
    print("coordenada z de p1 = ")
    print(p1.get_z())
    
    # teste a __str__
    print("p1 = ")
    print(p1)
    
    # teste a adiciona_vetor
    v1 = Vetor3D(10.0, 20.0, 30.0)
    p2 = p1.adiciona_vetor(v1)
    print("v1 = ")
    print(v1)
    print("p2 = ")
    print(p2)
    
    # teste a +
    p3 = p1 + v1
    print("p3 = p1 + v1 = ")
    print(p3)
    
    # teste a subtrai_ponto
    v2 = p2.subtrai_ponto(p1)
    print("v2 = ")
    print(v2)
    
    # teste a -
    v3 = p2 - p1
    print("v3 = ")
    print(v3)
    