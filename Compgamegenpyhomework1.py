import random
t = random.randint(20, 30)
print('the starting number is', t)

while t > 20:
    player = int(input('Remove 1, 2 or 3: '))
    t -= player
    print(t+'left')

    if t == 0:
        print('You lose')
        
    c = random.randint(1, 3)
    print('Computer removes'+ c)
    t -= c
    print( t+'left')

    if t == 0:
        print('The winner is you')
        


