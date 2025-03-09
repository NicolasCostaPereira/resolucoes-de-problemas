# Código simples que irá calcular o total a pagar da quantidade de peças basesada no valor de cada uma.

# Entrada
peca1, num_peca1, valor_peca1 = input('Digite o código da primeira peça, a quantidade de peças e o valor unitário: ').split() # Ex: 12 1 5.30
peca2, num_peca2, valor_peca2 = input('Digite o código da segunda peça, a quantidade de peças e o valor unitário: ').split() # Ex: 16 2 5.10

# Cálculo do valor total a pagar da quantidade do código da primeira peça e da segunda.
total_pagar = (int(num_peca1) * float(valor_peca1)) + (int(num_peca2) * float(valor_peca2)) # Ex: 15.50

# Saída
print(f'VALOR A PAGAR: R$ {total_pagar:.2f}') 