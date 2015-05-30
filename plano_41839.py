from ponto_41839 import Ponto3D
from vetor_41839 import Vetor3D

TOLERANCIA_ZERO = 10.0 **(-10)

class ErroPontosColineares(Exception):
    pass


class Plano:
    
    def __init__(self, ponto1, ponto2, ponto3):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3
        vtr1_2 = Vetor3D(self.ponto2.get_x() - self.ponto1.get_x(), self.ponto2.get_y() - self.ponto1.get_y(), self.ponto2.get_z() - self.ponto1.get_z())
        vtr1_3 = Vetor3D(self.ponto3.get_x() - self.ponto1.get_x(), self.ponto3.get_y() - self.ponto1.get_y(), self.ponto3.get_z() - self.ponto1.get_z())
        normal = Vetor3D.externo(vtr1_2, vtr1_3)
        
        if(normal.comprimento() < TOLERANCIA_ZERO):
            raise ErroPontosColineares
       
        self.normal = normal
        
    def __str__(self):
        return "Plano(Ponto3D(" + str(self.ponto1.get_x()) + ", " + str(self.ponto1.get_y()) + ", " + str(self.ponto1.get_z())+ "), Ponto3D(" + str(self.ponto2.get_x()) + ", " + str(self.ponto2.get_y()) + ", " + str(self.ponto2.get_z()) + "), Ponto3D(" + str(self.ponto3.get_x()) + ", " + str(self.ponto3.get_y()) + ", " + str(self.ponto3.get_z()) + "), Vetor3D("  + str(self.normal.get_x()) + ", " + str(self.normal.get_y()) + ", " + str(self.normal.get_z()) + ")"
          
    def interceta_triangulo(self, reta):

        return lista 
    
        
if __name__ == "__main__":
    # teste ao construtor
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(2.0, 0.0, 0.0)
    c = Ponto3D(0.0, 2.0, 0.0)
    plano1 = Plano(a, b, c)
    print("Até aqui não foram lançadas exceções.")
    # teste a TOLERANCIA_ZERO
    print("TOLERANCIA_ZERO = " + str(TOLERANCIA_ZERO))
    # teste à exceção ErroPontosColineares
    try:
        plano2 = Plano(a, b, b)
    except ErroPontosColineares:
        print("Ao tentar definir-se o plano plano2 = Plano(a, b, b)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("A execução foi interrompida. plano2 não ficou definida.")
    # teste a __str__
    # a normal tem que apontar no sentido do eixo dos z’s
    # e tem que ter comprimento 1
    print(plano1)
                
            