from pyinstaller_functions import resource_path # This helps pyinstaller package resources for single file executables 'pyinstaller_functions.py'
class Card:
    def __init__(self, value_1, value_2, card_id, image): # Create our card object
        self.value_1 = value_1 # Value of card
        self.value_2 = value_2 # Secondary value we'll set to 0 unles it's an ace
        self.card_id = card_id # A unique ID for each card in the deck
        self.image = image # The card image

    def Build_Deck(deckType): # Function for building a deck
        if deckType == 'standard': # We'll create a single standard deck, only the card values and images are necessary, I've omitted suits
            deck = [] # Store the cards here
            tmp_id = 1 # This will set our card ids
            #Now we add four of each card to the deck (because there are no suits)
            for ace in range(4):
                deck.append(Card(1,11,tmp_id,resource_path('A.png')))
                tmp_id+=1
            for two in range(4):
                deck.append(Card(2,0,tmp_id,resource_path('2.png')))
                tmp_id+=1
            for three in range(4):
                deck.append(Card(3,0,tmp_id,resource_path('3.png')))
                tmp_id+=1
            for four in range(4):
                deck.append(Card(4,0,tmp_id,resource_path('4.png')))
                tmp_id+=1
            for five in range(4):
                deck.append(Card(5,0,tmp_id,resource_path('5.png')))
                tmp_id+=1
            for six in range(4):
                deck.append(Card(6,0,tmp_id,resource_path('6.png')))
                tmp_id+=1
            for seven in range(4):
                deck.append(Card(7,0,tmp_id,resource_path('7.png')))
                tmp_id+=1
            for eight in range(4):
                deck.append(Card(8,0,tmp_id,resource_path('8.png')))
                tmp_id+=1
            for nine in range(4):
                deck.append(Card(9,0,tmp_id,resource_path('9.png')))
                tmp_id+=1
            for ten in range(4):
                deck.append(Card(10,0,tmp_id,resource_path('10.png')))
                tmp_id+=1
            for jack in range(4):
                deck.append(Card(10,0,tmp_id,resource_path('J.png')))
                tmp_id+=1
            for queen in range(4):
                deck.append(Card(10,0,tmp_id,resource_path('Q.png')))
                tmp_id+=1
            for king in range(4):
                deck.append(Card(10,0,tmp_id,resource_path('K.png')))
                tmp_id+=1
            return deck #and return the list of cards
        elif deckType == 'aces':
            deck = [] # Store the cards here
            tmp_id = 1 # This will set our card ids
            #Now we add 52 aces to test with
            for ace in range(52):
                deck.append(Card(1,11,tmp_id,resource_path('A.png')))
                tmp_id+=1
            return deck #and return the list of cards
        else:
            return # I put this here in case I decide to add different deck configurations (I probably won't)

