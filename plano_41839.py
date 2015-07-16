from ponto_41839 import Ponto3D
from vetor_41839 import Vetor3D
from matriz_41839 import Matriz
from reta_41839 import Reta

TOLERANCIA_ZERO = 10.0 **(-10)

class ErroPontosColineares(Exception):
    pass


class Plano:
    
    def __init__(self, ponto1, ponto2, ponto3):
        vetor12 = ponto2 - ponto1
        vetor13 = ponto3 - ponto1

        vetor = vetor12.externo(vetor13)
        
        comprimento = vetor.comprimento()
        
        if(abs(comprimento) < TOLERANCIA_ZERO):
            raise ErroPontosColineares
               
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3
        self.normal = vetor.versor()
        
    def __str__(self):
        return "Plano(Ponto3D(" + str(self.ponto1.get_x()) + ", " + str(self.ponto1.get_y()) + ", " + str(self.ponto1.get_z())+ "), Ponto3D(" + str(self.ponto2.get_x()) + ", " + str(self.ponto2.get_y()) + ", " + str(self.ponto2.get_z()) + "), Ponto3D(" + str(self.ponto3.get_x()) + ", " + str(self.ponto3.get_y()) + ", " + str(self.ponto3.get_z()) + "), Vetor3D("  + str(self.normal.get_x()) + ", " + str(self.normal.get_y()) + ", " + str(self.normal.get_z()) + ")"
          
    def interceta_triangulo(self, reta):
        #reta
        pontoOrigem = reta.origem
        pontoDestino = reta.destino
        vetorDiretor = reta.vetor_diretor

        #pontoReta = pontoOrigem + t*vetorDiretor        
        
        #plano
        ponto1 = self.ponto1
        ponto2 = self.ponto2
        ponto3 = self.ponto3

        vetor12 = ponto1 - ponto2 ##ponto2 - ponto1 
        vetor13 = ponto1 - ponto3 ##ponto3 - ponto1

        #pontoPlano = plano.ponto1 + alfa*vetor12 + beta*vetor13

        #Se há interceção:
        #pontoPlano = pontoReta 
        #<=> plano.ponto1 + alfa*vetor12 + beta*vetor13 =
        # = pontoOrigem + t*vetorDiretor
        #<=> alfa*vetor12 + beta*vetor13 - t*vetorDiretor
        # = pontoOrigem - plano.ponto1
        
        #1ºpasso) calcular det(matriz dos coeficientes)

        m = Matriz(3,3)
        m.set_entrada(1, 1, vetor12.x)
        m.set_entrada(1, 2, vetor13.x)
        m.set_entrada(1, 3, vetorDiretor.x)
        m.set_entrada(2, 1, vetor12.y)
        m.set_entrada(2, 2, vetor13.y)
        m.set_entrada(2, 3, vetorDiretor.y)
        m.set_entrada(3, 1, vetor12.z)
        m.set_entrada(3, 2, vetor13.z)
        m.set_entrada(3, 3, vetorDiretor.z)

        if abs(m.det()) < TOLERANCIA_ZERO:
            ##print("1 if, det")
            return [False, None, None]

        #2ºpasso) calcular alfa com a regra de cramer

        #Matriz m * [alfa, beta, t]^T = pontoOrigem - plano.ponto1
        
        m1 = m.copia()
      
        m1.set_entrada(1, 1, (ponto1.x - pontoOrigem.x))
        m1.set_entrada(2, 1, (ponto1.y - pontoOrigem.y))
        m1.set_entrada(3, 1, (ponto1.z - pontoOrigem.z))      
        
        alfa = m1.det()/m.det()

        if (alfa<0.0 or alfa>1.0):
            ##print("2 if, alfa")
            return [False, None, None]

        #3ºpasso) calcular beta com regra de cramer

        m2 = m.copia()
        m2.set_entrada(1, 2, (ponto1.x - pontoOrigem.x))
        m2.set_entrada(2, 2, (ponto1.y - pontoOrigem.y))
        m2.set_entrada(3, 2, (ponto1.z - pontoOrigem.z))     
        
        beta = m2.det()/m.det()
        
        if (beta<0.0 or beta>1.0):
            ##print("3 if, beta")
            return [False, None, None]

        #4ºpasso) calcular o gama 

        gama = 1 - alfa - beta

        if (gama<0.0 or gama>1.0):
            ##print("4 if, gama")
            return [False, None, None]

        #5ºpasso) calcular t com a regra de cramer

        m3 = m.copia()
        m3.set_entrada(1, 3, (ponto1.x - pontoOrigem.x))
        m3.set_entrada(2, 3, (ponto1.y - pontoOrigem.y))
        m3.set_entrada(3, 3, (ponto1.z - pontoOrigem.z))    
        
        t = m3.det()/m.det()

        #print(t)
        
        if (t<TOLERANCIA_ZERO):
            ##print("5 if, t")
            return [False, None, None]

        #6ºpasso) substituir t na equação da reta
        #para obter o ponto de interceção

        ponto_intercecao = ponto1 + (ponto2-ponto1)*alfa + (ponto3-ponto1)*beta
        
        return [True, ponto_intercecao, t]
        
        
if __name__ == "__main__":
    print("teste ao construtor")
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(2.0, 0.0, 0.0)
    c = Ponto3D(0.0, 2.0, 0.0)
    plano1 = Plano(a, b, c)
    print("Até aqui não foram lançadas exceções.")
    
    print()
    print("teste a TOLERANCIA_ZERO")
    print("TOLERANCIA_ZERO = " + str(TOLERANCIA_ZERO))
    
    print()
    print("teste à exceção ErroPontosColineares")
    try:
        plano2 = Plano(a, b, b)
    except ErroPontosColineares:
        print("Ao tentar definir-se o plano plano2 = Plano(a, b, c)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("A execução foi interrompida. plano2 não ficou definida.")
    
    print()
    print("teste a __str__")
    # a normal tem que apontar no sentido do eixo dos z’s
    # e tem que ter comprimento 1
    print(plano1)
                
    print()
    print("testes a interceta_triangulo")
    p1 = Ponto3D(1.0, 1.0, 10.0)
    p2 = Ponto3D(1.0, 1.0, 5.0)
    r1 = Reta(p1, p2)
    trio = plano1.interceta_triangulo(r1)
    if trio[0] == True:
        print("r1 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
        print("interceção calculada com a equação da reta e t.")
        print("(tem que dar o mesmo que trio[1])")
        t = trio[2]
        pi = r1.origem + (r1.vetor_diretor * t)
        print(pi)
    else:
        print("r1 NÃO interceta plano1.")
        p3 = Ponto3D(2.0, 2.0, 10.0)
        r2 = Reta(p1, p3)
        trio = plano1.interceta_triangulo(r2)
        if trio[0] == True:
            print("r2 interceta plano1.")
            print("interceção = " + str(trio[1]))
            print("parâmetro t = " + str(trio[2]))
        else:
            print("r2 NÃO interceta plano1.")
            