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
            deck.append(Card(1,11,tmp_id,resource_path('ah.png')))
            tmp_id+=1
            deck.append(Card(1,11,tmp_id,resource_path('ac.png')))
            tmp_id+=1
            deck.append(Card(1,11,tmp_id,resource_path('ad.png')))
            tmp_id+=1
            deck.append(Card(1,11,tmp_id,resource_path('as.png')))
            tmp_id+=1
            deck.append(Card(2,0,tmp_id,resource_path('2h.png')))
            tmp_id+=1
            deck.append(Card(2,0,tmp_id,resource_path('2c.png')))
            tmp_id+=1
            deck.append(Card(2,0,tmp_id,resource_path('2d.png')))
            tmp_id+=1
            deck.append(Card(2,0,tmp_id,resource_path('2s.png')))
            tmp_id+=1
            deck.append(Card(3,0,tmp_id,resource_path('3h.png')))
            tmp_id+=1
            deck.append(Card(3,0,tmp_id,resource_path('3c.png')))
            tmp_id+=1
            deck.append(Card(3,0,tmp_id,resource_path('3d.png')))
            tmp_id+=1
            deck.append(Card(3,0,tmp_id,resource_path('3s.png')))
            tmp_id+=1
            deck.append(Card(4,0,tmp_id,resource_path('4h.png')))
            tmp_id+=1
            deck.append(Card(4,0,tmp_id,resource_path('4c.png')))
            tmp_id+=1
            deck.append(Card(4,0,tmp_id,resource_path('4d.png')))
            tmp_id+=1
            deck.append(Card(4,0,tmp_id,resource_path('4s.png')))
            tmp_id+=1
            deck.append(Card(5,0,tmp_id,resource_path('5h.png')))
            tmp_id+=1
            deck.append(Card(5,0,tmp_id,resource_path('5c.png')))
            tmp_id+=1
            deck.append(Card(5,0,tmp_id,resource_path('5d.png')))
            tmp_id+=1
            deck.append(Card(5,0,tmp_id,resource_path('5s.png')))
            tmp_id+=1
            deck.append(Card(6,0,tmp_id,resource_path('6h.png')))
            tmp_id+=1
            deck.append(Card(6,0,tmp_id,resource_path('6c.png')))
            tmp_id+=1
            deck.append(Card(6,0,tmp_id,resource_path('6d.png')))
            tmp_id+=1
            deck.append(Card(6,0,tmp_id,resource_path('6s.png')))
            tmp_id+=1
            deck.append(Card(7,0,tmp_id,resource_path('7h.png')))
            tmp_id+=1
            deck.append(Card(7,0,tmp_id,resource_path('7c.png')))
            tmp_id+=1
            deck.append(Card(7,0,tmp_id,resource_path('7d.png')))
            tmp_id+=1
            deck.append(Card(7,0,tmp_id,resource_path('7s.png')))
            tmp_id+=1
            deck.append(Card(8,0,tmp_id,resource_path('8h.png')))
            tmp_id+=1
            deck.append(Card(8,0,tmp_id,resource_path('8c.png')))
            tmp_id+=1
            deck.append(Card(8,0,tmp_id,resource_path('8d.png')))
            tmp_id+=1
            deck.append(Card(8,0,tmp_id,resource_path('8s.png')))
            tmp_id+=1
            deck.append(Card(9,0,tmp_id,resource_path('9h.png')))
            tmp_id+=1
            deck.append(Card(9,0,tmp_id,resource_path('9c.png')))
            tmp_id+=1
            deck.append(Card(9,0,tmp_id,resource_path('9d.png')))
            tmp_id+=1
            deck.append(Card(9,0,tmp_id,resource_path('9s.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('10h.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('10c.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('10d.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('10s.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('jh.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('jc.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('jd.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('js.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('qh.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('qc.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('qd.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('qs.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('kh.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('kc.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('kd.png')))
            tmp_id+=1
            deck.append(Card(10,0,tmp_id,resource_path('ks.png')))
            tmp_id+=1
            return deck #and return the list of cards
        elif deckType == 'aces':
            deck = [] # Store the cards here
            tmp_id = 1 # This will set our card ids
            #Now we add 52 aces to test with
            for ace in range(52):
                deck.append(Card(1,11,tmp_id,resource_path('as.png')))
                tmp_id+=1
            return deck #and return the list of cards
        else:
            return # I put this here in case I decide to add different deck configurations (I probably won't)

