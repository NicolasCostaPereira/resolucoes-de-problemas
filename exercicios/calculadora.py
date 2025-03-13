import time

print('Olá essa é uma calculadora simples!')

time.sleep(2)

while True:
    entrar_sair = input('Você deseja entrar na calculadora ou sair? entrar/sair ').lower()

    if entrar_sair == 'sair':
        break

    elif entrar_sair == 'entrar':
        print('Você entrou na calculadora!')
        time.sleep(1)
        
        while True:
            primeiro_numero = input('Digite o primeiro número: ')
            time.sleep(1)
            segundo_numero = input('Digite o segundo número: ')

            if primeiro_numero.isdigit() and segundo_numero.isdigit():
                primeiro_numero = float(primeiro_numero)
                segundo_numero = float(segundo_numero)
                break
            else:
                print('Você não digitou números, recomece a calculadora.')
                time.sleep(2)

        print(' ')
        print('Essa é a lista dos operadores que a calculadora suporta:')
        print('soma -> +')
        print('subtração -> -')
        print('divisão -> /')
        print('multiplicação -> *')
        time.sleep(2)

        while True:
            operador = input('Digite um dos operadores para efetuar o cálculo: +-/* ')

            if operador not in '+-/*' or len(operador) > 1:
                print('Operador inválido. Tente novamente.')

            else:
                if operador == '+':
                    soma = primeiro_numero + segundo_numero
                    print('Você escolheu a soma!')
                    time.sleep(2)
                    print(f'{primeiro_numero} + {segundo_numero} = {soma}')
                    time.sleep(2)

                elif operador == '-':
                    subtracao = primeiro_numero - segundo_numero
                    print('Você escolheu a subtração!')
                    time.sleep(2)
                    print(f'{primeiro_numero} - {segundo_numero} = {subtracao}')
                    time.sleep(2)

                elif operador == '/':
                    if segundo_numero == 0:
                        print('Erro: divisão por zero não é permitido!')

                    else:
                        divisao = primeiro_numero / segundo_numero
                        print('Você escolheu a divisão!')
                        time.sleep(2)
                        print(f'{primeiro_numero} / {segundo_numero} = {divisao}')
                    time.sleep(2)

                elif operador == '*':
                    multiplicacao = primeiro_numero * segundo_numero
                    print('Você escolheu a multiplicação!')
                    time.sleep(2)
                    print(f'{primeiro_numero} * {segundo_numero} = {multiplicacao}')
                    time.sleep(2)
                
    else:
        print('Não entendemos o que você quis dizer, recomece a calculadora.')
        time.sleep(2)