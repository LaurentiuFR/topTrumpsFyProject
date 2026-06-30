import random

#card class
class card:
    def __init__(self,name,hgt,wgt,lgt,yrs,kr,iq):
        self.name = name
        #dictionary that accesses all the attributes needed for compariosn
        self.attributes = {
            "Height (m)": hgt,
            "Weight (kg)": wgt,
            "Length (m)": lgt,
            "Age (years)": yrs,
            "Killer Rating": kr,
            "Intelligence": iq,
        }

    def getAttribute(self,attributeName):
        if attributeName in self.attributes:
            return self.attributes[attributeName]
        else:
            return f"Attribute {attributeName} does not exist,\n Try retyping it."

    def highestAttribute(self):
        #this is useful for what the bot will be choosing.
        return max(self.attributes,key=self.attributes.get)

    def __str__(self):
        #display the cards name and attributes
        eachLine = [f"{key}: {value}" for key, value in self.attributes.items()]
        return f"{self.name}\n" + "\n".join(eachLine)

def avaliableCards():
    cardTri = card("Triceratops",3,5500,9,72,2,4)
    cardBar = card("Barosaurus",26,40000,26,156,3,2)
    cardHyp = card("Hypsilophodon",0.8,50,2,125,1,6)
    cardIgua = card("Iguanodon",5,4500,10,135,3,6)
    cardTrx = card("Tyrannosaurus Rex",5.6,6000,12,67,9,9)
    cardBra = card("Brachiosaurus",16,80000,26,156,3,2)
    cardSuch = card("Suchomimus",4,4000,12,100,8,7)
    cardGall = card("Gallimimus",3,200,5.6,74,5,7)
    cardCento = card("Centrosaurus",2,1000,6,76,2,4)
    cardOvir = card("Oviraptor",0.8,20,1.8,70,5,8)


    return [cardTri, cardBar,cardHyp,cardIgua,cardTrx,cardBra,cardSuch,cardGall,cardCento,cardOvir]

class stackOfCards:

    def __init__(self,name):
        self.name = name
        self.cards = []

    def push(self,cardObj):
        self.cards.append(cardObj)

    def pop(self):
        if not self.isEmpty():
            return self.cards.pop()
        else:
            print(f"{self.name} has no more cards!")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.cards[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.cards) == 0

    def size(self):
        return len(self.cards)

    def __str__(self):
        return f"{self.name} - {self.size()} cards remaining"
def shuffleCards():
    # receives the cards, shuffles them and pushes them into main deck
    listOfCards = avaliableCards()
    random.shuffle(listOfCards)

    deckStack = stackOfCards("Main Deck Stack")
    for card in listOfCards:
        deckStack.push(card)

    return deckStack

def dealCards(deckStack):
    playerHand = []  # List to hold player's cards
    botHand = []     # List to hold bot cards

    turn = 0  # 0 = Player's turn, 1 = Bot turn

    while not deckStack.isEmpty():
        card = deckStack.pop()

        if turn == 0:
            playerHand.append(card)
            turn = 1  # Switch to bot
        else:
            botHand.append(card)
            turn = 0  # Switch back to player

    return playerHand, botHand

deck = shuffleCards()         # Creates the shuffled deck
playerHand, botHand = dealCards(deck)  # Deal the cards
def choosePlayerCard(playerHand): # player chooses a card
    print("\nYour Cards:")
    for index, card in enumerate(playerHand):
        print(f"{index+1}: {card.name}")

    choice = int(input("\nChoose your card number: ")) - 1

    while choice < 0 or choice >= len(playerHand):
        print("Invalid choice. Please choose again.")
        choice = int(input("Choose your card number: ")) - 1

    return playerHand.pop(choice)

def chooseAttribute(card):
    attributes = list(card.attributes.keys())  # get all attribute names

    print("\nAvailable Attributes and their Values:")
    for index, attribute in enumerate(attributes):
        value = card.getAttribute(attribute)
        print(f"{index + 1}: {attribute} ({value})")

    choice = input("\nChoose an attribute number: ")

    # Validate input
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(attributes):
        print("Invalid choice. Try again.")
        choice = input("Choose an attribute number: ")

    chosen_attribute = attributes[int(choice) - 1]
    return chosen_attribute

def chooseBotCard(botHand):
    bot_card = random.choice(botHand)
    botHand.remove(bot_card)
    return bot_card

def compareCards(playerCard, botCard, attribute):
    player_value = playerCard.getAttribute(attribute)
    bot_value = botCard.getAttribute(attribute)

    print("\nBattle Result:")
    print(f"Your {playerCard.name} - {attribute}: {player_value}")
    print(f"Bots {botCard.name} - {attribute}: {bot_value}")

    if player_value > bot_value:
        print("You win this round!\n")
        return "player"
    elif player_value < bot_value:
        print("Bot wins this round!\n")
        return "bot"
    else:
        print("It's a draw!\n")
        return "draw"

def playGame(playerHand, botHand):
    while len(playerHand) > 0 and len(botHand) > 0:
        print("\n--------------------------------------------------")

        playerCard = choosePlayerCard(playerHand)
        chosenAttribute = chooseAttribute(playerCard)
        botCard = chooseBotCard(botHand)

        print("\nBot chose its card!")

        winner = compareCards(playerCard, botCard, chosenAttribute)

        if winner == "player":
            playerHand.append(playerCard)
            playerHand.append(botCard)
        elif winner == "bot":
            botHand.append(playerCard)
            botHand.append(botCard)
        else:  # draw
            playerHand.append(playerCard)
            botHand.append(botCard)

        print(f"\nYou have {len(playerHand)} cards left.")
        print(f"Bot has {len(botHand)} cards left.")

    # Check who won the game
    if len(playerHand) > 0:
        print("\nYou won the game! Congratulations!")
    else:
        print("\nBot won the game! Better luck next time.")

def welcome():

    print("""
     ----------------------------------------------------------------------------------
    |->                               Top Trumps: Dino                               <-|
    |                                                                                  |
    |        •In order to be able to play, read the rules and sign in or sign up       |
    |                                                                                  |
    |->                              Rules: How to Play                              <-|
    |                                                                                  |
    |                1) Computer will randomly select who plays first!                 |
    |                2) Whoever goes first will get to choose a card                   |
    |                   and an attribute.                                              |
    |                3) The opponent also gets to choose their card.                   |
    |                4) The winner of the round will receive the cards                 |
    |                   that were placed. Turns switch                                 |
    |                5) If it happens that the value of the attribute                  |
    |                   chosen is the same for both cards. Then                        |
    |                   Both players get to pick another card.                         |
    |                   In a winner takes all style.                                   |
    |                                                                                  |
     ----------------------------------------------------------------------------------
    """)
def playerVerifySys(user):  #Subprogram that will verify the users met the criteria for the password making
    if user.isdigit():
        print("Your username is not allowed – made up of only integers")
        isValid = False
    else:
        isValid = True
    return isValid
def database(user,option):

    #database check
    check = True # assume user is not already in database
    with open('database.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if user == line:
                check = False
                break # if the user is found no need to continue.

    #user sign up once check is complete
    if check and playerVerifySys(user) and option == 1:
        with open("database.txt", 'a') as f:
            f.write(f"{user}\n")
            print("Username accepted, criteria have been met.\nYour Username has been added to our database")
    elif not check and playerVerifySys(user) and option == 1:
        print("Username already exists, Try again or log in.")
    #user log in requires check
    elif not check and playerVerifySys(user) and option == 2:
        print("You've logged in successfully!")
        Logged = True
        return Logged

    if check and playerVerifySys(user) and option == 2:
        print("The information provided is incorrect. \nTry a different username or sign up!")
def mainMenu():
    menuShow = True
    Logged = False # assume the user has not logged in yet.
    while menuShow == True and Logged == False:
        option = input("""
             ----------------------------------------------------------------------------------
            |                                     Menu                                         |
            |                                                                                  |
            |           1 - Sign Up                              2 - Log in                    |
            |                                                                                  |
            |           3 - Rules                                4 - Quit                      |   
            |                                                                                  |
             ----------------------------------------------------------------------------------

             Choose an option 1 to 4:

            """) # option variable kept as string to check that it is actually of type string due to input turning everything into int
        if int(option) == 1 or int(option) == 2:
            playerUsername = input("Username: ")  # input Username from user.
            if playerVerifySys(playerUsername) and int(option) == 1:
                database(playerUsername,1)
            elif playerVerifySys(playerUsername) and int(option) == 2:
                Logged = database(playerUsername,2)
                if Logged:
                    #game function call
                    print("Welcome to your game")
                    deck = shuffleCards()
                    playerHand, botHand = dealCards(deck)
                    playGame(playerHand, botHand)

        if int(option) == 3:
            welcome()
            input("Press enter once done reading to go back to menu")
        if int(option) == 4:
            print("Thanks for trying the game!")
            menuShow = False
            quit()
        elif option.isdigit() == False or int(option) >4 or int(option)<1:
            print("             Please choose out of the available options\n"
                  "             It has to be a number and it has to be between 1 and 4       ")


mainMenu()
