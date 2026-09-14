#A user is trying to log in to their account. They have to enter the correct password. If they enter the wrong password, they are asked to try again. 
#Task: Write a program that keeps asking for a password until the correct one is entered (You can initialize any string as a password in your program. Example password can be like pass@123)
password= input('Enter a password ')

while password != 'password':
    password= input('Try again ')

print('Well done you entered the correct password')


