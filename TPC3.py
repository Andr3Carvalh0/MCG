from matriz_41839 import Matriz

# teste adicional a determinantes de matrizes de 9x9
matriz_A = Matriz(9, 9)

matriz_A.set_linha(1, [3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 0.0, 0.0])
matriz_A.set_linha(2, [0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 0.0])
matriz_A.set_linha(3, [0.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0])

matriz_A.set_linha(4, [6.0, 0.0, 0.0, 16.0, 0.0, 0.0, 17.0, 0.0, 0.0])
matriz_A.set_linha(5, [0.0, 6.0, 0.0, 0.0, 16.0, 0.0, 0.0, 17.0, 0.0])
matriz_A.set_linha(6, [0.0, 0.0, 6.0, 0.0, 0.0, 16.0, 0.0, 0.0, 17.0])

matriz_A.set_linha(7, [3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 7.0, 0.0, 0.0])
matriz_A.set_linha(8, [0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 7.0, 0.0])
matriz_A.set_linha(9, [0.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 7.0])

det_A = matriz_A.det()
print("det(A) = " + str(det_A))

lista_B = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
matriz_A1 = matriz_A.copia()
matriz_A2 = matriz_A.copia()
matriz_A3 = matriz_A.copia()
matriz_A4 = matriz_A.copia()
matriz_A5 = matriz_A.copia()
matriz_A6 = matriz_A.copia()
matriz_A7 = matriz_A.copia()
matriz_A8 = matriz_A.copia()
matriz_A9 = matriz_A.copia()

matriz_A1.set_coluna(1, lista_B)
matriz_A2.set_coluna(2, lista_B)
matriz_A3.set_coluna(3, lista_B)
matriz_A4.set_coluna(4, lista_B)
matriz_A5.set_coluna(5, lista_B)
matriz_A6.set_coluna(6, lista_B)
matriz_A7.set_coluna(7, lista_B)
matriz_A8.set_coluna(8, lista_B)
matriz_A9.set_coluna(9, lista_B)

a = matriz_A1.det()/det_A 
print("a = " + str(round(a, 3)))
b = matriz_A2.det()/det_A
print("b = " + str(round(b, 3)))
c = matriz_A3.det()/det_A
print("c = " + str(round(c, 3)))
d = matriz_A4.det()/det_A
print("d = " + str(round(d, 3)))
e = matriz_A5.det()/det_A
print("e = " + str(round(e, 3)))
f = matriz_A6.det()/det_A
print("f = " + str(round(f, 3)))
g = matriz_A7.det()/det_A
print("g = " + str(round(g, 3)))
h = matriz_A8.det()/det_A
print("h = " + str(round(h, 3)))
i = matriz_A9.det()/det_A
print("i = " + str(round(i, 3)))

# verificação
matriz_M = Matriz(3, 3)
matriz_M.set_linha(1, [3.0, 4.0, 5.0])
matriz_M.set_linha(2, [6.0, 16.0, 17.0])
matriz_M.set_linha(3, [3.0, 4.0, 7.0])

matriz_M_inversa = Matriz(3, 3)
matriz_M_inversa.set_linha(1, [a, b, c])
matriz_M_inversa.set_linha(2, [d, e, f])
matriz_M_inversa.set_linha(3, [g, h, i])
matriz_I = matriz_M * matriz_M_inversa
print(matriz_I)
print("Entradas de matriz_I com 3 casas decimais")
print(str(round(matriz_I.get_entrada(1,1), 3)) + " "
+ str(round(matriz_I.get_entrada(1,2), 3)) + " "
+ str(round(matriz_I.get_entrada(1,3), 3)))
print(str(round(matriz_I.get_entrada(2,1), 3)) + " "
+ str(round(matriz_I.get_entrada(2,2), 3)) + " "
+ str(round(matriz_I.get_entrada(2,3), 3)))
print(str(round(matriz_I.get_entrada(3,1), 3)) + " "
+ str(round(matriz_I.get_entrada(3,2), 3)) + " "
+ str(round(matriz_I.get_entrada(3,3), 3)))