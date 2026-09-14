def isprime(a):
    for i in range(2,a-1) :
        b=a % i
        if b ==0:
            return False
       
    return True

a=int(input('Enter a number'))
answer = isprime(a)
print(answer)
        
