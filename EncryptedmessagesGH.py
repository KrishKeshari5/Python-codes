alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3

message = input('Enter a word: ')
newmessage = ''

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newposition = (position + key) 
        newcharacter = alphabet[newposition]
        newmessage += newcharacter
else:
    print('Invalid choice')


