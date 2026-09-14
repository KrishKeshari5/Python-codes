###Create a number list and practice the following functions in it
#Adding an element, Adding multiple elements, Insert values, Remove values
#both by mentioning the value and by position(index)
#Count the no. of occurrence of a value and finding index
#Sort it, Reverse it
#Make use of copy function

numbers = [42, 7, 89, 13, 56, 24, 91]

numbers.append(60)

numbers.extend(73, 82, 97)

numbers.insert(2, 25)

numbers.remove(7)
numbers.pop(3)

numbers.count(20)
numbers.index(50)

numbers.sort()
numbers.reverse()

numbers.copy()

