def add(self,x,y):
    """This function add two numbers"""
    if(not isinstance(x,(int,float))) | (not isinstance(y,(int,float))):
        raise TypeError("Only numbers are allowed")
    return x + y 

