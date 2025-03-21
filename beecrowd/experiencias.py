# Recebe a quantidade de testes que serão realizados
testes = int(input())

# Inicializa as variáveis para contar o total de cada tipo de cobaia
total_coelhos = 0
total_cobaias = 0
total_ratos = 0
total_sapos = 0

# Loop que será executado 'testes' vezes
for i in range(testes):
    # Lê a quantidade de cobaias e o tipo de animal (separados por espaço)
    qtd_testes, animal = input().split()
    qtd_testes = int(qtd_testes) # Converte a quantidade para inteiro

    # Soma a quantidade total de cobaias
    total_cobaias = qtd_testes + total_cobaias

    # Verifica qual é o tipo de cobaia e soma ao respectivo contador
    if animal == 'C': # 'C' representa coelhos
        total_coelhos += qtd_testes
    elif animal == 'R': # 'R' representa ratos
        total_ratos += qtd_testes
    elif animal == 'S': # 'S' representa sapos
        total_sapos += qtd_testes

# Calcula os percentuais de cada tipo de cobaia em relação ao total
percentual_coelhos = total_coelhos / total_cobaias * 100
percentual_ratos = total_ratos / total_cobaias * 100
percentual_sapos = total_sapos       / total_cobaias * 100

# Exibe os resultados formatados
print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')