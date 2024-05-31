from iterator2 import Week

if (__name__ == "__main__"):
    wk = Week()
    iter1 = iter(wk)
    iter2 = iter(wk)

    print(iter1.__next__())
    print(iter2.__next__())
    print(next(iter1))
    print(next(iter2))