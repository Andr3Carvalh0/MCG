from vetor_41839 import Vetor3D

v1 = Vetor3D(0.0, 1.0, 2.0)   #AB
v2 = Vetor3D(0.0, 3.0, 4.0)  #AC

# teste a externo
e = v1.externo(v2)
print("e = v1 externo v2 = ")
print(e)
print("")


#cosseno de AB e AC é --> AB.interno(AC) / AB.comprimento() * AC.comprimento()

# teste a cosseno
cos = v1.interno(v2) / v1.comprimento() * v2.comprimento()
print("cos = cosseno v1 e v2 = ")
print(round(cos, 3))
print("")
# n = (-2, 0, 0) <=> plano = -2x + 0y + 0z + d = 0    A = (2, -3, 0)
#<=> -4 + d = 0 <=> d = 4 <=> plano = -2x + 0y 0z = - 4

#D = (2, 1, 6)

resultado = (-2*2) + (0*1) + (0*6)
if resultado == -4:
    print (True)
else:
    print (False)
