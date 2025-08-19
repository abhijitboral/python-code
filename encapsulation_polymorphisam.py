
cart_items = [
    {
        'product_name': 'Mobile',
        'price': 12000,
    },
    {
        'product_name': 'TV',
        'price': 20000,
    },
    {
        'product_name': 'T-shirt',
        'price': 3000,
    },
]
class Cart:
    def __init__(self,items):
        self.__items = items #private variable
# Example of accessing private variable using method
    def cart_total(self):
        total = sum(item['price'] for item in self.__items)
        return total

# example of Over-riding Built in Functions. 
    def __len__(self):
        return len(self.__items)


cart_obj = Cart(cart_items)
# print(cart_obj.items) # can't access, because items is a private variable.
# print(cart_obj._Cart__items) # Using Name Mangling we can access the private variable
# print(f"The cart total is",cart_obj.cart_total())
# print(f"Total Items in cart is: ",len(cart_obj))
print(f"Total Items in cart is: {len(cart_obj)} and cart total is: {cart_obj.cart_total()}")