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
# or using lambda function
filter_list_2 = filter(lambda student:True if student_data[student] >= 50 else False ,student_data)
print('Marks getter than 50: ',list(filter_list_2))

# Example of map function
list_data = [22,23,24,25,26,27,28]
map_obj = map(lambda num:num*2,list_data)
print(list(map_obj))

# second example of map function

first_list_vals = [10,20,30,40]
second_list_vals = [5,6,7,8]

def myfunc(first_list_val,second_list_vals):
    return first_list_val + second_list_vals
add_nums = list(map(myfunc,first_list_vals,second_list_vals))
print(add_nums)

# or using lambda 

lambda_add_nums = list(map(lambda first_list_val,second_list_vals:first_list_val + second_list_vals,first_list_vals,second_list_vals))
print('Map function with Lambda: ',lambda_add_nums)

# Example of reduce function to find the maxmimum number
import functools
num_lists = [10,20,30,40,50] 
max_num = functools.reduce(lambda a,b: a if a >= b else b,num_lists)
print('Reduce function with Lambda',max_num)

# Recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(f"Factorila number: ",factorial(5))

# Recursion using Lambda to get know a number is prime or not
check_prime = lambda nums,i : 'Prime' if i==1 else 'Not Prime' if nums%2==0 else check_prime(nums,i-1)
print(check_prime(11,10))


# Direct Recursion function to print n to 1 sequence .

def my_recu(n):
    
    if n==0:
        return
    else:
        print(n)
        my_recu(n-1)
my_recu(10)
# Direct Recursion function to print n to 1 sequence with Lambda.
recur_nums = lambda n: None if n == 0 else (print(n) or recur_nums(n - 1))
recur_nums(10)

# Febonacci series using Recursion
def febonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (febonacci(n-2) + febonacci(n-1)) 

num = 4
for i in range(1,num+1):
    print(F"Febonacci series: {febonacci(i)}")
# Febonacci series using Recursion unsing Lambda
fibo = lambda n: (
    0 if n == 0 else
    1 if n == 1 else
    fibo(n-1) + fibo(n-2)
)    
[print(fibo(i)) for i in range(10)]

# Febonacci series using loop
nums = 10 
febo = []
a, b = 0, 1
for _ in range(nums):
    febo.append(a)
    a, b = b, a + b

print(febo)
    
# Decorater
def decor(main_func):
    # return main_func()
    def inner():
        even_nums = main_func()
        # even_nums = even_nums ** 2
        squear_val = [val ** 2 for val in even_nums]
        return squear_val
    return inner

@decor
def main_func():
    even = []
    list_vals = [2,4,5,7,8,6,5,13,45,67]
    for num in list_vals:
        if num % 2 == 0:
            even.append(num)
    return even
        

print(main_func())