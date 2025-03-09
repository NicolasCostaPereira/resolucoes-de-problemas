# A variável "distancia" recebe uma entrada do usuário que será a distância em quilômetros
distancia = int(input('Insira a distância que a viagem possui: '))

# Calculo do tempo que levaria para percorrer a distância à uma velocidade constante de 30 km/h.
tempo = 60 / 30 * distancia

# # Saída
print(f'{tempo:.0f} minutos')