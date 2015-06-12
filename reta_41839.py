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


if __name__ == "__main__":
    # teste ao construtor
    p1 = Ponto3D(0.0, 0.0, 0.0)
    p2 = Ponto3D(1.0, 2.0, 3.0)
    r1 = Reta(p1, p2)
    print("Até aqui não foram lançadas exceções.")
    # teste à exceção ErroPontosCoincidentes
    try:
        r2 = Reta(p2, p2)
    except ErroPontosCoicidentes:
        print("Ao tentar definir-se a reta r2 = Reta(p2, p2)")
        print("foi lançada a exceção ErroPontosCoincidentes.")
        print("A execução foi interrompida. r2 não ficou definida.")
        
        
    # teste a __str__
    print(r1)