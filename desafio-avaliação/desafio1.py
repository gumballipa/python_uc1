##
# Aula Pyhon - Desafio 1
# Nome: [Henrique]
# Data: [25/08]

### DESAFIO 1 ###

""""
import random
matriz_2 = []
for i in range(10): # for de fora = linha
    linha2=[]

    for j in range (10): # for de dentro = coluna
        valor=random.randint(1,999)
        linha2.append(valor)

    matriz_2.append(linha2)
    for linha in matriz_2 :
      for valor in linha:
        print(f"{valor:02}", end=' ')
    print(f"")
    """

"""
import random
matriz_2 = []
for i in range(10): # for de fora = linha
    linha2=[]

    for j in range (10): # for de dentro = coluna
        valor=random.randint(1,999)
        linha2.append(valor)

    matriz_2.append(linha2)
  
#print(f"{matriz_2}")

for linha in matriz_2:
    print(linha)

print()

matriz_3 = []
for i in range(10): # for de fora = linha
    linha3=[]

    for j in range (10): # for de dentro = coluna
        valor=random.randint(1,999)
        linha3.append(valor)

    matriz_3.append(linha3)
    
#print(f"{matriz_3}")

for linha in matriz_3:
    print(linha3)

matriz_soma = []
for i in range(10):  #linha
    linha_soma = []
    for j in range(10): #coluna
        soma = matriz_2[i][j] + matriz_3[i][j]
        linha_soma.append(soma)
    matriz_soma.append(linha_soma)

print("Matriz Soma:")
for linha in matriz_soma:
    print(linha)
"""


import random
matriz1 = [[random.randint(1, 999) for j in range(10)] for i in range(10)]
matriz2 = [[random.randint(1, 999) for j in range(10)] for i in range(10)]

m3 = []
for i in range(0,10):
    linha3=[]
    for j in range(0,10):
        soma=matriz1[i][j] + matriz2[i][j]
        linha3.append(soma)
    m3.append(linha3)

    #print(f"{m3}")

    for i in range (0,10):
        print(f"m3 linha: .: {i:2}:. {m3[i][1:10]}")

        