# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:18:54 2020

@author: joshu

Blackjack using class notation
"""

import random

deck=[]
cardslib={}
vallib={}
#Assigning values to all 52 cards and setting structure for the deck
for i in list(range(1,53)):
    deck.append(i)
    if i%13==0:
        cardslib[i]="K"
        vallib[i]=10
    elif i%13==1:
        cardslib[i]="A"
        vallib[i]=11
    elif i%13==2:
        cardslib[i]="2"
        vallib[i]=2
    elif i%13==3:
        cardslib[i]="3"
        vallib[i]=3
    elif i%13==4:
        cardslib[i]="4"
        vallib[i]=4
    elif i%13==5:
        cardslib[i]="5"
        vallib[i]=5
    elif i%13==6:
        cardslib[i]="6"
        vallib[i]=6
    elif i%13==7:
        cardslib[i]="7"
        vallib[i]=7
    elif i%13==8:
        cardslib[i]="8"
        vallib[i]=8
    elif i%13==9:
        cardslib[i]="9"
        vallib[i]=9
    elif i%13==10:
        cardslib[i]="10"
        vallib[i]=10
    elif i%13==11:
        cardslib[i]="J"
        vallib[i]=10
    elif i%13==12:
        cardslib[i]="Q"
        vallib[i]=10
        


class player():
    
    def __init__(self):
        #Setting initial balance
        balance="a"
        while type(balance)!=float:
            try:
                balance=input("What is your starting balance?: ")
                balance=float(balance)
            except:
                print("This is not a number")    
        self.balance=balance
        
        self.deck=[]
        for i in list(range(1,53)):
            self.deck.append(i)
        self.deck=deck
        self.playerhand=[]
        self.bankerhand=[]
        
    def reshuffle(self):
        self.deck=[]
        for i in list(range(1,53)):
            self.deck.append(i)
        self.deck=deck
        self.playerhand=[]
        self.bankerhand=[]
            
        
    def playerdeal(self):
        self.playerhand.append(random.choice(self.deck))
        self.deck.remove(self.playerhand[0])
        self.playerhand.append(random.choice(self.deck))
        self.deck.remove(self.playerhand[1])
    
    def bankerdeal(self):
        self.bankerhand.append(random.choice(self.deck))
        self.deck.remove(self.bankerhand[0])
        self.bankerhand.append(random.choice(self.deck))
        self.deck.remove(self.bankerhand[1])
    
    
    def printplayerhand(self):
        output="Your hand is: "
        handcard=[]
        for i in list(range(0,len(self.playerhand))):
            handcard.append(cardslib[self.playerhand[i]])
            if i < len(self.playerhand)-1:
                output=output + handcard[i] + ", "
            else:
                output=output+handcard[i]
        return output
    
    def printbankerinitialhand(self):
        output="Bankers hand is: "
        handcard=[]
        for i in list(range(0,1)):
            handcard.append(cardslib[self.bankerhand[i]])
            if i < len(self.bankerhand)-1:
                output=output + handcard[i] + ", "
            else:
                output=output+handcard[i]
        output=output+"?"
        return output
    
    def playerround(self):
        twist="a"
        handindex=len(self.playerhand)-1
        while twist not in ["Y","y","N","n"]:
            twist=input("Do you want another card? (Y/N): ")
            if twist in ["Y","y"]:
                self.playerhand.append(random.choice(self.deck))
                handindex=handindex+1
                self.deck.remove(self.playerhand[handindex])
        
    

        
        
a=player()
a.playerdeal()
a.bankerdeal()
a.printplayerhand()
a.printbankerinitialhand()
a.playerround()