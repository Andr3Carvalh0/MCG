from ponto_41839 import Ponto3D
from cor_phong_41839 import CorPhong
from cor_rgb_41839 import CorRGB
from luz_41839 import LuzPontual
from imagem_41839 import Imagem
from vetor_41839 import Vetor3D

h = 215.0
n_pontos = 63

# teste adicional
luz_posicao = Ponto3D(1.0, 0.0, 1.0)
luz_i_ambiente = CorRGB(1.0, 1.0, 1.0)
luz_i_difusa = CorRGB(1.0, 1.0, 1.0)
luz_i_especular = CorRGB(1.0, 1.0, 1.0)
luz = LuzPontual(luz_posicao, luz_i_ambiente, luz_i_difusa, luz_i_especular)
olho = Ponto3D(-1.0, 0.0, 1.0)
k_ambiente = CorRGB(0.0, 0.0, 0.0)
k_difusa = CorRGB(0.0, 0.0, 0.0)
k_especular = CorRGB(0.9, 0.9, 0.9)
brilho = 100.0
k_ambiente.set_hsv(h, 1.0, 0.1)
k_difusa.set_hsv(h, 1.0, 0.8)
cor_phong = CorPhong(k_ambiente,k_difusa,k_especular, brilho)
imagem = Imagem(n_pontos, n_pontos)
incremento = 2.0 / n_pontos
normal = Vetor3D(0.0, 0.0, 1.0)
sombra = False
for m in range(n_pontos): # índice de linhas
    for n in range(n_pontos): # índice de colunas
        ponto = Ponto3D(-1.0 + n*incremento, 1.0 - m*incremento, 0)
        direcao_luz = (luz.posicao - ponto).versor()
        direcao_olho = (olho - ponto).versor()
        cor = cor_phong.get_cor_rgb(luz, direcao_luz, normal, direcao_olho, sombra)
        imagem.set_cor(m+1, n+1, cor)
        if( m== 15 and n == 50):
            print(cor)
        
    
imagem.guardar_como_ppm("cor_phong_adicional.ppm")