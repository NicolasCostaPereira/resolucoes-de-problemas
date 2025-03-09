# Código que irá mostrar o consumo de km/L que foi em uma viagem.

# Entrada
distancia = int(input('Distância percorrida: ')) # Ex: 24
combustivel = float(input('Combustível gasto: ')) # Ex: 35.0

# Cálculo do consumo em km/L
consumo = distancia / combustivel # resultado = 0.686 

# Saída
print(f'{consumo:.3f} km/L')