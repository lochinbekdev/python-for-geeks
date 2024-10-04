from collections import Counter

print(Counter('people'))


my_counter= Counter([1,2,1,2,3,4,1,3])

print(my_counter.most_common())
print(list(my_counter.elements()))


print(Counter({'A':2,'B':2,'C':2,'C':3}))
