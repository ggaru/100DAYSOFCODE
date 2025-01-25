
#Passagem de parametros
#Uma função, após definida, pode ou não ter parametros, que são caracteristas especificas daquela função
#que ao chama-lá devem ser passadas para que a função exerça seu objetivo
def hello(name):
    #a função Hello possui um parametro chamado Name, que ao ser recebida, irá printa-lo
    print(f"hello {name}")
    print(name)
#hello("Angela")#Chamando a função e passando pra ela o seu parametro

#Prática 01 - Vida em semanas
def life_in_weeks(age):
    weeks = 0
    for q in range(age,90):
        weeks += 52
    print(f"Sua vida ainda tem {weeks} semanas até os 90")
#age = int(input("Digite sua idade:"))
#life_in_weeks(age)

#Prática 02 - Love Calculator
#todo 01 - pegar duas entradas de nomes
#todo 02 - checar quantas vezes as letras da palavra TRUE aparecem nos dois nomes
#todo 03 - checar quantas vezes as letras da palavra LOVE aparece nos dois nomes
#todo 04 - concatenar os dois para dar o resultado esperado
#name1 = input("Digite seu nome: ")
#name2 = input("Digite o nome do seu parceiro: ")
true = ["t", "r","u", "e"]
love = ["l", "o", "v", "e"]
def truelove(name1, name2):
    t = 0
    l = 0
    for z in true:
        t += name1.count(z)
        t += name2.count(z)
    for n in love:
        l += name1.count(n)
        l += name2.count(n)
    print(f"O calculo de vocês é de: {t}{l}")
#truelove(name1, name2)

#DESAFIO DAY 08 - CEASER CYPHER

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
playing = True

def ceasar (message, shift, choose):
    message_encrypt = ""
    if choose == "decrypt":
        shift *= -1
    for i in message:
        if i in alphabet:
            ind = alphabet.index(i) + shift
            ind %= len(alphabet)
            message_encrypt += alphabet[ind]
            print(f"Debug {choose}, {shift}, {ind}, {message_encrypt}")
        else:
            message_encrypt += i
    print(message_encrypt)

while playing:
    choose = input("Welcome! do you wish do Encrypt or Decrypt a message?").lower()
    message = input("Write the message: ")
    shift = int(input("Number of shifts: "))
    ceasar(message, shift, choose)
    if input("Types Yes if you want to go again") != "yes":
        playing = False