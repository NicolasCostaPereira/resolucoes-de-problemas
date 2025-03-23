# Inicializa a contagem de notas válidas
qtd_notas_validas = 0

# Inicializa a soma das notas válidas
notas_validas = 0

# Inicia um loop infinito para receber notas do usuário
while True:
    # Lê uma nota do usuário e converte para float
    nota = float(input())

    # Verifica se a nota está dentro do intervalo válido (0 a 10)
    if nota > 0 and nota <= 10:
        # Incrementa a contagem de notas válidas
        qtd_notas_validas += 1

        # Soma a nota válida à variável acumuladora
        notas_validas += nota
    else:
        # Se a nota não for válida, exibe a mensagem de erro
        print('nota invalida')

    # Se já tivermos duas notas válidas, calculamos a média e encerramos o loop
    if qtd_notas_validas >= 2:
        print(f'media = {notas_validas/2:.2f}')
        break