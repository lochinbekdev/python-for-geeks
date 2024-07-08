
class MyAdd:
    def add(self,x,y):
        "This function add two numbers"
        if(not isinstance(x,(int,float))) | (not isinstance(y,(int,float))):
            raise TypeError('only number are allowed')
        return x+y