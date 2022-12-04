# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:48:23 2020

@author: joshu

Blackjack 2nd attempt

"""

import random

deck=[]
cardslib={}
vallib={}
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
        

def blackjackgame():
    balance=input("What is your starting cash (enter a number): ")
    balance=int(balance)
    finalbalance=0
    
    while balance>0:
        play="a"
        while play not in ["Y","y","N","n"]:
            play=input("Would you like to play blackjack (Y/N): ")
            if play in ["Y","y"]:
                stake=input("Your balance is {}, what is your stake: ".format(balance))
                stake=int(stake)
                if stake<=balance:
                    balance=balance-stake
                    [playertotal,deck]=blackjackround()
                    multiplier=bankerplay(playertotal,deck)
                    balance=balance + (multiplier * stake)
                else:
                    if stake>balance:
                        play="a"
            
            else:
                #Need to change to a proper exit sequence at some point
                print("You leave the casino with {}".format(balance))
                finalbalance=balance
                balance=0
    
    if finalbalance<=0:
        print("You have run out of funds!")
                
def handshow(hand):
    output="Your hand is: "
    handcard=[]
    for i in list(range(0,len(hand))):
        handcard.append(cardslib[hand[i]])
        if i < len(hand)-1:
            output=output + handcard[i] + ", "
        else:
            output=output+handcard[i]
    return(output)

def bankerhandshow(hand):
    output="Banker's hand is: "
    handcard=[]
    for i in list(range(0,len(hand))):
        handcard.append(cardslib[hand[i]])
        if i < len(hand)-1:
            output=output + handcard[i] + ", "
        else:
            output=output+handcard[i]
    return(output)
                
def blackjackround():
    deck=[]
    for i in list(range(1,53)):
        deck.append(i)
    
    hand=[]
    hand.append(random.choice(deck))
    deck.remove(hand[0])
    hand.append(random.choice(deck))
    deck.remove(hand[1])
    print(handshow(hand))
    
    handindex=1
    twist="a"
    while twist not in ["Y","y","N","n"]:
        twist=input("Do you want another card? (Y/N): ")
        if twist in ["Y","y"]:
            hand.append(random.choice(deck))
            handindex=handindex+1
            deck.remove(hand[handindex])
            print(handshow(hand))
            twist="a"
            total=calculatevalue(hand)
            print("Your total is: {}".format(total))
            if total>21:
                print("You have gone bust")
                break
        if twist in ["N","n"]:
            print(handshow(hand))
            total=calculatevalue(hand)
            print("Your total is: {}".format(total))
    playertotal=total
    return [playertotal,deck]
            
def calculatevalue(hand):
    total=0
    aces=0
    for i in list(range(0,len(hand))):
        total=total+vallib[hand[i]]
        if hand[i]%13==1:
            aces=aces+1
    print(aces)
    for i in list(range(0,aces)):
        if total>21:
            total=total-10
    return(total)
        
def bankerplay(playertotal,deck):
    
    hand=[]
    hand.append(random.choice(deck))
    deck.remove(hand[0])
    hand.append(random.choice(deck))
    deck.remove(hand[1])
    print(bankerhandshow(hand))
    
    total=calculatevalue(hand)
    print(bankerhandshow(hand))
    print("Bankers total is: {}".format(total))
    print("Your total is: {}".format(playertotal))
    while total<=17:
        hand.append(random.choice(deck))
        total=calculatevalue(hand)
        print(bankerhandshow(hand))
        print("Bankers total is: {}".format(total))
        print("Your total is: {}".format(playertotal))
    
    
    if total<=21 and total>playertotal:
        print("Banker win")
        multiplier=0
    elif total<=21 and total<playertotal:
        if playertotal==21:
            print("Blackjack")
            multiplier=3
        elif playertotal>21:
            print("Banker win")
            multiplier=0
        else:
            print("Player win")
            multiplier=2
    elif total>21 and playertotal>21:
        print("Both lose")
        multiplier=0
    elif total>21 and playertotal<=21:
        if playertotal==21:
            print("Blackjack")
            multiplier=3
        else:
            print("Player win")
            multiplier=2
    #elif total>21 and playertotal==total:
    #    print("Both lose")
    #    multiplier=0
    elif total<=21 and playertotal==total:
        print("Draw")
        multiplier=1
    return (multiplier)

blackjackgame()