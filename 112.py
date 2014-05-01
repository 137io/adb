""" Euler 112
->Sample Output:
1587000
5.39340400696
[Finished in 5.4s]
-> Why this problem:
Seemed like a good start.
-> A description of the process you followed in solving the problem:
This was easy - OK. Most of my time was spent on figuring out the pattern but then I just brute forced my way in 
to submit for this test. Will revisit soon.
First iteration was typecasting number to a string and using built-in functions to manipulate parts.
Second thought - teration was to use a list (sort)
Third iteration, use simple mod and div functions and compare selective parts of the number with former and prior.
A simple optimization was to use the info given in problem statement.
-> Sources:
-> Time Spent:
~1 hour.
"""
import timeit

def checkBouncy(num):
    """
    Returns True if num if increase and decreasing.
    """

    decreasingOrder = False
    increasingOrder = False
 
    #grab last digit
    lastDigit = int(num % 10)
    #grab first as well
    num = num / 10
 
    while num > 0:
        #loop one by one until end and make a note of the difference.
        nextDigit = int(num % 10)
        num = num / 10
        if (nextDigit > lastDigit):
            decreasingOrder = True
        elif (nextDigit < lastDigit):
            increasingOrder = True
 
        lastDigit = nextDigit
    return decreasingOrder & increasingOrder



def leastBouncyAt99():
    """
    Main function - start at givenBouncy number in problem stat and brute through
    """
    #this is given in problem statement
    givenBouncy = 21780
    #this too
    count = givenBouncy*0.9
    bouncy=givenBouncy
    currentBouncy = 0
    while True:
        bouncy+=1
        if checkBouncy(bouncy):
            count += 1
            if count/bouncy==0.99:
               return bouncy


if __name__ == "__main__":
    start = timeit.default_timer()
    print leastBouncyAt99()
    stop = timeit.default_timer()
    print stop - start 
