duracao_segundo = int(input())

horas = duracao_segundo // 3600
minutos = (duracao_segundo % 3600) // 60
segundos = duracao_segundo % 60

print(f'{horas}:{minutos}:{segundos}')