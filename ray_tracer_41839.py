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
from reta_41839 import Reta
from imagem_41839 import Imagem

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
        imagem = Imagem(self.camara.resolucao_vertical, self.camara.resolucao_horizontal)
        
        for m in range(self.camara.resolucao_vertical): # índice de linhas
            print("linha = "+ str(m+1) + " de " + str(self.camara.resolucao_vertical))
            
            for n in range(self.camara.resolucao_horizontal): # índice de colunas
                # a) Obtencao das coordenadas da camara
                posicao_camera = self.camara.posicao
                
                # b) Obtencao da posicao do ponto do plano de projecao, no sistema de coordenadas
                #    Globais
                posicao_ponto = self.camara.get_pixel_global(m, n)
                
                # c) Criar uma reta com origem na camara e fim no ponto de coordenadas globais
                reta = Reta(posicao_camera, posicao_ponto)
                
                # d) Obter cor vista pelo raio de visao
                cor_vista = self.get_cor_vista_por_raio(reta)
                
                # e) Guardar a cor na imagem
                imagem.set_cor(m+1, n+1, cor_vista)
        return imagem 
                
    def get_face_intercetada_mais_proxima(self, raio):
        ponto_intercepcao = None
        t = None
        face = None
        primeiro_valor = True
       
        #Interceta_triangulo devolve uma lista assim_ [True/False, ponto_intercepcao, t]
        #O 1 valor da lista indica se a reta intercepta ou nao a face
        #O 2 indica o ponto de intercepcao da reta no plano
        #O 3 indica a "distancia da reta po plano
        
        #Assim a 1 coisa a fazer seria um ciclo para varrer a lista de faces
        #Em cada face verificariamos o valor da posicao 0, para ver se a reta intercepta ou nao o plano
        #Se sim, iriamos comparar a face com a distancia mais pequena ja conhecida, com a face atual
        #Se a distancia for mais pequena, guardamos esta face
       
        for i in range(len(self.lista_faces)):
            #Se retomarmos uma lista com valor true, faremos a compraracao entre os diferentes valores de t
            if(self.lista_faces[i].interceta_triangulo(raio)[0]):
               
                if(t is None):
                    pass
                else:
                    if(self.lista_faces[i].interceta_triangulo(raio)[2] <= t and not primeiro_valor):
                        face = self.lista_faces[i]
                        ponto_intercepcao = self.lista_faces[i].interceta_triangulo(raio)[1]
                        t = self.lista_faces[i].interceta_triangulo(raio)[2]
                
                    elif(primeiro_valor):
                        face = self.lista_faces[i]
                        ponto_intercepcao = self.lista_faces[i].interceta_triangulo(raio)[1]
                        t = self.lista_faces[i].interceta_triangulo(raio)[2]
                        primeiro_valor = False
                    
        if(t is None):
            return [False, None, None, None]
        else:
            return [True, ponto_intercepcao, t, face]
        
        
    
    def get_cor_face(self, face, ponto_intercecao, direcao_olho):
        cor = None
        
        for i in range(len(self.lista_luzes)):
            #Obtemos a posicao da luz
            pos_luz = self.lista_luzes[i].posicao
            
            #Construimos uma reta com inicio na face e fim na posicao da luz
            reta = Reta(face, pos_luz) 
            
            direcao_luz = (pos_luz - face).versor()
            normal = Ponto3D(0.0,0.0,1.0)
            for m in range(len(self.lista_faces)):
                aux = self.lista_faces[m].cor_phong
                aux1 = CorPhong(aux)   
                
                #Se interceptar devolvemos a cor Phong em Sombra
                if(self.lista_faces[m].interceta_triangulo(reta)):
                    cor = cor + aux1.get_cor_rgb(self.lista_luzes[i], direcao_luz, normal, direcao_olho, True)
                else:
                    cor = cor + aux1.get_cor_rgb(self.lista_luzes[i], direcao_luz, normal, direcao_olho, False)
                
            
            
        return cor
    
    def get_cor_vista_por_raio (self, raio):
        face_mais_proxima = self.get_face_intercetada_mais_proxima(raio)
        
        #Se nao houver nenhuma face proxima devolvemos a cor de fundo
        if(face_mais_proxima[0] == False):
            return self.cor_fundo
        
        else:
            direcao_olho = (raio.origem - raio.destino).versor()
            cor_face = self.get_cor_face(face_mais_proxima[3], face_mais_proxima[1], direcao_olho)
            return cor_face
        
        
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
    #print(ray_tracer)
    #print("\n")

    # teste a renderiza
    imagem = ray_tracer.renderiza()
    imagem.guardar_como_ppm("teste1.ppm")
         
                
