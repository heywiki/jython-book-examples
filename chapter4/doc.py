# This function is used in order to provide the square
# of any value which is passed in.  The result will be
# passed back to the calling code.
def square_val(value):
    return value * value

def tip_calc(value, pct):
    ''' This function is used as a tip calculator based on a percentage
       which is passed in as well as the value of the total amount.  In
       this function, the first parameter is to be the total amount of a
       bill for which we will calculate the tip based upon the second
       parameter as a percentage '''
    return value * (pct * .01)

print tip_calc(75,15)
print tip_calc.__doc__
