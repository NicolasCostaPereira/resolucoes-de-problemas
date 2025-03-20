# Solicita ao usuário o número de testes que serão realizados
numero_de_testes = int(input())

# Loop que será executado 'numero_de_testes' vezes
for i in range(numero_de_testes):
    # Recebe três números separados por espaço e os converte para float
    primeiro, segundo, terceiro = map(float, input().split())

    # Calcula a média ponderada com pesos: 2 para o primeiro, 3 para o segundo e 5 para o terceiro
    media_ponderada = ((primeiro * 2) + (segundo * 3) + (terceiro * 5)) / 10

    # Exibe a média ponderada formatada com uma casa decimal
    print(f'{media_ponderada:.1f}')