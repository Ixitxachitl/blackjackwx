import sys, os # For input, exiting
import wx # A Python implementation of the wx libraries (windows apps)
import gettext # Needed for wxGlade generated layouts
from threading import Thread # so we can do calculations in the background
from random import shuffle # Perfect function for this application
from deck_functions import Card # I've created a class to contain card information and functions 'deck_functions.py'
from pyinstaller_functions import resource_path # This helps pyinstaller package resources for single file executables 'pyinstaller_functions.py'

class MAIN(wx.Frame):
    def dealer_draw(self):# A function for drawing cards into the dealer's hand, read this after this function is called
        self.dealer_hand.append(self.deck[self.draw_index])# Add a card
        self.draw_index += 1 # Increment the draw index everytime we add a card
        print("Dealer Drew: " + str(self.dealer_hand[len(self.dealer_hand)-1].card_id))
        if self.dealer_hand[len(self.dealer_hand)-1].value_2 == 0: # Fancy way of saying if the drawn card isn't an ace
            for score in range(len(self.dealer_score)): # Iterate through the list of scores (only multiple if ace was drawn)
                if self.dealer_score[score-1] + self.dealer_hand[len(self.dealer_hand)-1].value_1 <= 21: # Did you bust?
                    self.dealer_score[score-1] += self.dealer_hand[len(self.dealer_hand)-1].value_1 # No add the new card to the score
                else:
                    if len(self.dealer_score) == 1: # Yes, that was the dealers last chance to win
                        print("Dealer Bust")
                        self.statusbar.SetStatusText("You Win")
                        self.dealer_score[score-1] += self.dealer_hand[len(self.dealer_hand)-1].value_1 # We'll hold onto his score just for fun
                    else:
                        del self.dealer_score[score-1] # If there were multiple scores we can remove any that go over 21
        else: # If it is an ace
            add_score = [] # A temporary list to hold new values
            for score in range(len(self.dealer_score)): # Iterate through the list of scores (only multiple if ace was drawn)
                if self.dealer_score[score-1] + self.dealer_hand[len(self.dealer_hand)-1].value_2 <= 21: # If adding 11 doesn't bust
                    add_score.append(self.dealer_score[score-1] + self.dealer_hand[len(self.dealer_hand)-1].value_2) # Hold onto any value here
                if self.dealer_score[score-1] + self.dealer_hand[len(self.dealer_hand)-1].value_1 <= 21: # If adding 1 doesn't bust (when would it? maths)
                    self.dealer_score[score-1] += self.dealer_hand[len(self.dealer_hand)-1].value_1 # Add 1
                else: # And if somehow you added 1 and got 22, I'm not sure if this is possible beyond this point
                    if len(self.dealer_score) == 1:
                        print("Dealer Bust")
                        self.statusbar.SetStatusText("You Win")
                        self.dealer_score[score-1] += self.dealer_hand[len(self.dealer_hand)-1].value_1
                    else:
                        self.dealer_score.pop(score-1)
            for score in range(len(add_score)): # Add any aditional scores to the score
                self.dealer_score.append(add_score[score])
        print("Dealer Score: ", end="", flush=True)
        print(*list(set(self.dealer_score)), sep = ", ")
        if 21 in self.dealer_score: # Did the dealer win?
            print ("Dealer Wins!")
            self.statusbar.SetStatusText("You Lose")
            #win_dialogue(false)
        lbl2=' or '.join(str(e) for e in list(set(self.dealer_score))) # Updates the dealer score in the wx window
        self.label_4.SetLabel(lbl2)
        self.update_cards()
        if max(self.dealer_score) <= 21:
            if max(self.dealer_score) < 17:
                self.dealer_draw()
            elif max(self.dealer_score) >= max(self.player_score):
                self.statusbar.SetStatusText("You Lose")
            else:
                self.statusbar.SetStatusText("You Win")
        
        

    def player_draw(self): # Pretty much the same as dealer_draw without the AI
        self.player_hand.append(self.deck[self.draw_index])# Add a card
        self.draw_index += 1 # Increment the draw index everytime we add a card
        print("Player Drew: " + str(self.player_hand[len(self.player_hand)-1].card_id))
        if self.player_hand[len(self.player_hand)-1].value_2 == 0: # Fancy way of saying if the drawn card isn't an ace
            for score in range(len(self.player_score)): # Iterate through the list of scores (only multiple if ace was drawn)
                if self.player_score[score-1] + self.player_hand[len(self.player_hand)-1].value_1 <= 21: # Did you bust?
                    self.player_score[score-1] += self.player_hand[len(self.player_hand)-1].value_1 # No add the new card to the score
                else:
                    if len(self.player_score) == 1: # Yes, that was the your last chance to win
                        print("Player Bust")
                        self.statusbar.SetStatusText("You Lose")
                        self.button_1.Enable(False) # Disables the buttons 
                        self.button_2.Enable(False)
                        self.player_score[score-1] += self.player_hand[len(self.player_hand)-1].value_1 # We'll hold onto his score just for fun
                    else:
                        del self.player_score[score-1] # If there were multiple scores we can remove any that go over 21
        else: # If it is an ace
            add_score = [] # A temporary list to hold new values
            for score in range(len(self.player_score)): # Iterate through the list of scores (only multiple if ace was drawn)
                if self.player_score[score-1] + self.player_hand[len(self.player_hand)-1].value_2 <= 21: # If adding 11 doesn't bust
                    add_score.append(self.player_score[score - 1] + self.player_hand[len(self.player_hand)-1].value_2) # Hold onto any value here
                if self.player_score[score-1] + self.dealer_hand[len(self.dealer_hand)-1].value_1 <= 21: # If adding 1 doesn't bust (when would it? maths)
                    self.player_score[score-1] += self.player_hand[len(self.player_hand)-1].value_1 # Add 1
                else: # And if somehow you added 1 and got 22, I'm not sure if this is possible beyond this point
                    if len(self.player_score) == 1:
                        print("player Bust")
                        self.statusbar.SetStatusText("You Lose")
                        self.player_score[score-1] += self.player_hand[len(self.player_hand)-1].value_1
                    else:
                        self.player_score.pop(score-1)
            for score in range(len(add_score)): # Add any aditional scores to the score
                self.player_score.append(add_score[score-1])
        print("Player Score: ", end="", flush=True)
        print(*list(set(self.player_score)), sep = ", ")
        if 21 in self.player_score: # Did the player get 21?
            print ("Player Stays")
            self.button_1.Enable(False) # Disables the buttons 
            self.button_2.Enable(False)
            self.dealer_draw()
        lbl1=' or '.join(str(e) for e in list(set(self.player_score))) # Updates the players score in the wx window
        self.label_2.SetLabel(lbl1)
        self.update_cards()

    def update_cards(self):
        for card in range(len(self.dealer_cards)):
            try:
                self.dealer_cards[card].SetBitmap(wx.Image(self.dealer_hand[card].image,wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            except:
                self.dealer_cards[card].SetBitmap(wx.Image(resource_path("blank.png"),wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        
        for card in range(len(self.player_cards)):
            try:
                self.player_cards[card].SetBitmap(wx.Image(self.player_hand[card].image,wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            except:
                self.player_cards[card].SetBitmap(wx.Image(resource_path("blank.png"),wx.BITMAP_TYPE_ANY).ConvertToBitmap())                
        
    #Our setup gameplay function
    def run(self):
        self.button_1.Enable(False) # Disables the buttons if they had perviously been enabled
        self.button_2.Enable(False)
        #self.deck = Card.Build_Deck('standard')# Setup the deck
        self.deck = Card.Build_Deck('standard')
        shuffle(self.deck)# Shuffle the deck
        self.draw_index = 0# This is the index of the last card that was drawn, the first card being 0

        '''### This prints out data about all of the cards in the deck in the shuffled order
        for card, card_id in enumerate(self.deck):
            print(str(self.deck[card].card_id) + ' - ' + str(self.deck[card].value_1), end="", flush=True)
            if self.deck[card].value_2 != 0: # Or if it's an ace
                print(' - ' + str(self.deck[card].value_2), end="", flush=True)
            print(' - ' + self.deck[card].image)
        ### ...'''
            
        self.player_hand = [] # This is where we'll store the players hand
        self.dealer_hand = [] # This is where we'll store the dealers hand
        self.player_hand.append(self.deck[self.draw_index])# Player draws
        self.draw_index += 1 #Increment the draw index every time we draw a card
        self.dealer_hand.append(self.deck[self.draw_index])# Dealer draws
        self.draw_index += 1
        self.player_hand.append(self.deck[self.draw_index])
        self.draw_index += 1

        #Displays the card IDs of the hands, complecated because we're looking through objects
        print("Player Hand: ", end="", flush=True)
        for card, card_id in enumerate(self.player_hand):
            print(str(self.player_hand[card].card_id) + " " , end="", flush=True)
        print()
        
        print("Dealer Hand: ", end="", flush=True)
        for card, card_id in enumerate(self.dealer_hand):
            print(str(self.dealer_hand[card].card_id) + " " , end="", flush=True)
        print()

        # Fiugure out the player's score
        self.player_score = [self.player_hand[0].value_1 + self.player_hand[1].value_1] # always the first values
        if self.player_hand[0].value_2 != 0: # is the first card an ace?
            if self.player_hand[0].value_2 + self.player_hand[1].value_1 <= 21: # does the second card plus 11 bust?
                self.player_score.append(self.player_hand[0].value_2 + self.player_hand[1].value_1) # no, add it to the players scores
        if self.player_hand[1].value_2 != 0: # is the second card an ace?
            if self.player_hand[1].value_2 + self.player_hand[0].value_1 <= 21: # does the first card plus 11 bust?
                self.player_score.append(self.player_hand[1].value_2 + self.player_hand[0].value_1)# no, add it to the players scores
        if self.player_hand[0].value_2 != 0 and self.player_hand[1].value_2 != 0: # are both cards aces?
            if self.player_hand[0].value_2 + self.player_hand[1].value_2 <= 21: # if 22 is under 22 then add it to the score (for maths)
                self.player_score.append(self.player_hand[0].value_2 + self.player_hand[1].value_2)

        # Dealer starts with 1 card
        self.dealer_score = [self.dealer_hand[0].value_1] # always the first value
        if self.dealer_hand[0].value_2 != 0: # is it an ace?
            self.dealer_score.append(self.dealer_hand[0].value_2) # yes, add 11
            
        print("Player Score: ", end="", flush=True)
        print(*list(set(self.player_score)), sep = ", ") # Shows all possible scores so far and removes duplicate entries
        print("Dealer Score: ", end="", flush=True)
        print(*list(set(self.dealer_score)), sep = ", ") # "
        if 21 in self.player_score: # Player stays on 21
            print ("Player Stays")
            self.dealer_draw()
        else:
            self.button_1.Enable(True) # Enable the buttons if player didn't get 21 on initial draw
            self.button_2.Enable(True)
        lbl1=' or '.join(str(e) for e in list(set(self.player_score)))
        lbl2=' or '.join(str(e) for e in list(set(self.dealer_score)))
        self.label_2.SetLabel(lbl1)
        self.label_4.SetLabel(lbl2)
        self.update_cards()
        #self.Refresh()
        #If player didn't bust start dealer cycle    
        
    def __init__(self, *args, **kwds):
        self.playerscore = 0
        self.dealerscore = 0
        self.dealer_cards = []
        self.player_cards = []
        self.overlay = wx.Overlay()
        # begin wxGlade: MAIN.__init__
        kwds["style"] = kwds.get("style", 0) | wx.BORDER_SIMPLE | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((480, 300))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("&New Game"), "")
        self.Bind(wx.EVT_MENU, self.ON_RESTART, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("&Quit"), "")
        self.Bind(wx.EVT_MENU, self.ON_QUIT, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, _("&File"))
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Hit"), style=wx.BU_AUTODRAW)
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Stand"), style=wx.BU_AUTODRAW)
        self.button_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Image(resource_path("refresh.png"),wx.BITMAP_TYPE_ANY).ConvertToBitmap(), style=wx.BU_AUTODRAW)
        

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.ON_HIT, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.ON_STAND, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.ON_RESTART, self.button_3)
        # end wxGlade
        self.statusbar = self.CreateStatusBar(1)
        self.run()

    def __set_properties(self):
        # begin wxGlade: MAIN.__set_properties
        self.SetTitle(_("Blackjack"))
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(resource_path("A.bmp"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.button_1.SetMinSize((50, 32))
        self.button_1.Enable(False)
        self.button_2.SetMinSize((50, 32))
        self.button_2.Enable(False)
        self.button_3.SetMinSize((32, 32))
        # end wxGlade
        
    def __do_layout(self):
        # begin wxGlade: MAIN.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        static_line_3 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_2.Add(static_line_3, 0, wx.EXPAND, 0)
        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, _("D\nE\nA\nL\nE\nR"))
        sizer_3.Add(label_5, 1, wx.LEFT | wx.RIGHT, 4)
        no_card_img = wx.Image(resource_path("0.png"),wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #no_card_img = wx.Bitmap(resource_path("0.bmp"),wx.BITMAP_TYPE_ANY)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[0].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[0], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[1].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[1], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[2].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[2], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[3].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[3], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[4].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[4], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[5].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[5], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[6].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[6], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[7].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[7], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[8].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[8], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[9].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[9], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.dealer_cards.append(wx.StaticBitmap(self.panel_2))
        self.dealer_cards[10].SetBitmap(no_card_img)
        sizer_5.Add(self.dealer_cards[10], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.panel_2.SetSizer(sizer_5)
        sizer_3.Add(self.panel_2, 99, wx.BOTTOM | wx.EXPAND | wx.LEFT, 2)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        static_line_2 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_2.Add(static_line_2, 0, wx.EXPAND, 0)
        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, _("P\nL\nA\nY\nE\nR"))
        sizer_4.Add(label_6, 1, wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[0], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[1], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[2], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[3], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[4], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[5], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[6], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[7], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[8], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[9], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.player_cards.append(wx.StaticBitmap(self.panel_3, wx.ID_ANY, no_card_img))
        sizer_6.Add(self.player_cards[10], 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        self.panel_3.SetSizer(sizer_6)
        sizer_4.Add(self.panel_3, 99, wx.BOTTOM | wx.EXPAND | wx.LEFT, 2)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 90, wx.EXPAND, 0)
        static_line_4 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_4, 0, wx.EXPAND, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, _("Player Score: "), style=wx.ALIGN_LEFT)
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_BOTTOM | wx.CENTER, 0)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, str(self.playerscore), style=wx.ALIGN_LEFT)
        self.label_2.SetMinSize((50, -1))
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        grid_sizer_1.Add(static_line_1, 0, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _("Dealer Score: "), style=wx.ALIGN_LEFT)
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_BOTTOM | wx.LEFT, 2)
        self.label_4 = wx.StaticText(self, wx.ID_ANY, str(self.dealerscore))
        self.label_4.SetMinSize((50, -1))
        grid_sizer_1.Add(self.label_4, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 0)
        static_line_5 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        grid_sizer_1.Add(static_line_5, 0, wx.EXPAND | wx.RIGHT, 30)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 2)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 30)
        grid_sizer_1.Add(self.button_3, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 2)
        sizer_1.Add(grid_sizer_1, 10, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def ON_RESTART(self, event):  # wxGlade: MAIN.<event_handler>
        self.statusbar.SetStatusText(" ")
        self.run()

    def ON_QUIT(self, event):  # wxGlade: MAIN.<event_handler>
        os._exit(0)

    def ON_HIT(self, event):  # wxGlade: MAIN.<event_handler>
        self.player_draw()

    def ON_STAND(self, event):  # wxGlade: MAIN.<event_handler>
        self.button_1.Enable(False) # Disables the buttons if they had perviously been enabled
        self.button_2.Enable(False)
        self.dealer_draw()

    def ON_NOTHING(self,event):
        event.Skip() 

# end of class MAIN

class GameWindow(wx.App):
    def OnInit(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.frame = MAIN(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    
if __name__ == "__main__": # Hopefully you didn't try to call this script from another script because this will prevent it from doing anythig
    gettext.install("app")
    app = GameWindow(0)
    app.MainLoop()
