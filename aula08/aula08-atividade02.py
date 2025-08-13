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