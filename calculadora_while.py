""""
Calculadora com while
"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o perador ( +-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    ### Verificações de dados no imput
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True # Verifica e transforma os dados em float.
    except:
        numeros_validos = None # Caso a verificação falahar retorna None

    if numeros_validos is None:
        print('Um ou ambos os números divitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos: # Valida os operadores permitidos atraves de uma lista valida.
        print('Operador invalido.')
        continue

    if len(operador) > 1: # Regra para inserir apenas um operador
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta. Confira o resuultado abaixo: ')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Nunca chegar aqui') # Uma forma de verificar.

    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break
