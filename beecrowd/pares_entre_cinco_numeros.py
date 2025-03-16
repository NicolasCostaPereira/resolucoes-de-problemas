numeros_pares = 0 # Inicializa a variável que irá contar os números pares.

# Loop que se repete 5x
for i in range(5):
    numero = int(input('Escreva um número: '))

    # Verifica se o número é par
    if numero % 2 == 0:
        numeros_pares += 1 # Incrementa +1 se o valor for par

# Saída
print(f'{numeros_pares} valores pares')