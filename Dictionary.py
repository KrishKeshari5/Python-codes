#Repeatedly ask the user to enter a team name and how many games the team has won and how many they lost. 
# Store this information in a dictionary where the keys are the team names and the values are lists of the form [wins, losses].
#(a) Using the dictionary created above, allow the user to enter a team name and print out the team's winning percentage.
#(b) Using the dictionary, create a list whose entries are the number of wins of each team.
#(c) Using the dictionary, create a list of all those teams that have winning records.

dict={}

ans = 0
while ans == 0:
    name=input('Enter the team name ')
    Win= int(input('How many wins '))
    loss= int(input('How many losses '))
    dict.update({name:[Win,loss]})
    print(dict)
    ans=int(input('Type 0 to continue'))

wpn=input('Which teams winning percentage would you like to see')
if wpn in dict:
    Win = dict[wpn][0]
    loss = dict[wpn][1]

    wp= Win / (Win+loss)*100
    print (wp)