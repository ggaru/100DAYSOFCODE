
#Importing important classes and creating variables
import random
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
pc_cards = []
user_cards = []
playing = False
user_points = 0

#Function created to get the pc hands
def get_pc_cards(qntd):
    """THIS FUNCTION WILL GET CARDS FOR THE PC BASED ON THE NUMBER PASSED"""
    global pc_points
    #for every item in the range that's called
    for i in range(0, qntd):
        ## the function will add a random card choosed in card list
        card = random.choice(cards)
        #adding the card and points to the pc
        pc_cards.append(card)
        pc_points += card
        #if the points are higher than 21 and there's a 11 on the list
        if pc_points > 21 and 11 in pc_cards:
            #this will change the card to 1 and get 10 points down
            pc_cards[pc_cards.index(11)] = 1
            pc_points -= 10

def get_plyr_cards(qntd):
    """THIS FUNCTION WILL GET CARDS FOR THE PLAYER BASED ON THE NUMBER PASSED"""
    global user_cards
    global user_points
    global pc_cards

    #for every item in the number passed
    for i in range(0, qntd):
        ##the game will also get cards for the player's hand and add points
        card = random.choice(cards)
        user_cards.append(card)
        user_points += card

        if user_points > 21:
            if 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_points -=10

    print(f"Your cards are {user_cards}")
    print(f"You have {user_points} points.")
    print(f"Computer's hand: {pc_cards[0]}")

    #if user points is higher than 21 even after the substitution, game ends
    if user_points > 21:
        endgame()

def endgame():
    """THIS FUNCTION CONTROLS THE END OF THE GAME"""
    global user_cards
    global user_points
    global pc_cards
    global pc_points
    global playing

    #if game did'nt end for burnout of player's hand
    if user_points <= 21:
        #get pc cards while he is not higher than 21 and not higher than player cards
        while pc_points < user_points and pc_points < 21:
            get_pc_cards(1)


    print(f"Your hand was {user_cards}. And your final points was {user_points}")
    print(f"The computer hand was {pc_cards}. And his final points was {pc_points}")

    #Controlling who wins
    if user_points == pc_points:
        print("Empate")
    elif user_points > 21:
        print("You lose")
    elif pc_points > 21:
        print("You win.")
    elif user_points > pc_points:
        print("You win")
    else:
        print("you lose")
    restart()

def restart():
    """THIS FUNCTION RESTART THE GAME"""
    global user_cards
    global pc_cards
    global playing
    global user_points
    global pc_points

    #If user wants to continue playing blackjack, all the variables are gonna be restarted
    if input("Wanna play blackjack?") != "n":
        user_cards = []
        pc_cards = []
        user_points = 0
        pc_points = 0
        get_pc_cards(1)
        get_plyr_cards(2)
        playing = True
    else:
        playing = False

restart()

while playing == True:
    if input("Wanna draw another card?") !=  "n":
        get_plyr_cards(1)
    else:
        endgame()