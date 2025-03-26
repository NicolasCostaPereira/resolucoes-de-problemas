# Lê um número inteiro do usuário
numero = int(input())

# Percorre todos os números de 1 até o número digitado
for i in range(1, numero + 1):

    # Verifica se o número é PAR (divisível por 2)
    if i % 2 == 0:

        # Calcula o quadrado do número
        quadrado = i ** 2

        # Imprime o resultado no formato desejado
        print(f'{i}^2 = {quadrado}')