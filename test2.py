# from test import add

# result = add(4, 5)
# print(f"The result of adding is: {result}")


# Example of returing function from a function 
def myFun(fun):
    def fun(a,b):
        return a+b
    return fun

demo = myFun('add')
print(demo(10,5))


# Example of heigher order function
def func1(args):
    return args

def heigher_order_func(params):
    def params(func1_params):
        return "hi " + func1_params
    return params

hof = heigher_order_func('func1')
print(hof('Raju'))

# Example of filter function

list_data = [22,23,24,25,26,27,28]
filter_obj = filter(lambda num:True if num%2 == 0 else False,list_data)
print(list(filter_obj))
