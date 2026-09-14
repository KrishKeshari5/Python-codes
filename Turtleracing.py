import turtle
import time
import random

WIDTH , HEIGHT = 600 , 600
COLOURS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_num_of_racers():
    racers = 0
    while True:
        racers =  input('Enter the number of racers(must be more than 2) ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('You need to enter a number')
            continue

        if racers >= 2:
            return racers
        else:
            print('Invalid number')

def race(colours):
    turtles = create_turtles(colours)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT//2 - 10:
                time.sleep(1)
                return colours[turtles.index(racer)]


def create_turtles(colours):
    turtles = []
    spacingx = WIDTH // (len(colours)+1)
    for i,colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 +20)
        racer.pendown()

        turtles.append(racer)

    return turtles



def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle racing')


racers = get_num_of_racers()
init_turtle()
random.shuffle(COLOURS)
colours = COLOURS[:racers]
winner =race(colours)
print(f'The {winner} turtle has won')

            