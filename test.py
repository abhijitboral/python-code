import sys
import copy


# Type of arguments:
# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable names arguments
# 5. Variable Length Positional Arguments (*args)
# 6. Variable Length Keyword Arguments (**kwargs)
# 7. Fast class objects 

# print("hello world")

# def add(a, b):
#     return a + b

# get the age type and print a message based on the age
# import types

# while True:
#     userAge = input("Enter your age: ")
#     userAge = int(userAge) if userAge.isdigit() else sys.exit("Invalid input, please enter a number.")
#     if len(str(userAge)) > 3:
#         print("Please enter a valid age.")
#         sys.exit()
#     if userAge < 13:
#         print("You are a child.")
#     elif userAge < 20:
#         print("You are a teenager.")
#     else:
#         print("You are an adult.")


# Grade Calculatter 

# marks = input("Enter your marks: ")
# marks = int(marks) if marks.isdigit() else exit("Invalid input, please enter a number.")
# grade = "You have failed." if marks < 60 else "You have passed." if marks < 80 else "You have excelled."
# print(grade)
# if len(str(marks)) > 3:
#     print("Please enter a valid marks.")
#     exit()
# if marks < 60:
#     print("You have failed.")
# elif marks < 80:
#     print("You have passed.")
# else:
#     print("You have excelled.")




str = "Hello, World!"
rev_str = ""
for char in str:
    rev_str = char + rev_str

print("Reversed string:", rev_str)

# shallow copy example
list = [1, 2, 3, 4, 5]
new_list = copy.copy(list)
new_list.append(6)
print("Original list:", list)
print("New list:", new_list)

# deep copy example
dict = {"name": "Alice", "age": 30,"address":{"street": "123 Main St", "city": "Los Angeles"}}
new_dict = copy.deepcopy(dict)
new_dict["address"]["city"] = "New York"
new_dict["address"]["pin"] = 123
print("Original dict:", dict)
print("New dict:", new_dict)


# List Comprehension Example
num = [1,2,3,4,5,6]
squear_val = [val ** 2 for val in num]
print(squear_val)

#List Comprehension Example with if condition
num_lists = [1,2,3,4,5,6,7,8,10]
even_num = [num_list ** 2 for num_list in num_lists if num_list %2 == 0]
print(even_num)

#List Comprehension Example with Multiple if condition
num_lists2 = [1,2,3,4,5,6,7,8,10]
even_num2 = [num_list ** 2 for num_list in num_lists if num_list %2 == 0 if num_list %3 == 0]
print(even_num2)

# List Comprehension Example with If Else If Else
new_nums = [1,2,3,4,5,6,7,8,9,10]

# if new_nums is even then get the squre else if get the qube else print hi.
filter_nums = [new_num**2 if new_num%2==0 else new_num **3 if new_num%3 == 0 else "hi" for new_num in new_nums]
print(filter_nums)

# Example of lambda function

myprint = lambda value='',option=0 :print(value) if option<1 else (print(value) ,exit())
myprint('test',1)


def myFun(fun):
    print(fun)
    # def fun(a,b):
    #     return sum(a,b)
    # return fun


myFun('add')
# demo = myFun('add')
# print(f"hello ",{demo(10,5)})
