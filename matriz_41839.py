class Matriz:

    def __init__(self, numero_linhas, numero_colunas):
        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas = []

        for m in range(numero_linhas):
            linha_com_zeros = []
            for n in range(numero_colunas):
                linha_com_zeros.append(0.0)
        
        self.linhas.append(linha_com_zeros)


    def __str__(self):
        
        resultado = "Matriz(" + str(self.numero_linhas) + ", " + str(self.numero_colunas) + ")\n"

        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado = resultado + str(self.linhas[l][c]) + " "
                resultado = resultado + "\n"
        
        return resultado

    def set_entrada(self, linha, coluna, valor):
        self.linhas[linha-1][coluna-1] = valor

    def get_entrada(self, linha, coluna):
        return self.linhas[linha-1][coluna-1]

    def adiciona(self, outra_matriz):
        resultado = Matriz(self.numero_linhas,self.numero_colunas)

        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                valor = self.linhas[l][c] + outra_matriz.linhas[l][c]
                resultado.linhas[l][c] = valor

        return resultado

    def __add__(self, outra_matriz):
        return self.adiciona(outra_matriz)

    def transposta(self):
        """Retorna a matriz transposta."""
        # falta implementar este método

    def multiplica(self, outra_matriz):
        resultado = Matriz(self.numero_linhas,
        outra_matriz.numero_colunas)
        
        for l in range(resultado.numero_linhas):
            for c in range(resultado.numero_colunas):
                valor = 0.0

        for n in range(self.numero_colunas):
            valor = valor + self.linhas[l][n] * outra_matriz.linhas[n][c]
            resultado.linhas[l][c] = valor
        return resultado


    def multiplica_escalar(self, escalar):
        resultado = Matriz(self.numero_linhas, self.numero_colunas)
    
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                resultado.linhas[l][c] = self.linhas[l][c] * escalar
    
        return resultado

    def __mul__(self, valor):

        if isinstance(valor, Matriz):
            return self.multiplica(valor)
        else:
            return self.multiplica_escalar(valor)

    def det_2x2(self):
        a = self.linhas[0][0]
        b = self.linhas[0][1]
        c = self.linhas[1][0]
        d = self.linhas[1][1]

        return a*d - b*c

    def det_3x3(self):
        a = self.linhas[0][0]
        b = self.linhas[0][1]
        c = self.linhas[0][2]
        d = self.linhas[1][0]
        e = self.linhas[1][1]
        f = self.linhas[1][2]
        g = self.linhas[2][0]
        h = self.linhas[2][1]
        i = self.linhas[2][2]
        
        return a*e*i + b*f*g + d*h*c - c*e*g - b*d*i - h*f*a

    def sub_matriz(self, linha_a_remover, coluna_a_remover):
        resultado = Matriz(self.numero_linhas-1, self.numero_colunas-1)

        for l in range(resultado.numero_linhas):
            for c in range(resultado.numero_colunas):
                lindex = l
                cindex = c

                if l >= linha_a_remover-1:
                    lindex = l + 1
                if c >= coluna_a_remover-1:
                    cindex = c + 1
                    resultado.linhas[l][c] = self.linhas[lindex][cindex]
                return resultado
    
    def det(self):
        if self.numero_linhas == 1:
            return self.linhas[0][0]
        elif self.numero_linhas == 2:
            return self.det_2x2()
        elif self.numero_linhas == 3:
            return self.det_3x3()
        else:
            resultado = 0.0
        for n in range(self.numero_colunas):
            resultado = resultado + (-1)**n * self.linhas[0][n] * self.sub_matriz(1,n+1).det()
    
        return resultado

    def copia(self):
        """Retorna uma cópia da matriz."""
        print("hel")
        # falta implementar este método

    def set_linha(self, linha, uma_lista):
        print("hel")
        # falta implementar este método

    def set_coluna(self, coluna, uma_lista):
        # falta implementar este método
        print("hel")