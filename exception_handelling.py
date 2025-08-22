import ast
class ExceptionHandelling:
    def __init__(self):
        pass

    def get_input_and_add_int(self,user_input):
    
        # user_input = input("Please enter your input:")
        sum = 0
        for num in user_input:
            try:
                num = int(num)
                sum = sum + num
            except Exception as err:
                print(err)
        print(f"Total is: ",sum)
    
    def like_count(self):
        reviews = [
            {
                'image':'abc.jpg',
                'like': 30,
                'comment':100
            },
            {
                'image':'xyz.jpg',
                'like': 200,
                'comment':100
            },
            {
                'image':'123.jpg',
                'like': 50,
                'comment':100
            }
        ]
        total = sum(review['like'] for review in reviews) 
        print(total)



obj = ExceptionHandelling()
obj.get_input_and_add_int([1,'a','b',5])
obj.like_count()