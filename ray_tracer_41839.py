'''
Created on Jul 5, 2015

@author: andre
'''

from face_41839 import FaceTriangular
from luz_41839 import LuzPontual
from camara_41839 import Camara
from cor_rgb_41839 import CorRGB
from ponto_41839 import Ponto3D
from vetor_41839 import Vetor3D
from cor_phong_41839 import CorPhong
from imagem_41839 import Imagem
from reta_41839 import Reta

class ErroNaoPertence(Exception):
    pass

class RayTracer:

    def __init__(self, lista_faces, lista_luzes, camara, cor_fundo):
        
        #Detecao se os objectos percentem a devida classe.
        if not isinstance(lista_faces, list):
            ErroNaoPertence
        
        if not isinstance(lista_luzes, list):
            ErroNaoPertence
        
        for i in range (len(lista_faces)):
            if not isinstance(lista_faces[i], FaceTriangular):
                ErroNaoPertence
        
        for i in range (len(lista_faces)):
            if not isinstance(lista_luzes[i], LuzPontual):
                ErroNaoPertence
                
        if not isinstance(camara, Camara):
            ErroNaoPertence
            
        if not isinstance(cor_fundo, CorRGB):
            ErroNaoPertence
                
        #Inicializacao        
        self.lista_faces = lista_faces
        self.lista_luzes = lista_luzes
        self.camara = camara
        self.cor_fundo = cor_fundo
        
    def __str__(self):
        parcial = "RayTracer("
        
        #Prep. para as faces.
        for i in range (len(self.lista_faces)):
            parcial = parcial + self.lista_faces[i].__str__()
            
        parcial = parcial + "\n, \n"
        
        #Prep. para as luzes.
        for i in range (len(self.lista_luzes)):
            parcial = parcial + self.lista_luzes[i].__str__() 
        
        parcial = parcial + "\n, \n"
        
        #Prep. para a Camara.
        parcial = parcial + self.camara.__str__() + ",\n"
        
        #Prep. para a cor_fundo.
        parcial = parcial + self.cor_fundo.__str__() + "\n)"
        
        return parcial
    
    def renderiza(self):
        
        for m in range(self.camara.resolucao_vertical): # índice de linhas
            print("linha = "+ str(m) + " de " + str(self.camara.resolucao_vertical))
            
            for n in range(self.camara.resolucao_horizontal): # índice de colunas
                # a)
                posicao_camera = self.camara.posicao
                
                # b)
                posicao_ponto = self.camara.get_pixel_global(m, n)
                
                # c)
                reta = Reta(posicao_camera, posicao_ponto)
                
                # d)
                self.get_face_intercetada_mais_proxima(reta)
                
                
    def get_face_intercetada_mais_proxima(self, raio):
        #Agora que ja temos as 3 coordenadas, basta chamar a classe plano, e usar a funcao
        pass
    
    def get_cor_face(self, face, ponto_intercecao, direcao_olho):
        pass
    
    def get_cor_vista_por_raio (self, raio):
        pass
        
if __name__ == "__main__":
    # teste ao construtor
    # teste ao construtor - cor da face
    verde = CorRGB(0.0, 0.0, 0.4)
    brilho = 100.0
    cor_face = CorPhong(verde, verde, verde, brilho)
    
    # teste ao construtor - face
    p1 = Ponto3D(0.0, 0.0, 0.0)
    p2 = Ponto3D(-1.0, 0.0, 0.0)
    p3 = Ponto3D(0.0, -1.0, 0.0)
    face = FaceTriangular(p1, p2, p3, cor_face)
    lista_faces = [face]
    
    # teste ao construtor - luz
    branco = CorRGB(1.0, 1.0, 1.0)
    luz_posicao = Ponto3D(-1.0, 0.0, 2.0)
    luz = LuzPontual(luz_posicao, branco, branco, branco)
    lista_luzes = [luz]
    
    # teste ao construtor - camara
    camara_posicao = Ponto3D(0.0, 0.0, 2.0)
    olhar_para = Ponto3D(0.0, 0.0, 0.0)
    vertical = Vetor3D(0.0, 1.0, 0.0)
    distancia_olho_plano_projecao = 1.5
    largura_retangulo_projecao = 2.0
    altura_retangulo_projecao = 2.0
    resolucao_horizontal = 50
    resolucao_vertical = 50
    camara = Camara(camara_posicao, olhar_para, vertical, distancia_olho_plano_projecao, largura_retangulo_projecao, altura_retangulo_projecao, resolucao_horizontal, resolucao_vertical)
    
    # teste ao construtor - cor de fundo
    cor_fundo = CorRGB(0.3, 0.0, 0.0) # vermelho escuro
    # teste ao construtor - ray tracer
    ray_tracer = RayTracer(lista_faces, lista_luzes, camara, cor_fundo)       
    print(ray_tracer)
    print("\n")

                
                
