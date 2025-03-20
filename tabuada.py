numero = int(input('Escreva um número: ')) # Solicita ao usuário um número inteiro para gerar a tabuada

print(f'A tabuada de {numero}: ')

# Loop que percorre de 1 a 10 (para calcular a tabuada)
for i in range(1, 11):

    produto = numero * i # Calcula o produto do número digitado pelo valor atual de 'i'
    
    print(f'{i} x {numero} = {produto}') # Exibe a multiplicação formatada no estilo de tabuada