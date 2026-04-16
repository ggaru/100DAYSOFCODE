####
#Setando uma variavel chamada Altura, perguntando ao usuário uma entrada e convertendo-a para int.
#height = int(input("Qual a sua altura?"))

#A função If checa se um valor é Verdadeiro, ou Falso.
#Checa se a altura dada pelo usuário é Maior que 128.
#if height > 128:
    #Caso retorne verdadeiro, todo código escrito aqui será executado
    #print("Você é bem alto!")
#else:
    #Caso retorne falso, todo código escrito aqui será executado
    #print("Que anão")
####
#Operadores de comparação.
x = 10
y = 9
z = "a"
h = True
#o Operador > compara se um dado é maior que o outro.
if x > 10:
    print("O x é Maior que 10!")
#O operador < compara se um dado é menor que o outro.
if y < 9:
    print("o Y é menor que 9!")
#o operador >= compara se um dado é maior ou igual que o outro.
if x >= 10:
    print("o X é igual ou maior que 10!")
#o operador <= compara se um dado é menor ou igual que o outro.
if y <= 9:
    print("o y é menor ou igual a 9!")
#o operador == compara se os dados são iguais.
if z == "a":
    print("o Z é igual a letra A")
#o operador != compara se os dados são diferentes.
if h != False:
    print("o h é diferente de Falso")

#Modulo
#O operador % retorna o que sobrou da divisão. O retorno será 1.
print(10 % 3)

#Checando se um valor é impar ou par
#n = int(input("Digite um número"))
#x = n % 2

if x != 0:
    print("É um numero impar!")
else:
    print("É um numero par")

#Pizza delivery
#print("Bem vindo ao Delivery de pizza!")
#size = input("Qual tamaho da sua pizza? P, M ou G?")
#pep = input("Deseja peperroni? S ou N")
#cheese = input("Deseja queijo extra? S ou N")
#bill = 0

#if size == "P":
    #bill += 15
#elif size == "M":
    #bill += 20
#elif size == "G":
    #bill += 25

#if pep == "S":
    #if size == "P":
        #bill +=2
    #else:
        #bill += 3
#if cheese == "S":
    #bill +=1

#print(bill)

#DESAFIO DIA 03 - TREASURE HUNT TEXT GAME
print("Bem vindo ao caçador de tesouros!")
choose = input("Direita ou esquerda?: ").lower()

if choose == "esquerda":
    choose = input("Nadar ou esperar?").lower()
    if choose == "esperar":
        choose = input("Porta vermelha, azul ou amarela?").lower()
        if choose == "vermelha":
            print("Voce foi queimado.")
        elif choose == "Azul":
            print("Você foi comido")
        elif choose == "amarela":
            print("Você ganhou. uau.")
        else:
            print("Fim de jogo.")

    else:
        print("Fim de jogo.")
else:
    print("Fim de jogo.")