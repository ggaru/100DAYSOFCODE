import random
from random import random, randint

#A função randint() pega um número aleatório entre o dado A e o dado B.
random_integer = randint(1,10)
print(random_integer)

#Prática - Cara ou coroa
x = randint(1,2)
if x == 1:
    print("Cara")
else:
    print("Coroa")

#Listas
#Uma lista, reconhecivel pelos [] em Python é nada menos que a junção de vários dados em uma única variavel, organizada por lista.
estados_br = ["Ceará", "São Paulo"]
#Retorna a lista inteira
print(estados_br)
#Retorna o primeiro item da lista. Também se pode usar números negativos.
print(estados_br[0])

#É possivel alterar valores da lista utilizando o operador =
estados_br [1] = "Bahia"
print(estados_br)

#A função Append() adiciona um item no final da lista.
estados_br.append("Pernambuco")
print(estados_br)

#A função Extend(), funciona como a Append(), adicionando vários itens ao mesmo tempo.
estados_br.extend(["São Paulo", "Distrito Federal", "Amazonas"])
print(estados_br)

#Prática 02  - escolhendo quem vai pagar a conta
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
randx_ = randint(0,len(friends)-1)
print(f"Quem pagará a conta: {friends[randx_]}")

#DESAFIO DIA 04 - ROCK, PAPER AND SCISSORS
game = ["Pedra", "Papel", "Tesoura"]
choose = int(input("Selecione, \n 1 - PEDRA \n 2 - PAPEL \n 3- TESOURA"))
ia_ = randint(0,2)
p1 = choose - 1
print(f"Você escolheu: {game[p1]}")
print(f"O computador escolheu: {game[ia_]}")

if (p1 == 0 and ia_ ==2) or (p1 == 1 and ia_ ==0) or (p1 == 2 and ia_ ==1):
    print("Você venceu")
elif p1 == ia_:
    print("Empate")
else:
    print("Você perdeu.")