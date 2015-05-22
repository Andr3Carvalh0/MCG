from ponto_41839 import Ponto3D

class Reta:
    
    def __init__(self, origem, destino):
        
        self.origem = origem
        self.destino = destino
        
        vetor = destino - origem
        self.vetor_diretor = vetor.versor()
    
    def __str__(self):
        return "Reta(" + str(self.origem) + ", " + str(self.destino) + ", " + str(self.vetor_diretor) + ") "