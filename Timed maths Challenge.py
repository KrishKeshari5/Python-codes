import random
import time

Operator = ['+', '-', '*']
Min = 3
Max = 12
Total = 10


def generate_problem():
    left = random.randint(Min, Max)
    right = random.randint(Min, Max)
    operator = random.choice(Operator)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


w = 0
input('preess enter to start the game: ')

start = time.time()

for i in range(Total):
    expr, answer = generate_problem()
    while True:
        guess = input('Problem ' + str(i + 1) + ': ' + expr + ' = ')
        if guess == str(answer):
            break
        w += 1

end = time.time()
t = round(end - start, 2)

print('You finished in', t, 'seconds and got', w,'wrong' )
