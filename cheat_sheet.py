def return_string():
    return "literally any string"

def divides_by(numerator, denominator):
    return not numerator % denominator

def even_numbers(limit):
    return [ i for i in range(limit + 1) if not i % 2 ]
