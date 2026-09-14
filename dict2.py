#2.Create a month dictionary and store the month name along with the number of days. Ex:month={“Jan”:31,”Feb”:28……..}
#Get the name of the month from the user and print the no. of days in that month.

month = {'Jan':31, 'Feb':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'Oct':31,'Nov':30,'Dec':31}
print(month)
Mon=input('Enter a month:')
if Mon in month:
    print(month[Mon])

