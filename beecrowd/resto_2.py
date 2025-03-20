divisor = int(input()) # Solicita ao usuário um número inteiro para ser usado como divisor

# Loop que percorre de 1 até 9999
for i in range(1, 10000):

    # Verifica se o resto da divisão de 'i' pelo 'dividendo' é igual a 2
    if i % divisor == 2:
        print(i) # Se a condição for verdadeira, imprime o valor de 'i'