class Books:
    def __init__(self,pages):
        self.pages = pages
    
    def __add__(self,other): # take two object as a perameter for operater overloading __add__(b1,b2)
        total = self.pages + other.pages
        # return total # If we have only two objects as a parameter then we can return the total variable directly.
        return Books(total) # return the object for addition of more than two or 'n' numbers objects.

    def __gt__(self,other): # take two object as a perameter for operater overloading __add__(b1,b2)
            return Books(self.pages > other.pages)
    
    def __str__(self): # for print the output. As, for print python always use __str__ mmethod and it's returned string so we need to typecast in string
        return str(self.pages)

b1 = Books(100)
b2 = Books(100)
b3 = Books(400)

print(f"Total number of pages are: {b1+b2+b3}")
print(f"b1 has more pages than b2? {b1>b2}")
print(f"b3 has more pages than b2? {b3>b2}")