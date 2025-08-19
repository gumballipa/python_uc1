##
# Aula 08 - Atividade 02
# Nome: [Henrique]
# Data: [12/08]

### >>> QUESTÃO 1 <<< ###

def saudacao():
    """
    Função saudação
        - imprime uma mensagem de saudação
    """
    print(f"\n\n\tOlá, seja bem-vindo Henrique\n\n")
# chamando a função

# saudacao()

### >>> QUESTÃO 2 <<< ###

def banana():
   for i in range(1, 11):
       print(i)

### >>> QUESTÃO 3 <<< ###
def maca():
   print("Olá, Henrique Santos!")

  ### >>> QUESTÃO 4 <<< ###

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
    def main():
        numero = int(input("Digite um número para calcular o fatorial: "))
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")

       ##
# Aula 0808 - Atividade 01
# Nome: [Henrique]
# Data: [19/08]

### >>> QUESTÃO 1 <<< ###

vetor =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Vetor, {vetor}")

print(f" Dados da 4a posição: {vetor[3]}")