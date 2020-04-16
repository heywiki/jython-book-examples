def sales_tax(func):
    ''' Applies a sales tax to a given bill calculator '''
    def calc_tax(*args, **kwargs):
        f = func(*args, **kwargs)
        tax = f * .18
        print("Total before tax: $ %.2f" % (f))
        print("Tax Amount: $ %.2f" % (tax))
        print("Total bill: $ %.2f" % (f + tax))
    return calc_tax

@sales_tax
def calc_bill(amounts):
    ''' Takes a sequence of amounts and returns sum '''
    return sum(amounts)

amounts = [12.95,14.57,9.96]
print(sum(amounts)) #result of calc_bill() without decorator
print(calc_bill(amounts)) #once decorated does no longer return sum?
