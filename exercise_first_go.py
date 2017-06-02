'''
You can leave all the comments and passes in place. They are just there to
provide stubs for the test script to run.
'''

# 1: finish the function to return a string
def return_string():
    '''
    Your code
    '''
    return "Silly string"

# 2: Write a function that checks if numerator can be exactly divided by denominator
## Assume only positive integers will be passed into it

def divides_by(numerator, denominator):
    '''
    Your code
    '''
    if numerator % denominator == 0:
        print "Happy days"
    else:
        print "Try again"

# 3: Write a function that returns a LIST of EVEN numbers up till a user provided limit
# e.g:
# even_numbers(7)
# returns
# [0,2,4,6]

def even_numbers(limit):
    '''
    Your code
    '''

    numbers = [range(1,limit)]
    even_number = []
    rejects = []
    for x in numbers:
        c = x / 2
        if type(c) == "int":
            even_number.append(x)
        else:
            rejects.append(x)

    return even_number(limit)
    return rejects(limit)

even_numbers(7)
