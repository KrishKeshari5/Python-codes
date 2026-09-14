phonenumbers={}

while True :
    x = input('Enter a name')
    z=input('Enter your phone number')
    phonenumbers[x]=z
    y=int(input('Enter 5 to continue'))
    if y != 5 :
        break
print(phonenumbers)