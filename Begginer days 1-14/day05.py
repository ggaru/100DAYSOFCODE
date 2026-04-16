#Setando uma lista de frutas
import random

fruits = ["Maça", "Pera", "Laranja"]
#O operador For é um operador de LOOP'S em Python.
#O que o For faz é executar uma ação x vezes, dada uma condição, que neste caso é, traduzindo:
#Para cada item (fruit) na lista (fruits), ele irá printar o item (fruit). Todo o código abaixo acontecerá cada vez que o For for chamado.
for fruit in fruits:
    print(fruit)

#Exemplificação de uso
score = [150, 2, 156, 56, 209, 19, 88, 63, 26, 49]
#A função sum() reune todos os dados a ela atribuidos e faz uma soma.
print(sum(score))
#Uso do For para soma dos itens
#Após set de var, é feito a ronda nos itens da lista e a cada item verificado, soma-se à var i o valor de cada item. Mesma função do sum()
total = 0
for i in score:
    total +=i
print(total)

#Prática 01 - Cópia da função max()
print(max(score))
max_n = 0
for n in score:
    if max_n < n:
        max_n = n
#A função Range() define 3 valores, o número minimo, o numéro máximo e o incrementador.
#O que ela faz é basicamente delimitar aonde o For deve continuar. Para cada i no range de 0 até 7, pois não conta-se o último, será executado um código
#O incrementador aumenta o valor. O retorno serão os números de 0 à 8, aumentando de 2 em 2
for i in range (0,8,2):
    print(i)

#Prática 02 - Soma de números
x = 0
for i in range(1,101):
    x+=i
print(x)
print(6%3)

#Prática 03 - FizzBuzz
for j in range(1,101):
    if (j%3)==0 and (j%5)==0:
        print("FizzBuzz")
    elif( j% 3) == 0:
        print("Fizz")
    elif (j % 5) == 0:
         print("Buzz")
    else:
        print(j)

    #DESAFIO DIA 05 - PASSWORD GENERATOR

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

let = int(input("Quantas letras vc gostaria"))
num = int(input("Quantos numero vc gostaria"))
sym = int(input("Quantos simbolo vc gostaria"))
password = []
for n in range(0,let):
    x = random.randint(0,len(letters)-1)
    password.append(letters[x])

for n in range(0,num):
    x = random.randint(0,len(numbers)-1)
    password.insert(random.randint(0,len(password)-1),numbers[x])

for n in range(0,sym):
    x = random.randint(0,len(symbols)-1)
    password.insert(random.randint(0, len(password) - 1), symbols[x])

passw = ""
for char in password:
    passw += char
print(passw)