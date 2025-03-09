# Um código para aumento de salário dos funcionários de uma empresa X.

# Salário              Reajuste
# 0 - 400.00           15% 
# 400.00 - 800.00      12%
# 800.00 - 1200.00     10%
# 1200.00 - 2000.00    7%
# Acima de 2000.00     4%

# Entrada
salario = float(input('Digite o salário do funcionário: '))

# Verificação do salário e o reajuste dele dependendo da porcentagem
if salario > 0 and salario <= 400.00:
    reajuste = 15
    ganho = (salario * reajuste) / 100
    salario_reajustado = ganho + salario
elif salario > 400.00 and salario <= 800.00:
    reajuste = 12
    ganho = (salario * reajuste) / 100
    salario_reajustado = ganho + salario
elif salario > 800.00 and salario <= 1200.00:
    reajuste = 10
    ganho = (salario * reajuste) / 100
    salario_reajustado = ganho + salario
elif salario > 1200.00 and salario <= 2000.00:
    reajuste = 7
    ganho = (salario * reajuste) / 100
    salario_reajustado = ganho + salario
elif salario > 2000.00:
    reajuste = 4
    ganho = (salario * reajuste) / 100
    salario_reajustado = ganho + salario

# Saída
print(f'Novo salario: {salario_reajustado:.2f}')
print(f'Reajuste ganho: {ganho:.2f}')
print(f'Em percentual: {reajuste} %')