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
        resultado = Matriz(self.numero_colunas, self.numero_linhas)
        
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                
                resultado.linhas[c][l] = self.linhas[l][c]
        
        return resultado

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
         
        return a*e*i + b*f*g + d*h*c \
                - c*e*g - b*d*i - h*f*a

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
                resultado = resultado + ((-1)**n) * (self.linhas[0][n]) * (self.sub_matriz(1,n+1).det())            
            return resultado

    def copia(self):
        mCopia = Matriz(self.numero_linhas, self.numero_colunas)
        
        for l in range(self.numero_linhas):
            for c in range(self.numero_colunas):
                mCopia.linhas[l][c] = self.linhas[l][c]
        
        return mCopia
       
       
    def set_linha(self, linha, uma_lista):
        for c in range(len(uma_lista)):
            self.linhas[linha - 1][c] = uma_lista[c]
            
        return self
            
        
        

    def set_coluna(self, coluna, uma_lista):
        for l in range(len(uma_lista)):
            self.linhas[l][coluna - 1] = uma_lista[l]
            
        return self
        
if __name__ == "__main__":
    # teste ao construtor
    m1 = Matriz(3, 4)
    
    # teste a __str__
    print("Testes a __str__")
    print(m1)
    print("--------------------------------------------")
   
    # teste a set_entrada
    print("Testes a set_entrada")
    m1.set_entrada(1, 2, 1.0)
    m1.set_entrada(2, 2, 2.0)
    m1.set_entrada(3, 2, 3.0)
    print(m1)
    print("--------------------------------------------")
    
    # teste a get_entrada
    print("Testes a get_entrada")
    print("m1 entrada 3,1 = ")
    print(m1.get_entrada(3, 1))
    print("m1 entrada 3,2 = ")
    print(m1.get_entrada(3, 2))
    print("--------------------------------------------")
    
    # teste a adiciona
    print("Testes a adiciona")
    m2 = m1.adiciona(m1)
    print(m2)
    print("--------------------------------------------")
    
    # teste a +
    print("Testes a +")
    m3 = m1 + m1
    print(m3)
    print("--------------------------------------------")
    
    # teste a transposta
    print("Testes a transposta")
    m4 = m1.transposta()
    print(m4)
    print("--------------------------------------------")
    
    print("Testes a multiplica")
    # teste a multiplica
    m5 = m1.multiplica(m4)
    print(m5)
    print("--------------------------------------------")
    
    print("Testes a multiplica_escalar")
    # teste a multiplica_escalar
    m5a = m5.multiplica_escalar(-1.0)
    print(m5a)
    print("--------------------------------------------")
   
    print("Testes a *") 
    # teste a *
    m6 = m1 * m4
    print(m6)
    m6a = m1 * 2.0
    print(m6a)
    print("--------------------------------------------")

    print("Testes a det_2x2") 
    # teste a det_2x2
    m7 = Matriz(2, 2)
    m7.set_entrada(1, 1, 1.0)
    m7.set_entrada(1, 2, 2.0)
    m7.set_entrada(2, 1, 3.0)
    m7.set_entrada(2, 2, 4.0)
    print(m7)
    print("det(m7) = " + str(m7.det_2x2()))
    print("--------------------------------------------")

    print("Testes a det_3x3") 
    # teste a det_3x3
    print(m6)
    print("det(m6) = " + str(m6.det_3x3()))
    print("--------------------------------------------")

    print("Testes a sub_matriz") 
    # teste a sub_matriz
    m8 = m6.sub_matriz(2, 2)
    print(m8)
    print("--------------------------------------------")
    
    print("Testes a det") 
    # testes a det
    print(m7.det())
    print(m6.det())
    m9 = Matriz(5, 5)
    m9.set_entrada(1, 1, 2.0)
    m9.set_entrada(2, 2, 2.0)
    m9.set_entrada(3, 3, 2.0)
    m9.set_entrada(4, 4, 2.0)
    m9.set_entrada(5, 5, 2.0)
    print(m9)
    print(m9.det())
    print("--------------------------------------------")
   
    # testes a copia
    print("Testes a copia") 
    m10 = m7.copia()
    m10.set_entrada(1, 1, -2.0)
    print(m7)
    print(m10)
    print("--------------------------------------------")
   
    print("Testes a set_linha") 
    # teste a set_linha
    m9.set_linha(5, [1.0, 2.0, 3.0, 4.0, 5.0])
    print(m9)
    print("--------------------------------------------")
   
    print("Testes a set_coluna") 
    # teste a set_coluna
    m9.set_coluna(3, [10.0, 20.0, 30.0, 40.0, 50.0])
    print(m9)
    print("--------------------------------------------")
        
        