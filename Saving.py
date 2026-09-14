#You want to save up for a new gadget that costs $300.You plan to save a little each week and want to keep trackof how long it will take to save enough money.
#Task: Write a program that keeps asking for your weeklysavings and stops when you have saved enough to buy the gadget.
a = 0
t = 0
count = 1

while a < 300:
    t = float(input(f'How much would you want to save in Week {count}? '))
    a += t
    count += 1

print('You have achieved your goal in', count - 1, 'weeks')

    





    