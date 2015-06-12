from ponto_41839 import Ponto3D
from vetor_41839 import Vetor3D
from matriz_41839 import Matriz

class Camara:
    
    def __init__(self,posicao,olhar_para,vertical,distancia_olho_plano_projecao,largura_retangulo_projecao, altura_retangulo_projecao, resolucao_horizontal, resolucao_vertical):
        
        self.posicao = posicao
        self.olhar_para = olhar_para
        self.vertical = vertical
        self.distancia_olho_plano_projecao = distancia_olho_plano_projecao
        self.largura_retangulo_projecao = largura_retangulo_projecao
        self.altura_retangulo_projecao = altura_retangulo_projecao
        self.resolucao_horizontal = resolucao_horizontal
        self.resolucao_vertical = resolucao_vertical
       
        eixo_z = ((olhar_para - posicao).versor())
        eixo_y = (vertical + eixo_z * (-1.0 * vertical.interno(eixo_z))).versor()
        eixo_x = eixo_z.externo(eixo_y)
        
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.eixo_z = eixo_z
        
        incremento_horizontal = largura_retangulo_projecao / resolucao_horizontal
        incremento_vertical = altura_retangulo_projecao / resolucao_vertical
        
        self.incremento_horizontal = incremento_horizontal
        self.incremento_vertical = incremento_vertical
        
        canto_superior_esquerdo_x = -largura_retangulo_projecao / 2.0 + incremento_horizontal / 2.0
        canto_superior_esquerdo_y = altura_retangulo_projecao / 2.0 - incremento_vertical / 2.0
        canto_superior_esquerdo_z = distancia_olho_plano_projecao
        
        self.canto_superior_esquerdo_x = canto_superior_esquerdo_x
        self.canto_superior_esquerdo_y = canto_superior_esquerdo_y
        self.canto_superior_esquerdo_z = canto_superior_esquerdo_z
        
        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, self.eixo_x.x)
        matriz.set_entrada(2, 1, self.eixo_x.y)
        matriz.set_entrada(3, 1, self.eixo_x.z)
        matriz.set_entrada(4, 1, 0.0)
        
        matriz.set_entrada(1, 2, self.eixo_y.x)
        matriz.set_entrada(2, 2, self.eixo_y.y)
        matriz.set_entrada(3, 2, self.eixo_y.z)
        matriz.set_entrada(4, 2, 0.0)
        
        matriz.set_entrada(1, 3, self.eixo_z.x)
        matriz.set_entrada(2, 3, self.eixo_z.y)
        matriz.set_entrada(3, 3, self.eixo_z.z)
        matriz.set_entrada(4, 4, 0.0)
        
        matriz.set_entrada(1, 4, self.posicao.x)
        matriz.set_entrada(2, 4, self.posicao.y)
        matriz.set_entrada(3, 4, self.posicao.z)
        matriz.set_entrada(4, 4, 1.0)
        
        self.matriz = matriz
     
    def __str__(self):
        return "Camara(" + str(posicao) + ", \n" \
            + str(olhar_para) + ", \n"\
            + str(vertical) + ", \n"\
            + str(distancia_olho_plano_projecao) + ", \n"\
            + str(largura_retangulo_projecao) + ", \n"\
            + str(altura_retangulo_projecao) + ", \n"\
            + str(resolucao_horizontal) + ", \n"\
            + str(resolucao_vertical) + ", \n"\
            \
            + str(self.eixo_x) + ", \n"\
            + str(self.eixo_y) + ", \n"\
            + str(self.eixo_z) + ", \n"\
            \
            + str(self.incremento_horizontal) + ", \n"\
            + str(self.incremento_vertical) + ", \n"\
            + str(self.canto_superior_esquerdo_x) + ", \n"\
            + str(self.canto_superior_esquerdo_y) + ", \n"\
            + str(self.canto_superior_esquerdo_z) + ", \n"\
            \
            + str(self.matriz) + "\n"

            
        
    def get_pixel_local(self, linha, coluna):
        x = self.canto_superior_esquerdo_x + self.incremento_horizontal * (coluna - 1)
        y = self.canto_superior_esquerdo_y + self.incremento_vertical * (linha - 1)
        z = self.distancia_olho_plano_projecao
    
        pixel = Ponto3D(x,y,z)
        
        return pixel
    
    def local_para_global(self, ponto):
        m1 = Matriz(4,1)
        m1.set_entrada(1, 1, ponto.x)
        m1.set_entrada(2, 1, ponto.y)
        m1.set_entrada(3, 1, ponto.z)
        m1.set_entrada(4, 1, 1.0)
        
        m2 = self.matriz * m1
        
        p_global = Ponto3D(m2.get_entrada(1,1), m2.get_entrada(2,1), m2.get_entrada(3,1))
        
        return p_global
        
    
    def get_pixel_global(self, linha, coluna):
        p_local = self.get_pixel_local(linha, coluna)
        p_global = self.local_para_global(p_local)
        
        return p_global
        
     
if __name__ == "__main__":

    print("teste ao construtor")
    posicao = Ponto3D(0.0, 0.0, 3.0)
    olhar_para = Ponto3D(0.0, 0.0, 0.0)
    vertical = Vetor3D(0.0, 1.0, 0.0)
    distancia_olho_plano_projecao = 2.0
    largura_retangulo_projecao = 2.0
    altura_retangulo_projecao = 2.0
    resolucao_horizontal = 5
    resolucao_vertical = 5
    camara = Camara(posicao, olhar_para, vertical, distancia_olho_plano_projecao, largura_retangulo_projecao, altura_retangulo_projecao, resolucao_horizontal, resolucao_vertical)
    
    # teste a __str__
    print(camara)
    
    # teste a get_pixel_local
    print("sistema de coordenadas LOCAL")
    print("canto superior esquerdo = ")
    p1 = camara.get_pixel_local(1, 1)
    print(p1)
    print("canto superior direito = ")
    p2 = camara.get_pixel_local(1, 5)
    print(p2)
    print("canto inferior esquerdo = ")
    p3 = camara.get_pixel_local(5, 1)
    print(p3)
    print("canto inferioror direito = ")
    p4 = camara.get_pixel_local(5, 5)
    print(p4)
    
    # teste a local_para_global
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p1_global = camara.local_para_global(p1)
    print(p1_global)
    print("canto superior direito = ")
    p2_global = camara.local_para_global(p2)
    print(p2_global)
    print("canto inferior esquerdo = ")
    p3_global = camara.local_para_global(p3)
    print(p3_global)
    print("canto inferioror direito = ")
    p4_global = camara.local_para_global(p4)
    print(p4_global)
    
    # teste a get_pixel_global
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p5 = camara.get_pixel_global(1, 1)
    print(p5)
    print("canto superior direito = ")
    p6 = camara.get_pixel_global(1, 5)
    print(p6)
    print("canto inferior esquerdo = ")
    p7 = camara.get_pixel_global(5, 1)
    print(p7)
    print("canto inferioror direito = ")
    p8 = camara.get_pixel_global(5, 5)
    print(p8)
    
    