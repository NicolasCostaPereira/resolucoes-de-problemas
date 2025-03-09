"""
Este programa lê 6 valores do usuário e conta quando deles é positivo.
Ao final, Exibe a quantidade valores positivos.
"""

# Começa os contadores
contador_controle = 0 # Contador para limitar o while
contador_positivo = 0 # Contador de positivos

# Loop para a entrada do usuário
while contador_controle < 6:
    contador_controle += 1 # Soma mais 1 para limitar o while
    valor = float(input('Digite um valor numérico: '))
    
    if valor > 0: # Verifica se o valor digitado do usuário é positivo
        contador_positivo += 1 # Se for positivo incrementa no contador de positivos

# Exibe a quantidade de valores positivos lidos
print(f'{contador_positivo} valores positivos')
