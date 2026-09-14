def a(b):
    while b > 1:
        print(b)          
        if b % 2 == 0:
            b = b // 2
        else:
            b = 3 * b + 1
            
b = int(input("Enter a number"))
a(b)





