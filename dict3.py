#Given a date, (Just month name and day), status of the year, display the day number
daynum=0
month = {'Jan':31, 'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31, 'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
mon = input("Enter the month name(in three letter format):").capitalize()
day=int(input('Enter the day of the month'))
status = input("Type L if it is a leap year and N if it is not a leap year").upper()
if status == "L":
    month["Feb"]=29

if mon in month:
    for m in month:
        if m  != mon:
            daynum += month[m]
    
        else: 
            daynum += day    
            break
else:
    print('Invalid choice')
 
print(daynum)

    