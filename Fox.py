a = input('Type 6 o and 1 f ')
b = 0 

for i in a:
    if i == 'o':
        b += 1
    elif i == 'f':
        b += 1
        break

print(b)
