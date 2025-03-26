import os
import time

lista_compras = []

while True:
    print('Selecione uma opção: [i]nserir [a]pagar [l]istar')
    opcao = input().lower()
    if opcao == 'i':
        print('Escreva um item para adicionar a sua lista:')
        item = input()
        lista_compras.append(item)
        print(f'O item {item} foi adicionado na sua lista.')
        print('Carregando...')
        time.sleep(3)
        os.system('cls')
    elif opcao == 'a':
        if not lista_compras:
            print('Sua lista ainda não tem itens para apagar.')
        else:
            while True:
                try:
                    print('Escolha um índice para apagar:')
                    apagar_item = int(input())
                    print(f'O item {lista_compras[apagar_item]} foi removido da sua lista.')
                    lista_compras.pop(apagar_item)
                    print('Carregando...')
                    time.sleep(3)
                    os.system('cls')
                    break
                except:
                    print('O índice que você escreveu não existe na lista. Tente novamente.')
    elif opcao == 'l':
        if not lista_compras:
            print('Não possuí itens para listar.')
        else:
            for indice, produto in enumerate(lista_compras):
                print('Os itens da sua lista: ')
                print(indice, produto)
            print('Carregando...')
            time.sleep(3)
            os.system('cls')
    else:
        print('Você não colocou uma opção válida. Tente novamente.')