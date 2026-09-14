#Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times,
#  for G, it's pressed seven times, etc, etc. Write a program that takes a string (the message) and displays the total number of 
# times the button is pressed. 
#Examples 
#abde → 12 
#azy → 52 
#qudusayo → 123
total=0
alph=' abcdefghijklmonpqrstuvwxyz'
text=input('Enter a text: ')

for a in text:
    total+= alph.index(a)
print(total)