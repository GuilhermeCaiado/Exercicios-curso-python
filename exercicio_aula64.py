nome = str(input("Digite seu nome: "))

tamanho_nome = len(nome)
contador_letras = 0
while contador_letras < tamanho_nome:
    print(nome[contador_letras], end= '*')

    contador_letras += 1