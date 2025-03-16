quantidade_de_leituras = int(input()) # Solicita ao usuário a quantidade de valores que serão lidos

# Inicializa contadores para valores dentro e fora do intervalo
valores_entre = 0
valores_fora = 0

# Loop que se repete 'quantidade_de_leituras' vezes para receber os valores
for i in range(quantidade_de_leituras):

    valor = int(input()) # Solicita um número do usuário e o converte para inteiro

    # Verifica se o valor está dentro do intervalo [10, 20]
    if valor >= 10 and valor <= 20:
        valores_entre += 1  # Se estiver no intervalo, incrementa 'valores_entre
    else:
        valores_fora += 1 # Se estiver fora do intervalo, incrementa 'valores_fora'

# Exibe a quantidade de valores dentro e fora do intervalo
print(f'{valores_entre} in')
print(f'{valores_fora} out')