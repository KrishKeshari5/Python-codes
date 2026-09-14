#Get 2 strings of different length from the user, and print a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
#Examples 
#'Hello', 'hi' → 'hiHellohi’
#'aaa', 'b' → 'baaab'
a= input('Enter a word: ')
b= input('Enter another word: ')

if len(a) < len(b):
    print(a + b + a)
else:
    print(b + a + b)
    


