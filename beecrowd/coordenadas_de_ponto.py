# lê dois valores de ponto flutuante
x, y = map(float, input('Me dê um X e Y de um plano cartesinao e irei dizer em qual quadrante ele está: ').split())

# Verifica em qual quadrante o ponto (x, y) está
if x > 0 and y > 0:
    print('Q1') # Primeiro quadrante
elif x < 0 and y > 0:
    print('Q2') # Segundo quadrante
elif x < 0 and y < 0:
    print('Q3') # Terceiro quadrante
elif x > 0 and y < 0:
    print('Q4') # Quarto quadrante

# Verifica se o ponto está sobre os eixos
elif x == 0 and y > 0 or y < 0:
    print('Eixo Y')
elif y == 0 and x > 0 or x <0:
    print('Eixo X')

# Se não cair em nenhuma das condições acima, então o ponto é 0
else:
    print('Origem')