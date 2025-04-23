#importando dados
from datas import day14data
from random import *
data = day1 4data.data

#variaveis 
n = 'name'
d = 'description'
c = 'country'
f = 'follower_count'
global play 
global first
global second
global points
points = 0
play = True

#selecionando os dados para comparação
print("Welcome to higher Lower Game!")
num = len(data) - 1
first = data[randint(0,num)]
second = data[randint(0,num)]
if first == second:
    first = data[randint(0,len(data))]

#Comparando e substituindo opções, definindo a vitória e os pontos
def win():
    global first
    global second
    global play
    global points
    if x == "A" and first[f] > second[f] or x == "B" and first[f] < second[f]:
        print("Well done!")
        points += 1
        if x == "B":
            first = second
        second = data[randint(0,len(data))]
    else:
        print(f"You lost. Your score is {points}")
        play = False


#mantendo o jogo on
while play == True:
    print(f"Compare A: {first[n]}, a {first[d]}, from {first[c]}")
    print(f"vs B: {second[n]}, a {second[d]}, from {second[c]}")
    x = str(input("Who has more followers?"))
    win()
