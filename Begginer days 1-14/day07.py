#DESAFIO DAY 07 - HANGMAN GAME
#Criar um programa de forca.
#todo 01 - Criar uma lista com palavra e aleatóriamente escolher um para o jogo
#todo 02 - Fazer o usuário escolher uma letra e, caso seja a correta, mostrar a palavra trocando os '_' pela letra escolhida
#todo 02.1 - Caso a letra esteja incorreta, retirar 1 vida do usuário, ou remover 1 tentativa
import random

global playing #variavel de controle. Checha se o jogo ta rolando
global letters #variavel de controle. Guarda as letras escolhidas
global guess #variavel de comando. É a variavel que o usuário irá nos dar
global life #variavel de controle. Quantidade de tentativas do usuário

playing = True
letters = []
life = 5

#Função que irá escolher a palavra de uma lista. O retorno dessa função é a palavra escolhida e uma lista censurada.
def chosing_word():
    #Lista com as palavras
    list_words = ["batata", "goiaba", "macaxeira", "sorvete", "banana", "pizza", "sushi", "macarrao", "indio", "beterraba", "joao",
                  "macarronada", "portugues", "espanha", "legumes", "japao", "enterro", "caixa", "limao", "testamento"]
    global rand_word
    rand_word = random.choice(list_words)
    global list_guess
    list_guess = []

    for i in rand_word:
        list_guess.append("_ ")

    #DEBUG
    #print(rand_word)
    #print(list_guess)

def guessing_word():
    #Essa função pergunta ao usuário por uma letra e então, troca-a pela lista censurada no seu mesmo index
    global rand_word
    global list_guess
    global letters
    global guess
    global life
    global playing

    #print(rand_word)

    censor_word()
    guess = input("Escolha uma letra: ")

    n = 0
    check_word()

    #se não escolhi a letra
    if check_word() == False:
        #se a letra ta na palavra
        if guess in rand_word:
            for i in rand_word:
                if guess == i:
                    list_guess.pop(n)
                    list_guess.insert(n,i +" ")
                n += 1
            if not "_ " in list_guess:
                print("Você achou a palavra!")
                censor_word()
                playing = False
        #se a letra não está na palavra
        else:
            life -= 1
            print(f"Essa letra não está na palavra. Você perdeu uma vida e esta com: {life}")
            if life <= 0:
                print(f"Você perdeu. A palavra era: {rand_word}")

                playing = False

    else:
        print("Você já escolheu essa letra.")
    letters.append(guess)
    #print(letters)

def censor_word():
    #Essa função pega a lista censurada e transforma em uma string
    global rand_word
    global list_guess
    global guessed
    guessed = ""
    for i in list_guess:
        guessed += i
    print(guessed)

def check_word():
    global letters
    #já escolhi essa letra
    if guess in letters:
        return True
    #ainda não escolhi
    else:
        return False

chosing_word()
while playing:
    guessing_word()
