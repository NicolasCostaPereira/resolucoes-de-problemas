# Solicita ao usuário a quantidade de números a serem verificados
quantidade_numeros = int(input())

# Loop que percorre de 0 até a quantidade informada (incluindo ela)
for i in range(quantidade_numeros + 1):

    # Verifica se o número é ímpar (se o resto da divisão por 2 for diferente de 0)
    if i % 2 != 0:
        print(i) # Se for ímpar, imprime o número