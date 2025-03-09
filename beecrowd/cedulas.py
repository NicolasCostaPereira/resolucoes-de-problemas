# Código que irá mostrar quantas notas de determinado valor terá em um número inteiro.

# Entrada
valor = int(input()) # Ex: 576

# Calculando quantas notas tem em cada valor
notas_100 = valor // 100 # Ex: 5
notas_50 = (valor % 100) // 50 # Ex: 1
notas_20 = (valor % 100 % 50) // 20 # Ex: 1
notas_10 = (valor % 100 % 50 % 20) // 10 # Ex: 0
notas_5 = (valor % 100 % 50 % 20 % 10) // 5  # Ex: 1
notas_2 = (valor % 100 % 50 % 20 % 10 % 5) // 2 # Ex: 0
notas_1 = (valor % 100 % 50 % 20 % 10 % 5 % 2) // 1 # Ex: 1

# Saída mostrando quantas notas tem
print(valor)
print(notas_100, 'nota(s) de R$ 100,00')
print(notas_50, 'nota(s) de R$ 50,00')
print(notas_20, 'nota(s) de R$ 20,00')
print(notas_10, 'nota(s) de R$ 10,00')
print(notas_5, 'nota(s) de R$ 5,00')
print(notas_2, 'nota(s) de R$ 2,00')
print(notas_1, 'nota(s) de R$ 1,00')