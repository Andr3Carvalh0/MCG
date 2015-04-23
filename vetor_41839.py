
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
    
    def multiplicar_escalar(self, escalar):
        
        x = self.x * escalar
        y = self.y * escalar
        z = self.z * escalar
        
        resultado = Vetor3D(x, y, z)
        
        return resultado
    
    def __mul__(self, escalar):
        
        return self.multiplicar_escalar(escalar)
    
    def comprimento(self):
        
        return ((self.x)**2 + (self.y)**2 + (self.z)**2)**0.5
    
    def versor(self):
        
        return self * (1.0/self.comprimento())
    
    def interno(self, outro_vetor):
        
        return (self.x * outro_vetor) + (self.y * outro_vetor) + (self.z * outro_vetor)
    
    def externo(self, outro_vetor):
        
        return (self.x * outro_vetor) + (self.y * outro_vetor) + (self.z * outro_vetor)
    
    
    
        
        
        
    