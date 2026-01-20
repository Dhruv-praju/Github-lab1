def add(x,y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers")
    
    return x + y

def subract(x,y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int,float))):
        raise ValueError("Both inputs must be numbers")
    
    return x-y

def multiply(x,y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int,float))):
        raise ValueError("Both inputs must be numbers")
    
    return x*y

def add_all(x,y,z):
    return x+y+z