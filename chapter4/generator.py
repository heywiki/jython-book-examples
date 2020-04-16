#Generator Functions, Listing 4-24,25
def g():
    print("before yield point 1")
    # The generator will return a value once it encounters the yield statement
    yield 1
    print("after 1, before 2")
    yield 2
    yield 3

'''
if __name__ == "__main__":
    # Call the function to create the generator
    x = g()
    # Call next() to get the value from the yield
    print(x.next())
    print(x.next())
    print(x.next())
    print(x.next()) #will generate error
'''
