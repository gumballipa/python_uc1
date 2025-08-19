##
# Aula 0808 - Atividade 01
# Nome: [Henrique]
# Data: [19/08]

### >>> QUESTÃO 1 <<< ###

#Exemplo De Vetor
vetor=[10, 20, 30, 40, 50]
# print(f"Dados do Vetor: {vetor}")

# print(f" Dados da 4a posição : {vetor[3]}")

### >>> QUESTÃO 2 <<< ###

for i in range (5):
    # print(f"Valor do vetor na posição {i+1} é: {vetor[i]}")

### >>> QUESTÃO 3 <<< ###

    indice = 1
for elemento in vetor:
    # print (f"o vlaor do indice {indice} é: {elemento}")
    indice+= 1

### >>> QUESTÃO 4 <<< ###

import random
num = random.randint(1, 100)
# print(f"numero aleatorio gerado: {num}")

### >>> QUESTÃO 4.part2 <<< ###

numeros = []
for i in range (20) :
    numeros.append(random.randint(1, 100))

# print(f"numero aleatorio gerado: {numeros}")

soma=sum(numeros)
maior=max(numeros)
menor=min(numeros)
qt_elementos=len(numeros)
media=soma/qt_elementos

# print(f"\n\n\tSoma: {soma}, Maior: {maior}, Menor: {menor}, Quantidade de Elementos: {qt_elementos}, Média: {media}\n\n")

### >>> QUESTÃO 5 <<< ###
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

print(f"Números pares: {len(pares):4}")
print(f"Números ímpares: {len(impares):4}")