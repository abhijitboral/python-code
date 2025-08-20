class Decorator:
    def __init__(self,func):
        self.function  = func
        
    def __call__(self,a,b):
        result = self.function(a,b)
        return result ** 2

@Decorator
def add(num1,num2):
    return num1 + num2

print(add(1,2))

# Another example of class decorator to check the value whether the value is int or not. I the value is not int the print the error.
class Deco:
    def __init__(self,func):
        self.function = func
    def __call__(self, *args):
        try:
            if any(isinstance(i,str) for i in args):
                raise TypeError('Passed a sting as an argument')
            else:
                return self.function(*args)
        except Exception as err:
            return err


@Deco
def addition(*args):
    total = 0
    for val in args:
        total = total + val
    return total

print(addition(1,2,3)) # all values are intiger
print(addition(1,'2',3)) # Second value is sting
