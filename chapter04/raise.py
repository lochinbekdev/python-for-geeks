import math 

def sqrt(num):
    
    if not isinstance(num,(int,float)):
        raise TypeError("Only number are allowed")
    if num < 0:
        raise Exception("Negative number not supported")
    
    
    return math.sqrt(num)

if __name__ == "__main__":
    try:
        print(sqrt(4))
        print(sqrt("s"))
        print(sqrt(-9))
    except Exception as e:
        print(e)
    