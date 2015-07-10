from cor_rgb_41839 import CorRGB
from luz_41839 import LuzPontual
from ponto_41839 import Ponto3D
from vetor_41839 import Vetor3D
from imagem_41839 import Imagem

class CorPhong:
    
    def __init__(self, k_ambiente, k_difusa, k_especular, brilho):
        
        self.k_ambiente = k_ambiente
        self.k_difusa = k_difusa
        self.k_especular = k_especular
        self.brilho = brilho
        
    def __str__(self):
        
        return "CorPhong(" + str(self.k_ambiente) + ", " + str(self.k_difusa) + ", " + str(self.k_especular) + ", " + str(self.brilho)+ ")"
    
    def get_cor_rgb(self, luz, direcao_luz, normal, direcao_olho, sombra):
        
        cor_ambiente = self.k_ambiente * luz.get_intensidade_ambiente()
        
        if(sombra == True):
            return cor_ambiente
        
        cos_N_L = normal.interno(direcao_luz)
        
        if(cos_N_L < 0.0):
            cos_N_L = 0.0
            
        cor_difusa = self.k_difusa * luz.get_intensidade_difusa() * (cos_N_L)
        
        R = direcao_luz * (-1.0) + normal * (2.0 * cos_N_L)
            
        cos_V_R = direcao_olho.interno(R)
            
        if(cos_V_R < 0.0):
            cos_V_R = 0.0 
            
        cor_especular = self.k_especular * luz.get_intensidade_especular() * (cos_V_R)**self.brilho
            
        resultado = cor_ambiente + cor_difusa + cor_especular
            
        return resultado
        
    
if __name__ == "__main__":
    print("teste ao construtor")
    material_k_ambiente = CorRGB(0.0, 0.0, 0.1)
    material_k_difusa = CorRGB(0.0, 0.0, 0.9)
    material_k_especular = CorRGB(1.0, 1.0, 1.0)
    material_brilho = 100.0
    material_cor = CorPhong(material_k_ambiente, material_k_difusa, material_k_especular, material_brilho)
    
    print()
    print("teste a __str__")
    print(material_cor)
            
    print()
    print("teste a get_cor_rgb")
    luz_posicao = Ponto3D(1.0, 0.0, 1.0)
    luz_intensidade_ambiente = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_difusa = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_especular = CorRGB(1.0, 1.0, 1.0)
    luz = LuzPontual(luz_posicao, luz_intensidade_ambiente, luz_intensidade_difusa,
    luz_intensidade_especular)
    olho = Ponto3D(-1.0, 0.0, 1.0)
    n_pontos = 100
    imagem = Imagem(100, 100)
    incremento = 0.02 # 2.0/100.0
    normal = Vetor3D(0.0, 0.0, 1.0)
    sombra = False
    for m in range(100): # índice de linhas
        for n in range(100): # índice de colunas
            ponto = Ponto3D(-1.0 + n*incremento, 1.0 - m * incremento, 0)
            direcao_luz = (luz.posicao - ponto).versor()
            direcao_olho = (olho - ponto).versor()
            cor = material_cor.get_cor_rgb(luz, direcao_luz, normal, direcao_olho, sombra)
            imagem.set_cor(m+1, n+1, cor)
    imagem.guardar_como_ppm("cor_phong.ppm")
        
        