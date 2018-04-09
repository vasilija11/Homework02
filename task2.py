"""
===================   TASK 2   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def gcd(a,b):

    if not isinstance(a,int) and not isinstance(b,int): # da li su unijeti brojevi cijeli brojevi
        return -1

    a_ = abs(a)
    b_ = abs(b)
    x = abs(a_-b_)

    if x == 0:
        return b_
    else:
        return gcd(x,min(a_,b_))

def main():

    print(gcd(-120, 24))

main()