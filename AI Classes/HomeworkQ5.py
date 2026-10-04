#numbers = [12, 5, 18, 21, 7, 30, 14, 9]
#Even = [x**2 for x in numbers if x % 2 == 0 and x > 10 ]
#print(Even)
numbers = [12, 5, 18, 21, 7, 30, 14, 9]

even = filter(lambda x: x>10 and x%2==0, numbers)
f = list(map(lambda x: x*x, even))
print(f)