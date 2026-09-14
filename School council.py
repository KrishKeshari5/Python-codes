y=0
n=0
while True:
    a = input('enter yes or no ')
    if a=='yes' or a=='Yes':
        y=y+1
    elif a=='no' or a=='No':
        n=n + 1
    elif a=='stop' or a=='Stop':
        break
    else:
        print('Not valid')

print('you got', y, 'yeses and ', n, 'nos')