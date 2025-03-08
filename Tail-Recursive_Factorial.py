
# Exercise: The Tail-Recursive Factorial (Tail Recursion)
# Factorial calculation is commonly done using direct recursion, 
# but it can be optimized using tail recursion to avoid stack overflow.

# Tasks:
#   Implement a tail-recursive factorial function.
#   Compare it with a non-tail-recursive version.
#   Analyze the complexity and discuss why tail recursion is more memory-efficient.

# expected output:
#   tail_rec_factorial(5) = 120



def tail_rec_factorial(n):
    if n == 0 or n == 1: 
        return 1         # stop condition
    else:
        return n * tail_rec_factorial(n-1)  # recursive call for the next number
#   Time Complexity: O(N)
#   Space Complexity: O(N) 


def head_rec_factorial(n):
    if n > 1:           # stop condition
        return n * head_rec_factorial(n-1)  # recursive call for the next number
    return 1
#   Time Complexity: O(N) 
#   Space Complexity: O(N) 


def factorial(n):
    sum = 1 # initialize the sum
    while n > 1:  # loop until n is 1
        sum *= n  # multiply the sum by n
        n -= 1    # decrement n
    return sum
#   Time Complexity: O(N) 
#   Space Complexity: O(1) 


# test the functions
print(tail_rec_factorial(5))
print(head_rec_factorial(4))
print(factorial(5))
