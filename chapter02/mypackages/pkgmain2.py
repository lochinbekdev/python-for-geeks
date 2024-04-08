import masifutil


def my_main():
    x = masifutil.random_2d()
    y = masifutil.random_1d()

    sum = masifutil.add(x, y)
    diff = masifutil.subtract(x, y)

    sroot = masifutil.sqrt(x)
    log10x = masifutil.log(x)
    log2x = masifutil.ln(x)

    print("x= {},y={}".format(x, y))
    print("sum is {}".format(sum))
    print("diff id {}".format(diff))
    print("square is {}".format(sroot))
    print("log base of 10 is {}".format(log10x))
    print("log base of 2 is {}".format(log2x))

if __name__ == "__main__":
    my_main()


