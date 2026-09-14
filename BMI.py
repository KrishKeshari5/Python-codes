age = int(input('What is you age'))

if age > 18:
    height=float(input('What is your height(m)'))
    weight=float(input('What is your weight(kg)'))

    BMI = weight / (height)**2

    if BMI < 18.5:
        print ('You are underweight')
    elif BMI >= 18.5 and BMI < 25:
        print('You are in the normal weight range')
    elif BMI >= 25 and BMI <= 29.9  :
        print('You are overweight')
    else:
        print('You are obese')

    
else:
    print('You are not elligible for this test')