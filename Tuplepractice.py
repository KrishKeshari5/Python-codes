patl=[]
rep=int(input('How many lab reports have you received'))
for i in range(rep):
    name=input('What is the name of the patient')
    t1 = int(input('What is your result for test 1'))
    t2 = int(input('What is your result for test 2'))
    t3 = int(input('What is your result for test 3'))
    t4 = int(input('What is your result for test 4'))
    t5 = int(input('What is your result for test 5'))

    val= (name,t1,t2,t3,t4,t5) 
    patl.append(val)
print(patl)
