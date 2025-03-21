# Lê o número de pares de valores a serem lidos
qtd_valores_lidos = int(input())

# Inicia um loop que irá rodar 'qtd_valores_lidos' vezes
for i in range(qtd_valores_lidos):
    # Lê dois números inteiros, separados por espaço
    x, y = map(int, input().split())

    # Tenta realizar a divisão x / y
    try:
        divisao = x / y
        # Se a divisão for possível, imprime o resultado
        print(divisao)

    # Caso ocorra um erro (por exemplo, divisão por zero), exibe a mensagem de erro    
    except:
        print('divisao impossivel')