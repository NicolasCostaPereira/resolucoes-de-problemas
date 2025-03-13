frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'.lower()

i = 0
qt_letra_apareceu_vezes = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    contagem_letra_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qt_letra_apareceu_vezes < contagem_letra_atual:
        qt_letra_apareceu_vezes = contagem_letra_atual
        letra_apareceu_mais = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais}" e a quantidade de vezes foi {qt_letra_apareceu_vezes}x')