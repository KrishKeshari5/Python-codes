scores = [110, 45, 97, 72, 89, 34, 91, 67, 55]
scores = [x for x in scores if x >= 60]
scores =  [min(x+5,100) for x in scores ]
print(scores)
