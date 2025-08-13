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

# second example of filter function
str_input = 'abhijit'
vowels = ['a','e','i','o','u']
vowels_letters = filter(lambda letter:True if letter in vowels else False,str_input)
print("Vowels: ",list(vowels_letters))

# Filter the student name whos marks is getter than 50

student_data = {
    'sachin':100,
    'virat':51,
    'Rahul':55,
    'Pant':20,
    'jadeja':78,
    'aswin':49
}
def func(student):
    return student_data[student] >= 50
filtered_list = filter(func,student_data)
print('Marks getter than 50: ',list(filtered_list))

# Example of map function
list_data = [22,23,24,25,26,27,28]
map_obj = map(lambda num:num*2,list_data)
print(list(map_obj))
