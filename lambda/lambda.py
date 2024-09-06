import math

result=lambda x:2*x

def rating(n):
    return lambda x:x**n

square=rating(2)
cube=rating(3)

#Map function take two argument first one is function second are list,obj and etc

numbers=list(range(0,11))

def calculate(x):
    return x + 2

result_calculate=list(map(calculate,numbers))
result_with_lambda=list(map(lambda x:x+2,numbers))

a = list(range(3,6))
b = list(range(7,10))

a_plus_b=list(map(lambda x,y:x+y,a,b))

print(a_plus_b)
