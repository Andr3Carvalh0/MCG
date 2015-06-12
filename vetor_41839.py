
class Vetor3D:
    
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
        
        return "Vetor3D(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def adiciona(self, outro_vetor):
        
        x = self.x + outro_vetor.x
        y = self.y + outro_vetor.y
        z = self.z + outro_vetor.z
        
        resultado = Vetor3D(x, y, z)
        
        return resultado
    
    def __add__(self, outro_vetor):
        
        return self.adiciona(outro_vetor)
    
    def multiplica_escalar(self, escalar):
        
        x = self.x * escalar
        y = self.y * escalar
        z = self.z * escalar
        
        resultado = Vetor3D(x, y, z)
        
        return resultado
    
    def __mul__(self, escalar):
        
        return self.multiplica_escalar(escalar)
    
    def comprimento(self):
        
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5
    
    def versor(self):
        
        return self * (1.0/self.comprimento())
    
    def interno(self, outro_vetor):
        
        return (self.x * outro_vetor.x) + (self.y * outro_vetor.y) + (self.z * outro_vetor.z)
    
    def externo(self, outro_vetor):
        # a = self
        # b = outro_vetor
        
        ax = self.x
        ay = self.y
        az = self.z
        
        bx = outro_vetor.x
        by = outro_vetor.y
        bz = outro_vetor.z
    
        x = ay * bz - az * by   
        y = -(ax * bz - az * bx)
        z = ax * by - ay * bx
        
        return Vetor3D(x, y, z)
    
    
if __name__ == "__main__":
    # teste ao construtor
     v1 = Vetor3D(1.0, 2.0, 3.0)
     
     
     # teste a get_x
     print("coordenada x de v1 = ")
     print(v1.get_x())
    
    
    # teste a get_y
     print("coordenada y de v1 = ")
     print(v1.get_y())
    
    # teste a get_z
     print("coordenada z de v1 = ")
     print(v1.get_z())
     
     # teste a __str__
     print("v1 = ")
     print(v1)
     
     
     # teste a adiciona
     v2 = Vetor3D(10.0, 20.0, 30.0)
     v3 = v1.adiciona(v2)
     print("v1 = ")
     print(v1)
     print("v2 = ")
     print(v2)
     print("v3 = ")
     print(v3)
     
     # teste a +
     v4 = v1 + v2
     print("v4 = ")
     print(v4)
     
     
     # teste a multiplica_escalar
     a = 2.0
     v5 = v1.multiplica_escalar(a)
     print("v5 = ")
     print(v5)
     
     
     # teste a *
     v6 = v1 * a
     print("v6 = ")
     print(v6)
     
     
     # teste a comprimento
     v7 = Vetor3D(3.0, 0.0, 4.0)
     cv7 = v7.comprimento()
     print("v7 = ")
     print(v7)
     print("comprimento de v7 = ")
     print(cv7)
     
     
     # teste a versor
     vv7 = v7.versor()
     cvv7 = vv7.comprimento()
     print("vv7 = ")
     print(vv7)
     print("comprimento de vv7 = ")
     print(cvv7)
     
     
     # teste a interno
     print("v1 =")
     print(v1)
     print("v7 =")
     print(v7)  
     iv1v7 = v1.interno(v7)
     print("v1 interno v7 = ")
     print(iv1v7)
     
     # teste a externo
     e = v1.externo(v7)
     print("e = v1 externo v7 = ")
     print(e)
     print("v1 interno e = ")
     print(v1.interno(e))
     print("v7 interno e = ")
     print(v7.interno(e))