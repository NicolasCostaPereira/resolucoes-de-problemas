# Recebe o nome do usuário
nome = input('Digite seu nome: ')

# Verifica se "nome" foi preenchido.
if nome:
    # Exibe o nome do usuário.
    print(f'O seu nome é {nome}')

    # Exibe o nome invertido
    print(f'O seu nome invertido é {nome[::-1]}')

    # Verifica se há espaços no nome
    if ' ' in nome:
        print('O seu nome contém espaços') # Se houver espaços
    else:
        print('O seu nome não tem espaços') # Se não houver espaços

    # Exibe a quantidade de letras do nome
    print(f'O seu nome tem {len(nome)} letras')

    # Exibe a primeira letra do nome
    print(f'A primeira letra do seu nome é {nome[0]}')
    
    # Exibe a última letra do nome
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    # Caso o campo "nome" esteja vazio
    print('Desculpe, você deixou campos vazios.')