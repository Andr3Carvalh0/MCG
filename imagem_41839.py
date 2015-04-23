from io import StringIO
from cor_rgb_41839 import CorRGB

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
        string_dinamica.write(str(self.numero_colunas) + " " + str(self.numero_linhas) + "\n")
        string_dinamica.write("255\n")
        
        for linha in range(self.numero_linhas):
            for coluna in range(self.numero_colunas):
                pixel_string = str(self.linhas[linha][coluna])
                string_dinamica.write(pixel_string + " ")
                string_dinamica.write("\n")
        
        resultado = string_dinamica.getvalue()
        
        string_dinamica.close()
        
        return resultado

    def set_cor(self, linha, coluna, cor_rgb):

        self.linhas[linha-1][coluna-1] = cor_rgb

    def get_cor(self, linha, coluna):

        return self.linhas[linha-1][coluna-1]

    def guardar_como_ppm(self, nome_ficheiro):

        ficheiro = open(nome_ficheiro, 'w')
        ficheiro.write(str(self))
        ficheiro.close()
