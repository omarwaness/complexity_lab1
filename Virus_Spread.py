

# Exercise: Virus Spread (Head Recursion) Problem:
#   A computer virus spreads exponentially every hour. 
#   If a system starts with P infected computers, 
#   and each infected computer infects two new computers every hour, 
#   how many infected computers will there be after N hours?
# 
# Tasks:
#   Write a head-recursive function virusSpread(N, P).
#   Determine the time complexity.
#   Modify the recursion to an iterative approach and compare efficiency.
#
# Expected Output:
#   virusSpread(3, 1)   ---> 15


# work!!!

# iterative solution
def virusSpreadIterative(N, P):
    while N > 0:        # stop consdition is hour 0
        P = P*2 + 1     # every loop the number doubles + one
        N -= 1          # decreacse hours
    return P
# Complexity:
#   Time Complexity: O(N)
#   Space Complexity: O(1)


# recursive solution
def virusSpread(N, P):
    if N == 0:                          # stop consdition is hour 0
        return 1
    return P*2 + virusSpread(N-1, P*2)  # decreacse hours and new population
# Complexity:
#   Time Complexity: O(N)
#   Space Complexity: O(N)


# test the functions
print('recursice function')
print(virusSpread(3, 1))

print('recuriterativesice functin')
print(virusSpreadIterative(3, 1))