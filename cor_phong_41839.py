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
        
        return "CorPhong(" + str(self.k_ambiente) + ", " + str(self.k_difusa) + ", " + str(self.k_especular) + ", " + str(self.brilho)
    
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
        
        cor_especular = self.k_especular * luz.get_intensidade_especular()() * (cos_V_R)**self.brilho
        
        resultado = cor_ambiente + cor_difusa + cor_especular
        
        return resultado
        
        
        