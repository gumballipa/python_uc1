##
# Aula 08 - Atividade 01
# Nome: [Henrique]
# Data: [12/08]

"""
Função saudação
    - imprime uma mensagem de saudação
"""
def saudacao () :
    print(f"\n\n\t Ola, seja bem vindo a aula de python, abaixo vc recebeu acesso a nossa calculadora! \n\n")

## chamando a funcao
saudacao ()

## >> Segunda atividade << ##
#  *Soma de numeros*

def somar_numeros (numero1, numero2):
    """
    Função que recebe dois números e retorna a soma deles.
    """

    soma = numero1 + numero2
    return soma

numero1 =float(input("Digite o primeiro numero: "))
numero2 =float(input("Digite o segundo numero: "))

resultado=somar_numeros (numero1, numero2)

print(f"\n\n\tO resultado da soma de {numero1} + {numero2} = {resultado}\n\n")