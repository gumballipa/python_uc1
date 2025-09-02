##
# Aula 0808 - Atividade 01
# Nome: [Henrique]
# Data: [21/08]

### >>>  ATIVIDADE 01 - aula10 <<< ###

#Criando uma matriz 3x3 
""" 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elemento (0,0):", matriz[0][0])  # Saída: 1
print("Elemento (2,1):", matriz[2][1])  # Saída: 8


for linha in matriz:
    for elemento in linha:
       print(elemento, end=' ')
   #print()
"""

"""""
import random
matriz_2 = []
for i in range(3):
    linha2=[]

    for j in range (3):
        #linha.append(i)
        #linha.append(j)
        #linha.append(rrandom.randint(0.100))
        valor=random.randint(0,100)
        linha2.append(valor)

    matriz_2.append(linha2)

print (f"{matriz_2}")
"""
