# Loop infinito que continuará rodando até que o usuário insira dois números iguais
while True:
    # Lê dois números inteiros separados por espaço e os converte para int
    x, y = map(int, input().split())

    # Se x for maior que y, significa que os números estão em ordem decrescente
    if x > y:
        print('Decrescente')

    # Se x for menor que y, significa que os números estão em ordem crescente    
    elif x < y:
        print('Crescente')

    # Se x for igual a y, o loop é interrompido    
    else:
        break