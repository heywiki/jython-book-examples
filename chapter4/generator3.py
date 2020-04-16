#Listing 4-27
#https://github.com/jython/book/blob/master/DefiningFunctionsandUsingBuilt-Ins.rst
def step_return(factor, stop):
    step = factor
    start = 0
    if factor >= stop:
        return
    while start <= stop:
        yield start
        start += step

for x in step_return(1,10):
    print x
