#Listing 4-43
#A coroutine is a function that receives data and does something with it
def co_example(name):
    print 'Entering coroutine %s' % (name)
    my_text = []
    while True:
        txt = (yield)
        my_text.append(txt)
        print my_text

#the yield statement is the point where
#text is being entered by the user
ex = co_example("example 1")

#The next() must be called once to initialize the coroutine.
#Once this has been done, the function is ready to accept values.
#You can eliminate this with the @coroutine_next decorator, see Listing 4-46
ex.next()

#As you can see, we use the send() method
#to actually send data values into the coroutine
ex.send("test1")
ex.send("test2")
ex.send("test3")
