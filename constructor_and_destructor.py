import time
class Employee:
    def __init__(self,name,age): # Constructor 
        self.__name = name
        self.__age = age

    def show(self):
        print(f"The employee name is - {self.__name} and the age is - {self.__age}")

    def __del__(self): # Destructor
        print('Destructor is called')

e1 = Employee('Raju',23)
e1.show()
time.sleep(3) # after 3 sec the destructor will be call automatically