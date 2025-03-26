# Solicita ao usuário que digite um número representando um mês
numero_do_mes = input()

# Utiliza a estrutura match-case (disponível a partir do Python 3.10) 
# para verificar qual número foi digitado e imprimir o mês correspondente.
match numero_do_mes:
    case '1':
        print('January')
    case '2':
        print('February')
    case '3':
        print('March')
    case '4':
        print('April')
    case '5':
        print('May')
    case '6':
        print('June')
    case '7':
        print('July')
    case '8':
        print('August')
    case '9':
        print('September')
    case '10':
        print('October')
    case '11':
        print('November')
    case '12':
        print('December')