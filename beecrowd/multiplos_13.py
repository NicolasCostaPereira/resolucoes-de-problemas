# Lê dois números inteiros
x = int(input())
y = int(input())

# Inicializa a variável soma com valor 0, 
# que será usada para armazenar o resultado final
soma = 0

# Verifica se x é maior que y, e caso seja, troca os valores de x e y
# Isso garante que x sempre será o menor número
if x > y:
    x, y = y, x

# Cria um laço de repetição
for i in range(x, y + 1):
    # Se o número i não for múltiplo de 13 (i % 13 != 0), 
    # soma esse número à variável soma
    if i % 13 != 0:
        soma += i


# Imprime o valor final da soma
print(soma)