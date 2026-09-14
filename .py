#You are tracking the number of steps you walk each day for a week. Your goal is to walk at least 10,000 steps daily. You want to know how many days you reached or exceeded this goal.
#Task: Write a program that records the steps for 7 days and tells you how many days you met your goal.
day = 0
for i in range(7):
    a = int(input('How many steps did you do today'))
    if a>= 10000:
        day+=1

            
print(day)