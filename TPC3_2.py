from matriz_41839 import Matriz

# teste adicional a determinantes de matrizes de 4x4
matriz_A = Matriz(4, 4)
matriz_A.set_linha(1, [1.0, 0.0, 0.0, -11.0])
matriz_A.set_linha(2, [0.0, 1.0, 0.0, -3.0])
matriz_A.set_linha(3, [0.0, 0.0, 1.0, -7.0])
matriz_A.set_linha(4, [9.0, 2.0, 6.0, 0.0])
det_A = matriz_A.det()
print("det(A) = " + str(det_A))

lista_B = [9.0, 3.0, 8.0, -7.0]
matriz_A1 = matriz_A.copia()
matriz_A2 = matriz_A.copia()
matriz_A3 = matriz_A.copia()
matriz_A4 = matriz_A.copia()
matriz_A1.set_coluna(1, lista_B)
matriz_A2.set_coluna(2, lista_B)
matriz_A3.set_coluna(3, lista_B)
matriz_A4.set_coluna(4, lista_B)
print("x = " + str(round((matriz_A1.det()/det_A), 3)))
print("y = " + str(round((matriz_A2.det()/det_A),3)))
print("z = " + str(round((matriz_A3.det()/det_A),3)))
print("t = " + str(round((matriz_A4.det()/det_A),3)))