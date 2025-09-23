import os

def limpar_tela():
  if os.name == 'nt':
     _ = os.system('cls')
  else:
     _ = os.system('clear')


produtos = []
quantidade = []
precos = []

#MENU
while True: 

    print ("-----------Menu----------")
    print (" 1 - Adicionar produto \n 2 - Listar produto \n 3 - Vender produto \n 4 - Relatório de estoque \n 5 - Sair")
    menus = int(input("Informe o que você quer fazer: "))
    print ("\n")

    #ADICIONAR PRODUTOS
    if menus == 1:
        pergunta_produto = str(input("Informe o nome do produto: ").lower())
        produtos.append(pergunta_produto)

        pergunta_quantidade = int(input("Informe a quantidade desse produto: "))
        quantidade.append(pergunta_quantidade)

        pergunta_preco = float(input("Informe o preço desse produto. (Ex: R$: 4.50): R$ "))
        precos.append(pergunta_preco)
        limpar_tela()
    
    #LISTAR PRODUTOS
    elif menus == 2:
        limpar_tela()
        contador_indice = 0
        while contador_indice < len(produtos):
            print(f"Produto: {produtos[contador_indice]}")
            print(f"Quantidade: {quantidade[contador_indice]}")
            print(f"Preço: R${precos[contador_indice]:.2f} \n")
            contador_indice += 1
    
    #VENDER PRODUTOS
    elif menus == 3:
        limpar_tela()
        print("----------VENDA----------")
        pergunta_venda_nome = str(input("Informe o nome do produto: ").lower())
        
        try:
            indice_do_produto = produtos.index(pergunta_venda_nome.lower()) 
        except ValueError:
            print(f"O produto '{pergunta_venda_nome}' não foi encontrado na lista.")

        pergunta_venda_quantidade = int(input("Informe a quantidade que vai ser vendida: "))
        
        if quantidade[indice_do_produto] >= pergunta_venda_quantidade:
            estoque = quantidade[indice_do_produto] - pergunta_venda_quantidade
            quantidade[indice_do_produto] = estoque
        else:
            print(f"Quantidade acima do estoque atual!!! \nEstoque atual: {quantidade[indice_do_produto]}")

        preco_venda = pergunta_venda_quantidade * precos[indice_do_produto]
        print(f"VALOR DA VENDA: {preco_venda} \nVENDA REALIZADA!!!!")
    
    #RELATORIO DE ESTOQUE
    elif menus == 4:
        limpar_tela()
        quantidade_total = len(produtos)
        print (f"Você tem {quantidade_total} produtos cadastrados.")

        soma_relatorio = sum(quantidade) * sum(precos)
        print(f"O valor do seu estoque é: {soma_relatorio}")

    #SAIR
    elif menus == 5:
        limpar_tela()
        print("OPERAÇÂO FECHADA!!!!")
        break
    
    else:
        limpar_tela()
        print("Informe um valor válido: ")
    
    