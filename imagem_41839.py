from cor_rgb_41839 import CorRGB
from io import StringIO

class Imagem:

    def __init__(self, numero_linhas, numero_colunas):
        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas = []
        
        for n in range(numero_linhas):
            linha = []
            for m in range(numero_colunas):
                linha.append(CorRGB(0.0, 0.0, 0.0))
            self.linhas.append(linha)

    def __str__(self):
        string_dinamica = StringIO()
        string_dinamica.write("P3\n")
        string_dinamica.write("# mcg@leim@isel 2014/2015\n")
        string_dinamica.write(str(self.numero_colunas)
                              + " " + str(self.numero_linhas) + "\n")
        string_dinamica.write("255\n")

        for linha in range(self.numero_linhas):
            for coluna in range(self.numero_colunas):
                pixel_string = str(self.linhas[linha][coluna])
                string_dinamica.write(pixel_string + " ")
            string_dinamica.write("\n")

        resultado = string_dinamica.getvalue()
        string_dinamica.close()
        return (resultado)

    def set_cor(self, linha, coluna, cor_rgb):

        self.linhas[linha-1][coluna-1] = cor_rgb

    def get_cor(self, linha, coluna):

        return self.linhas[linha-1][coluna-1]

    def guardar_como_ppm(self, nome_ficheiro):

        ficheiro = open(nome_ficheiro, 'w')
        ficheiro.write(str(self))
        ficheiro.close()
   
    # testes
if __name__ == "__main__":
    # teste ao construtor
    imagem1 = Imagem(5, 5)
    # teste a __str__
    imagem2 = Imagem(5, 5)
    print(imagem2)
    # teste a set_cor
    imagem3 = Imagem(5, 5)
    branco = CorRGB(1.0, 1.0, 1.0)
    imagem3.set_cor(3, 3, branco)
    print(imagem3)
    # testes a get_cor
    imagem4 = Imagem(5, 5)
    branco = CorRGB(1.0, 1.0, 1.0)
    imagem4.set_cor(3, 3, branco)
    print(imagem4.get_cor(3, 3))
    print(imagem4.get_cor(5, 5))
    # teste a guardar_como_ppm
    imagem5 = Imagem(3, 5)
    red = CorRGB(1.0, 0.0, 0.0)
    green = CorRGB(0.0, 1.0, 0.0)
    blue = CorRGB(0.0, 0.0, 1.0)
    imagem5.set_cor(2, 2, red)
    imagem5.set_cor(2, 3, green)
    imagem5.set_cor(2, 4, blue)
    imagem5.guardar_como_ppm("imagem5.ppm")
    # teste adicional
    linhas = 100
    colunas = 200
    imagem6 = Imagem(linhas, colunas)
    h = 130.0
    incremento_s = 1.0 / (colunas - 1)
    incremento_v = 1.0 / (linhas - 1)
    for l in range(linhas):
        v = l * incremento_v
        for c in range(colunas):
            s = c * incremento_s
            pixel = CorRGB(0.0, 0.0, 0.0)
            pixel.set_hsv(h, s, v)
            imagem6.set_cor(l+1, c+1, pixel)
    imagem6.guardar_como_ppm("imagem6.ppm")
