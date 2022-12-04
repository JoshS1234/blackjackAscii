# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:07:49 2020

@author: Mr Spence
"""
import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return(self.rank + " of " + self.suit)

class Deck():
    
    def __init__(self):
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.deck)
        

    
    def __str__(self):
        a=""
        for i in list(range(0,len(self.deck))):
            a=a+self.deck[i].rank + " of " + self.deck[i].suit + ", "
        return a
    
class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    def addcard(self,pack):
        self.cards.append(pack.deck[0])
        pack.deck.pop(0)
        
    def initialdeal(self,pack):
        self.cards.append(pack.deck[0])
        pack.deck.pop(0)
        self.cards.append(pack.deck[0])
        pack.deck.pop(0)
        
    def showhand(self):
        for i in list(range(0,len(self.cards))):
            print(self.cards[i])
    
    def show1card(self):
        print(self.cards[0])
        
    def handvalue(self):
        self.value=0
        aces=0
        for i in list(range(0,len(self.cards))):
            self.value=self.value+values[self.cards[i].rank]
            if self.cards[i].rank=="Ace":
                aces=aces+1
        for i in list(range(0,aces)):
            if self.value>21:
                self.value=self.value-10
        return self.value
        
    

    
    def __str__(self):
        a=self.cards[0].rank + " of " + self.cards[0].suit
        for i in list(range(1,len(self.cards))):
            a=a + ", " + self.cards[i].rank + " of " + self.cards[i].suit
        
        return a
        

    
class Chips():   
    def __init__(self):
        a=False
        while a == False:
            try:
                self.total = input("How many chips do you have?: ")  # This can be set to a default value or supplied by a user input
                self.total = float(self.total)
                if self.total>0:
                    a=True
            except:
                print("Invalid chips")
        self.bet = 0
        
    def win_bet(self):
        self.total=self.total+(self.bet)
    
    def lose_bet(self):
        self.total=self.total-self.bet
        
        
def take_bet(chips):
    print("you have " + str(chips.total) + " chips")
    bet="a"
    while bet=="a":
        try:
            bet=input("How much would you like to bet?: ")
            bet=float(bet)
            if bet>chips.total:
                bet="a"            
        except:
            print("invalid bet")
            bet="a"
    #Maybe check this
    chips.bet=bet
        
def hit(deck,hand,bankerhand):
    twist="a"
    if hand.handvalue()==21:
        print("-------------------------------")
        print("")
        print("Banker's show card is: ")
        bankerhand.show1card()
        print("")
        print("Your cards are: ")
        hand.showhand()
        print("Your total is: {}".format(hand.handvalue()))
            
    while hand.handvalue()<21:
        while twist not in ["Y","y","N","n"]:
            
            print("-------------------------------")
            print("")
            print("Banker's show card is: ")
            bankerhand.show1card()
            print("")
            print("Your cards are: ")
            hand.showhand()
            print("Your total is: {}".format(hand.handvalue()))
            
            
        
            twist=input("Would you like another card? (Y/N): ")
            if twist in ["Y","y"]:
                hand.addcard(deck)
                twist="a"
                print("Your total is: {}".format(hand.handvalue()))
                if hand.handvalue()>21:
                    print("")
                    print("Your cards are: ")
                    hand.showhand()
                    print("")
                    print("You have gone bust")
                    print("---------------------------------")
                    break
            if twist in ["N","n"]:
                print("Your total is: {}".format(hand.handvalue()))
                break
        break
    
def bankerplay(deck,hand,bankerhand):
    if hand.handvalue()>21:
        pass
    elif bankerhand.handvalue()<17:
            bankerhand.addcard(deck)
            
def checkoutcome(player,banker,chips):
    if player.handvalue()>21:
        chips.lose_bet()
        print("You lost {} chips".format(chips.bet))
    elif player.handvalue()<=21:
        if banker.handvalue()>21:
            chips.win_bet()
            print("You won {} chips".format(chips.bet))
        if banker.handvalue()<=21:
            if player.handvalue()>banker.handvalue():
                chips.win_bet()
                print("You won {} chips".format(chips.bet))
            elif player.handvalue()==banker.handvalue():
                print("This was a draw, you get your bet back")
            elif player.handvalue()<banker.handvalue():
                chips.lose_bet()
                print("You lost {} chips".format(chips.bet))
        
    


#a=Hand()
#b=Deck()
#b.shuffle()
#a.addcard(b)
#a.addcard(b)

#print(a)
#a.handvalue()
#print(a.value)


x=True
while x==True:
    
    print("You are playing Blackjack!")
    
    
    player_chips=Chips()
    
    pack=Deck()
    pack.shuffle()
    player=Hand()
    player.initialdeal(pack)
    banker=Hand()
    banker.initialdeal(pack)
    
    
    play="a"
    while play not in ["Y","y","N","n"]:
        play=input("Are you ready to play? (Y/N): ")
        if play in ["Y","y"]:
            #Start to play a round of blackjack
            take_bet(player_chips)
    
            hit(pack,player,banker)
            
            print("---------------")
            print("Banker's play")
            print("Banker's initial card value: {}".format(banker.handvalue()))
            banker.showhand()
            print(" ")
            
            bankerplay(pack, player, banker)
            print("Banker's final cards: ")
            banker.showhand()
            print("Banker's final card value: {}".format(banker.handvalue()))
            print(" ")
            
            checkoutcome(player, banker,player_chips)
            if player_chips.total<=0:
                print("You've gone bankrupt")
                break
            
            play="a"
            print("You have {} chips".format(player_chips.total))
            pack=Deck()
            pack.shuffle()
            player=Hand()
            player.initialdeal(pack)
            banker=Hand()
            banker.initialdeal(pack)    
        elif play in ["N","n"]:
            print("Okey doke")
            print("You leave the casino with {} chips".format(player_chips.total))
            break
        
        
    
    
    
    x=False