#Listing 4-39,40
def tip_amount(tip_pct):
    def calc_tip_wrapper(func):
        def calc_tip_impl(*args, **kwargs):
            f = func(*args, **kwargs)
            print "Total bill before tip: $ %.2f" % (f)
            print "Tip amount: $ %.2f" % (f * tip_pct)
            print "Total with tip: $ %.2f" % (f + (f * tip_pct))
        return calc_tip_impl
    return calc_tip_wrapper

@tip_amount(.18)
def calc_bill(amounts):
    ''' Takes a sequence of amounts and returns sum '''
    return sum(amounts)

amounts = [12.95,14.57,9.96]
print(sum(amounts)) #result of calc_bill() without decorator
print(calc_bill(amounts)) #once decorated does no longer return sum?
