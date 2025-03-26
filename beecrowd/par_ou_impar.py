# Lê um número inteiro que indica quantos números serão analisados
qtd_loops = int(input())

# Executa o loop 'qtd_loops' vezes
for i in range(qtd_loops):

    # Lê um número inteiro do usuário
    numero = int(input())

    # Se o número for zero, imprime "NULL" e pula o restante do código
    if numero == 0:
        print('NULL')

    else:
        # Verifica se o número é PAR ou ÍMPAR
        if numero % 2 == 0:
            par_impar = 'EVEN' # Par
        else:
            par_impar = 'ODD' # Ímpar

        # Verifica se o número é POSITIVO ou NEGATIVO
        if numero > 0:
            positivo_negativo = 'POSITIVE'
        elif numero < 0:
            positivo_negativo = 'NEGATIVE'

        # Exibe o resultado no formato: "EVEN POSITIVE" ou "ODD NEGATIVE", etc
        print(par_impar, positivo_negativo)