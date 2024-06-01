def moveZero(nums:list) -> list:
    zeros=[]
    others=[]
    for item in nums:
        if item == 0:
            zeros.append(item)
        else:
            others.append(item)
    return others + zeros

numbers=[0,1,0,3,12]

bad_solution_result=moveZero(numbers)

        
        
        
def move_zero_best_practice(nums:list)->list:
    count = 0
    
    for i,num in enumerate(nums):
        if num == 0:
            count +=1
            continue
        
        nums[i],nums[i-count] = nums[i-count],nums[i]
        
    return nums

good_solutions=move_zero_best_practice(numbers)
print(good_solutions)
