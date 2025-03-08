# Exercise: Pascal’s Triangle (Nested Recursion)
# Pascal’s Triangle is a triangular array of binomial coefficients.

# Tasks:
#   Write a nested recursive function pascal(n, k) to compute Pascal’s Triangle.
#   Analyze the complexity and suggest an iterative approach.
#   Print Pascal’s Triangle up to n = 5.

# expected output:
#   pascal(4)
#   1
#   1 1
#   1 2 1
#   1 3 3 1
#   1 4 6 4 1


def pascal_iterative(n):
    count = 0
    while count <= n:
        print(11 ** count)
        count += 1
#   Time Complexity: O(N)
#   Space Complexity: O(1)


def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)
#   Time Complexity: O(2^n)
#   Space Complexity: O(N)


def pascal2(n):
    if n == 0:
        print(1)
    else:
        pascal2(n - 1)
        print(11**n)
#   Time Complexity: O(N)
#   Space Complexity: O(N)


# test the functions
pascal_iterative(5)
pascal(4, 2)
pascal2(3)














