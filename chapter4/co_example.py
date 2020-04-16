#Listing 4-46 Decorators in Coroutines
#@coroutine_next
def co_example(name):
    print('Entering coroutine %s' % (name))
    my_text = []
    while True:
        txt = (yield)
        my_text.append(txt)
        print(my_text)

ex2 = co_example("example2")
ex2.next()
ex2.send("one")
ex2.send("two")
ex2.close()
