Weather = []
for i in range(7):
    a = int(input('Enter the weather in the morning'))
    b= int(input('Enter the weather in the afternoon '))
    c= int(input('Enter the weather in the evening '))
    W = [a,b,c]
    Weather.append(W)
print(Weather)

total=0
for j in range(7):
    total += Weather[i][0]
average = total/7
print (average)