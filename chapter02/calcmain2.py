import mycalculator as calc
import myrandom as rand

def my_main():
    x = rand.random_2d()
    y = rand.random_1d()

    sum = calc.add(x,y)
    diff = calc.subtract(x,y)

    print("x = {}, y = {}".format(x,y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))

if __name__ == "__main__": 
    my_main()


