'''
Created on Jun 12, 2015

@author: Andre
'''
from plano_41839 import Plano
from ponto_41839 import Ponto3D
from cor_rgb_41839 import CorRGB
from cor_phong_41839 import CorPhong
from plano_41839 import ErroPontosColineares

class FaceTriangular(Plano):
    
    def __init__(self, ponto1, ponto2, ponto3, cor_phong):
        super().__init__(ponto1, ponto2, ponto3)
        self.cor_phong = cor_phong
    
    def __str__(self):
        return "Facetriangular("+super().__str__() + ", " + str(self.cor_phong) + ")"
    
    def get_cor_phong(self):
        return self.cor_phong
        
        
if __name__ == "__main__":        
    # teste ao construtor
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(1.0, 0.0, 0.0)
    c = Ponto3D(0.0, 1.0, 0.0)
    k_ambiente = CorRGB(0.0, 0.0, 0.1)
    k_difusa = CorRGB(0.0, 0.0, 0.75)
    k_especular = CorRGB(1.0, 1.0, 1.0)
    brilho = 100.0
    cor = CorPhong(k_ambiente, k_difusa, k_especular, brilho)
    face1 = FaceTriangular(a, b, c, cor)
    print("Até aqui não foram lançadas exceções.")
    try:
        face2 = FaceTriangular(a, a, c, cor)
    except ErroPontosColineares:
        print("Ao tentar definir-se a face face2 = FaceTriangular(a, a, c, cor)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("É o comportamento herdado da classe Plano.")
    
    # teste a __str__
    print(face1)
    
    print(face1.get_cor_phong())
    
    d = Ponto3D(1.0, 0.0, 0.0)
    e = Ponto3D(0.0, 0.0, 2.0)
    f = Ponto3D(0.0, 3.0, 0.0)
    g = Ponto3D(0.0, 0.0, 0.0)
    
    base = FaceTriangular(d,e,g,cor)
    lado_tras = FaceTriangular(f,e,g,cor)
    lado_esquerdo = FaceTriangular(d,f,g,cor)
    frente = FaceTriangular(d,e,f,cor)
    
    