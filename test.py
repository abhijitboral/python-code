import sys

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

marks = input("Enter your marks: ")
marks = int(marks) if marks.isdigit() else exit("Invalid input, please enter a number.")
# if len(str(marks)) > 3:
#     print("Please enter a valid marks.")
#     exit()
# if marks < 60:
#     print("You have failed.")
# elif marks < 80:
#     print("You have passed.")
# else:
#     print("You have excelled.")


grade = "You have failed." if marks < 60 else "You have passed." if marks < 80 else "You have excelled."
print(grade)

str = "Hello, World!"
rev_str = ""
for char in str:
    rev_str = char + rev_str

print("Reversed string:", rev_str)