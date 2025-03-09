# Código simples que irá calcular a área de um triângulo, círculo, trapézio, quadrado e retangulo

# Entrada
a, b, c = map(float, input('Digita 3 valores para calcularmos a área das figuras geométricas: ').split()) # Ex: 3 4 5 

# Calculo das áreas
triangulo = (a * c) / 2 
circulo = 3.14159 * c ** 2
trapezio = (a + b) * c / 2
quadrado = b ** 2
retangulo = a * b

# Saída
print(f'A área do triângulo: {triangulo:.3f}') # Ex: 7.500
print(f'A área do círculo: {circulo:.3f}') # Ex: 78.540
print(f'A área do trapézio: {trapezio:.3f}') # Ex: 17.500
print(f'A área do quadrado: {quadrado:.3f}') # Ex: 16.000
print(f'A área do ratângulo: {retangulo:.3f}') # Ex: 12.000