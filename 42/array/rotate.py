def rotate(numbers: list, key: int) -> list:
    last = [numbers.pop(-1)]
    step1= last + numbers 
    print(step1)


numbers= [1,2,3,4,5,6,7]
key=3

result=rotate(numbers,key)
# print(result)