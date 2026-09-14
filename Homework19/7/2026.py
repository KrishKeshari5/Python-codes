x = 0
y = 0

def coordinates(a):
    
    for i in a:
        if i == 'n':
            y += 1
        elif i == 's':
            y -= 1
        elif i == 'e':
            x += 1
        elif i == 'w':
            x -= 1

a = ['s', 'e', 'n', 'w', 's']
coordinates(a)
print(x,',',y)
