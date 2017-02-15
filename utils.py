# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016


def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    try:
        if type(n) != int or n < 0:
            raise ValueError
        i = n
        result = 1
        while i > 0:
            result = result * n
            i -= 1
        return result

    except ValueError:
        print("n is not valid")
    
        

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + c = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """

    try:
        delta = b**2-4*a*c

        if delta > 0:
            result1 = (-b + delta**(1/2))/(2*a)
            result2 = (-b - delta**(1/2))/(2*a)
            answer = (result1, result2)
            return answer
        
        elif (delta == 0):
            result = (-b + delta**(1/2))/(2*a)
            answer = result,
            return answer
        
        else:
            return ()

    except:
        print("An error has occured")

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    h = float(upper - lower)/1000
    s = 0
    x = lower
    s += eval(function)/2
    for i in range(1, 1000):
        x = lower + i*h
        s+= eval(function)

    x = upper
    s += eval(function)/2

    return s * h

if __name__ == '__main__':
    print(fact(-4))
    print(roots(1, 4, 4))
    print(integrate('x ** 2 - 1', -1, 1))
