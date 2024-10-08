import itertools

iter=itertools.count(10,2)
print(next(iter))
print(next(iter))



# letters={'A','B','C'}
# for letter in itertools.cycle(letters):
#     # print(letter)

for x in itertools.repeat('Python',times=5):
    print(x)

