import math

print('i will solve the equation ax^2+bx+c=0')

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

d = b **2-4*a*c

if d < 0:
    print('The equation has no real solution')
elif d == 0: 
    x = (-b)/(2*a)
    print('this equation has one solution: ',x)

else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(max(x1, x2), 'This equation ha two solutions: ',x1, 'or', x2)
def getX(x1, x2):
    if(x1 > x2):
        print('X1')
    else:
        print('results')
                
