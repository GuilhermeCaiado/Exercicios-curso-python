import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

lista_compras = []

while True:
    tipo = input('[I]nserir um produto \n[A]pagar um produto \n[L]istar lista de compras \n[P]arar a lista de compras \nSelecione o tipo: ').upper()

    if tipo not in ['I', 'A', 'L', 'P']:
        print('Selecione um tipo válido.')
        continue

    if tipo == 'P':
        break

    if tipo == 'I':
        while True:
            compras = input("Insira um produto ou [S] para sair: ").lower()
            
            if compras == 's':
                limpar()
                break
            else:
                lista_compras.append(compras)

    if tipo == 'A':
        if not lista_compras:
            print("A lista está vazia.")
            continue

        try:
            while True: 
                for indice in range(len(lista_compras)):
                    print(indice, lista_compras[indice])

                pegar_indice = int(input('Insira o número do produto que você quer apagar: '))
                lista_compras.pop(pegar_indice)

                sair = input('Deseja sair? (S)im ou (N)ão: ').lower()
                if sair == 's':
                    limpar()
                    break
        except (ValueError, IndexError):
            print('Insira um valor válido.')
            continue

    if tipo == 'L':
        if not lista_compras:
            print("A lista está vazia.")
        else:
            for indice in range(len(lista_compras)):
                print(indice, lista_compras[indice])

        sair = input('Deseja sair? (S)im ou (N)ão: ').lower()
        if sair == 's':
            limpar()
            continue
