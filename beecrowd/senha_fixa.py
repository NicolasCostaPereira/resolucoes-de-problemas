# Inicia um loop infinito que continuará rodando até que a senha correta seja digitada
while True:
    # Solicita ao usuário que digite a senha
    senha = input()

    # Verifica se a senha digitada é diferente de '2002'
    if senha != '2002':
        print('Senha Invalida') # Exibe mensagem informando que a senha está errada
    
    else:
        print('Acesso Permitido') # Se a senha for '2002', exibe a mensagem de acesso permitido
        break # Sai do loop, encerrando o programa