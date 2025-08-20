produtos = (
    ("arroz", 5.99),
    ("feijão", 6.99),
    ("macarrão", 7.99),
    ("açúcar", 4.99),
    ("sal", 2.99),
)

# print("Produtos Disponiveis")

import random

numeros = []
for i in range(100):
    numeros.append(random.randint(1, 100))

soma = 0
for numero in numeros:
    soma += numero
media = soma / len(numeros)

"""print("Números gerados:")
for numero in numeros:
    print(numero,)"""

maiores = []
print(f"Média: {media:.2f}")
print("Números maiores que a média:")
for numero in numeros:
    if numero > media:
        # print(numero,)
        maiores.append(numero)

print(f"Numeros maiores que a media: {maiores}")