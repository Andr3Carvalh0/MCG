from face_41839 import FaceTriangular
from luz_41839 import LuzPontual
from camara_41839 import Camara
from cor_rgb_41839 import CorRGB
from ponto_41839 import Ponto3D
from vetor_41839 import Vetor3D
from cor_phong_41839 import CorPhong
from ray_tracer_41839 import RayTracer

#Camara
camara_posicao = Ponto3D(0.0, 0.0, 1.0)
olhar_para = Ponto3D(0.0, 0.0, 0.0)
vertical = Vetor3D(0.0, 1.0, 0.0)
distancia_olho_plano_projecao = 1.0
largura_retangulo_projecao = 1.0
altura_retangulo_projecao = 1.0
resolucao_horizontal = 400
resolucao_vertical = 200
camara = Camara(camara_posicao, olhar_para, vertical, distancia_olho_plano_projecao, largura_retangulo_projecao, altura_retangulo_projecao, resolucao_horizontal, resolucao_vertical)

#Cor de Fundo
cor_fundo = CorRGB(0.0, 0.0, 0.0)

#Faces
####################### FACE 1 ####################### 
face1_ambiente = CorRGB(1.0, 0.0, 0.0)
face1_difusa = CorRGB(1.0, 0.0, 0.0)
face1_especular = CorRGB(1.0, 0.0, 0.0)
face1_brilho = 1000.0
cor_face1 = CorPhong(face1_ambiente, face1_difusa, face1_especular, face1_brilho)

face1_ponto1 = Ponto3D(-1.0, -1.0, -2.0) 
face1_ponto2 = Ponto3D(1.0, -1.0, -2.0)
face1_ponto3 = Ponto3D(-1.0, 1.0, -2.0)

face1 = FaceTriangular(face1_ponto1, face1_ponto2, face1_ponto3, cor_face1)


####################### FACE 2 ####################### 
face2_ambiente = CorRGB(0.25, 0.25, 0.25)
face2_difusa = CorRGB(0.25, 0.25, 0.25)
face2_especular = CorRGB(0.25, 0.25, 0.25)
face2_brilho = 1.0
cor_face2 = CorPhong(face2_ambiente, face2_difusa, face2_especular, face2_brilho)

face2_ponto1 = Ponto3D(0.0, -1.0, 1.0) 
face2_ponto2 = Ponto3D(2.0, -1.0, -2.0)
face2_ponto3 = Ponto3D(-2.0, -1.0, -2.0)

face2 = FaceTriangular(face2_ponto1, face2_ponto2, face2_ponto3, cor_face2)


####################### FACE 3 ####################### 
face3_ambiente = CorRGB(0.0, 0.0, 0.0).set_hsv(0.77, 1.0, 1.0)
face3_difusa = CorRGB(0.0, 0.0, 0.0).set_hsv(0.77, 1.0, 1.0)
face3_especular = CorRGB(0.0, 0.0, 0.0).set_hsv(0.77, 1.0, 1.0)
face3_brilho = 10.0
cor_face3 = CorPhong(face3_ambiente, face3_difusa, face3_especular, face3_brilho)

face3_ponto1 = Ponto3D(-0.73, -0.58, -0.87) 
face3_ponto2 = Ponto3D(0.43, 0.34, -1.85)
face3_ponto3 = Ponto3D(0.46, -0.64, -1.42)

face3 = FaceTriangular(face3_ponto1, face3_ponto2, face3_ponto3, cor_face3)


####################### FACE 4 ####################### 
face4_ambiente = CorRGB(0.0, 0.0, 0.0).set_hsv(88.53, 1.0, 1.0)
face4_difusa = CorRGB(0.0, 0.0, 0.0).set_hsv(88.53, 1.0, 1.0)
face4_especular = CorRGB(0.0, 0.0, 0.0).set_hsv(88.53, 1.0, 1.0)
face4_brilho = 10.0
cor_face4 = CorPhong(face4_ambiente, face4_difusa, face4_especular, face4_brilho)

face4_ponto1 = Ponto3D(0.32, -0.54, -0.45) 
face4_ponto2 = Ponto3D(0.24, -0.61, -0.58)
face4_ponto3 = Ponto3D(0.67, -0.28, -0.35)

face4 = FaceTriangular(face4_ponto1, face4_ponto2, face4_ponto3, cor_face4)


####################### FACE 5 ####################### 
face5_ambiente = CorRGB(0.0, 0.0, 0.0).set_hsv(54.19, 1.0, 1.0)
face5_difusa = CorRGB(0.0, 0.0, 0.0).set_hsv(54.19, 1.0, 1.0)
face5_especular = CorRGB(0.0, 0.0, 0.0).set_hsv(54.19, 1.0, 1.0)
face5_brilho = 10.0
cor_face5 = CorPhong(face5_ambiente, face5_difusa, face5_especular, face5_brilho)

face5_ponto1 = Ponto3D(-0.38, 0.21, -0.51) 
face5_ponto2 = Ponto3D(-0.12, -0.15, -1.12)
face5_ponto3 = Ponto3D(-0.64, 0.61, -0.39)

face5 = FaceTriangular(face5_ponto1, face5_ponto2, face5_ponto3, cor_face5)

lista_faces = [face1, face2, face3, face4, face5]
    
#Luz
luz_ambiente = CorRGB(0.1, 0.1, 0.1)
luz_difusa = CorRGB(0.75, 0.75, 0.75)
luz_especular = CorRGB(0.75, 0.75, 0.75)

luz1_posicao = Ponto3D(1.0, 1.0, -1.0)
luz2_posicao = Ponto3D(-1.0, 1.0, -1.0)

luz_1 = LuzPontual(luz1_posicao, luz_ambiente, luz_difusa, luz_especular)
luz_2 = LuzPontual(luz2_posicao, luz_ambiente, luz_difusa, luz_especular)

lista_luzes = [luz_1, luz_2]

#Ray Tracer
ray_tracer = RayTracer(lista_faces, lista_luzes, camara, cor_fundo)       
    
imagem = ray_tracer.renderiza()
imagem.guardar_como_ppm("projeto_41839.ppm")