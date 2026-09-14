student = {}
numt= int(input('Enter how many students there are'))
for i in range(numt):
    name = input('what is there name: ')
    mark = int(input('How many marks '))
    student.update({name: mark})
print(student)

