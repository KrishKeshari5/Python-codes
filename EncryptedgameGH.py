import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = random.randint(1, 25)

message = input('Enter a word: ')
newmessage = ''

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newposition = (position + key) % 26
        newcharacter = alphabet[newposition]
        newmessage += newcharacter
    else:
        print('Invalid choice')
        break

print('New word is',newmessage)


while True:
    gue = int(input("Guess the key (1-25): "))

    if gue == key:
        print('Correct! ')
        break
    elif gue < key:
        print('Too low')
    else:
        print('Too high.')

