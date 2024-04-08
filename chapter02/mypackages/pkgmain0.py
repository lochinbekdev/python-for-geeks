import masifutil.mycalculator as calc
import masifutil.myrandom as rand
import masifutil.advcalc.advcalculator as acalc


def my_main():
    """ This is a main function which generates two randowm \ numbers and thme apply calculator functions on them """
    x = rand.random_2d()
    y = rand.random_1d()

    sum = calc.add(x, y)
    diff = calc.subtract(x, y)
    sroot = acalc.sqrt(x)
    log10x = acalc.log(x)
    log2x = acalc.ln(x)

    print("x= {},y={}".format(x, y))
    print("sum is {}".format(sum))
    print("diff id {}".format(diff))
    print("square is {}".format(sroot))
    print("log base of 10 is {}".format(log10x))
    print("log base of 2 is {}".format(log2x))


if __name__ == "__main__":
    my_main()
