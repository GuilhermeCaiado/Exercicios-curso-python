"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar") 
except:
    print("Digite um número inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = int(input("Digite o horário (só com as horas): "))

if 0 <= horario <= 11:
    print("Bom dia")
elif 12 <= horario <= 17:
    print("Boa tarde")
elif 18 <= horario <= 23:
    print("Boa noite")
else:
    print("Horário Inválido")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    nome = str(input("Digite seu nome: "))

    if len(nome) <= 4:
        print("Seu nome é curto")
    elif 5 <= len(nome) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é longo")
except:
    print("Digite um nome")