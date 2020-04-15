#see https://github.com/jython/book/issues/17
while x >= 0:
    if x == 0:
        print "x is now equal to zero!"
        break
    else:
        if x % 2 == 0:
            print x
    x = x – 1
