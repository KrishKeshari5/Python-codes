book = input('Say the score here: ').lower().split()
ball = 0
wicket=0
runs=0
over=0
for i in book:
    if wicket == 10 or ball == 100:
        print('game over')
        print(runs)
        break

    if i == 'nb':
        runs+=1
    
    elif i == 'w':
        wicket+=1
        ball+=1

    elif int(i) < 7:
        runs+=int(i)
        ball+=1

    over=ball/10
print(over)




