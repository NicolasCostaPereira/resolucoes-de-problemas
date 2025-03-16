# Inicializa as variáveis para contar a quantidade de pares, ímpares, positivos e negativos
pares = 0
impares = 0
positivos = 0
negativos = 0

# Loop que se repete 5x
for i in range(5):
    numero = int(input('Digite um número: ')) 

    # Verifica se o número é positivo
    if numero > 0:
        positivos += 1

    # Verifica se o número é negativo
    elif numero < 0:
        negativos += 1

    # Verifica se o número é par
    if numero % 2 == 0:
        pares += 1

    # Verifica se o número é negativo
    else:
        impares += 1
    
# Saída
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')