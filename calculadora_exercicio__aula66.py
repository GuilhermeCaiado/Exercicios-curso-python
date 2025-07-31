while True:

    # Campo para digitar os números que serão calculados (Se não for inserido um número retorna erro)
    try:
        numero_1 = float(input('Digite o seu primeiro número: '))
        numero_2 = float(input('Digite seu segundo número: '))
    except:
        print('Insira um valor válido')

    # Loop para receber o operador de conta (Se for inserido algum operador fora dos inseridos da erro)
    while True:
        operador = int(input('Selecione seu operador \n 1.SOMA \n 2.SUBTRAÇÃO \n 3.MULTIPLICAÇÃO \n 4.DIVISÃO \n Selecione o número do operador: '))

        if operador not in [1,2,3,4]:
            print("Insira um operador válido")
        else:
            break

    #Area das contas e impressão das mesmas
    if operador == 1:
        soma = numero_1 + numero_2
        print(f'Sua soma é igual a {soma}')
    elif operador == 2:
        sub = numero_1 - numero_2
        print(f'Sua subtração é igual a {sub}')
    elif operador == 3:
        mult = numero_1 * numero_2
        print(f'Sua multipluicação é igual a {mult}')
    else:
        div = numero_1 / numero_2
        print(f'Sua divisão é igual a {div}')
    
    
    # Area de saida do código.
    sair = input('Quer sair? [S]im, [N]ão: ').lower().startswith("s")
    
    if sair is True:
        break