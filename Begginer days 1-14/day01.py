#Código mais básico em python. Printa algo no console com a função print().
#print("Eu consigo.")

#Quebra de linha, utilizando \n
#print("Eu consigo. \n Eu sou capaz.")

#Combina as duas strings, utilizando o +.
#print("Eu consigo." +  "Eu sou capaz.")
#No caso de int's, são somadas.
#print(8.5 + 7)

#Usa a função input() para que o usuário escreva algo no console.
#input("Vai desistir?")
#Outro uso
#O programa ira rodar esse código, lendo toda a função print e depois, a função input, coletando todas as informações e retornando "Olá (nome)"
#print ("Olá " + input("Qual seu nome?"))

#Váriaveis são conjunto de dados que podem ser String's, Int's, Float's ou Boolean's, no qual se é passado uma informação e atribuido à ela.
#Fazendo com que o nome seja referência áquela informação dentro da memória do computador.
#name = "Vini"
#print(name)
#name = "Angela"
#print(name)

#DESAFIO DIA 01 - BAND NAME GENERATOR
#Fazer um programa que gere o nome de um banda de acordo com o nome da sua cidade e do seu animal.
#version1
#print("Bem vindo ao BandName Generator!")
#city = input("Qual cidade você nasceu?\n-")
#pet = input("Qual o nome do seu pet?\n-")
#print("O nome da sua banda é: " + city +" " + pet)

print("Bem vindo ao BandName Generator!")
print("O nome da sua banda é: " +  input("Qual cidade voce nasceu?: ") +" " input("Qual nome do seu pet?: ") )