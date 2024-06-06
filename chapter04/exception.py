#try:
    #a series of statement
#except: 
    #statement to be exceuted
    
    
try:
    # print(x)
    x=5
    y=2
    z = x / y
    print(x + y)
except NameError as e:
    print(e)
except ZeroDivisionError:
    print("Devision by 0 is not allowed")
except Exception as e:
    print("An error occured")
    print(e)
else:
    "Hello world"
finally:
    "End process" 