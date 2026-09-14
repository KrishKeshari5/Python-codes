import random

a = random.randint(1, 6)
b = random.randint(1, 6)
c = a + b

print('You rolled a', a,'and a' ,b)
print("Your total is ", c)

if c == 7 or c == 11:
    print("You won")
elif c == 2 or c == 3 or c == 12:
    print("You lost")
else:
    print("The point is ", c)
    p=c

    while True:
        input("Press to go again ")

        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = a + b

        print("You rolled", a, "and", b, " so your total is", c)

        if c == p:
            print("You Win")
            break
        elif c == 7:
            print("You rolled a 7. You lose")
            break
        else:
            print("Rolling again")