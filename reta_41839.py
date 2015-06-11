from ponto_41839 import Ponto3D
TOLERANCIA_ZERO = 10.0 **(-10)

class ErroPontosCoicidentes(Exception):
    pass

class Reta:
    
    def __init__(self, origem, destino):
        
        self.origem = origem
        self.destino = destino
        
        vetor = destino - origem
        
        comprimento = vetor.comprimento()
        
        if abs (comprimento) < TOLERANCIA_ZERO:
            raise ErroPontosCoicidentes
        
        self.vetor_diretor = vetor.versor()
    
    def __str__(self):
        return "Reta(" + str(self.origem) + ", " + str(self.destino) + ", " + str(self.vetor_diretor) + ") "
