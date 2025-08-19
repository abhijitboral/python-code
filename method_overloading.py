class Addition:
    #this is concept of method overloading. But this code will not work because Python does't support method overloading like C++ or JAVA.
    def add(self,n1,n2):
        print(n1+n2)

    def add(self,n1,n2,n3):
        print(n1+n2+n3)

print("!! this is concept of method overloading. But this code will not work because Python does't support method overloading like C++ or JAVA. In python always execugte the last method. So, if we call add method with 3 perameters then it will work.")
obj = Addition()
# obj.add(10,20)
obj.add(10,20,30)

# to achive method over loading with below code or with if else condition
class Sumation:
    def add(self,*args):
        print(sum(args))

obj = Sumation()
obj.add(1,2,3,4)
obj.add(1,2,3,4,6,7,8)
