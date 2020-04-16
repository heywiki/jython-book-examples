#Listing 4-39
#Decorators enhances the action of the function that they decorate
#We have the ability to change the inner-working of the function without
#adjusting the original decorated function at all
def plus_five(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs) + 5
        return x
    return inner

@plus_five
def add_nums(num1, num2):
    return num1 + num2

print(add_nums(2,3))
print(add_nums(2,6))
