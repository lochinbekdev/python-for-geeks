#calcmian3.py with from and alias combined
from mycalculator import add as my_add
from mycalculator import subtract as my_subtract
from myrandom import random_1d, random_2d

def my_main():
    x = random_2d()  
    y = random_1d()

    sum = my_add(x,y)
    diff=my_subtract(x,y)

    print("x= {}, y = {}".format(x,y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))


if __name__ == "__main__":
    my_main()