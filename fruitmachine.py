#Write a program to simulate a Fruit Machine that displays three symbols at random 
#from Cherry, Bell, Lemon, Orange, Star, Skull.
#The player starts with £1 credit, with each go costing 20p. 
#If the Fruit Machine “rolls” two of the same symbol, the user wins 50p. 
#The player wins £1 for three of the same and £5 for 3 Bells. 
#The player loses £1 if two skulls are rolled and all of his/her money if three skulls are rolled. 
#The player can choose to quit with the winnings after each roll or keep playing until there is no money left.
import random

symbols=['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
money = 100
stop='n'
while stop == 'n':
    print('You have', money ,'credits') 
    roll=input('would you like to roll (cost = 20 credits),')
    if roll== 'y':
        money-= 20
        outcome1=(random.choice(symbols))
        outcome2=(random.choice(symbols))
        outcome3=(random.choice(symbols))

        if outcome1 == outcome2 == outcome3:
            if outcome1 == 'Skull':
                money -= money
                
            elif outcome1 == 'Bell':
                money += 500
            else:
                money += 100

        elif outcome1 == outcome2 and outcome1 == 'Skull' or outcome1 == outcome3 and outcome1 == 'Skull' or outcome2 == outcome3 and outcome2 == 'Skull':
            money -= 100
            
        elif outcome1 == outcome2  or outcome1 == outcome3  or outcome2 == outcome3 :
            money+= 50

        
    
        print('You rolled' + outcome1,  outcome2 , outcome3)
    else:
        break     

        

        
