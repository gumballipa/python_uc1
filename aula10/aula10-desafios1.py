### Desafio 1 ###
""""
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
    print()
"""


### Desafio 2 ###
import random
matriz_2 = []
for i in range(3): # for de fora = linha
    linha2=[]

    for j in range (3): # for de dentro = coluna
        valor=random.randint(0,100)
        linha2.append(valor)

    matriz_2.append(linha2)
print(f"{matriz_2}")

import random
matriz_3 = []
for i in range(3): # for de fora = linha
    linha3=[]

    for j in range (3): # for de dentro = coluna
        valor=random.randint(0,100)
        linha3.append(valor)

    matriz_3.append(linha3)
print(f"{matriz_3}")

soma=sum(matriz_2)
soma=sum1(matriz_3)

resultado = sum+sum1