# Código simples para efetuar o cálculo da área de um círculo.

# Entrada
raio = float(input('Digite um valor correspondente ao raio de um círculo: ')) # Ex: 2

# Cálculo da área utilizando a fórmula: area = Pi . r ^ 2 (Pi = 3,14159)
area = 3.14159 * raio ** 2 

# Saída mostrando a área do círculo com 4 casas decimais de precisão
print(f'A área do círculo é {area:.4f}') # Ex: 12.5664