

# Exercise: The Recursive Cashier (Direct Recursion)
#   A cashier needs to give change using the fewest number of coins.
#   Given an amount N and a set of coin denominations {1, 5, 10, 25, 50, 100}, 
#   write a recursive function to compute the minimum number of coins needed.
#
# Tasks:
#   1- Write a recursive function minCoins(N, coins) that finds the minimum number of coins.
#   2- Analyze its complexity and explain why recursion may not be the best approach.
#   3- Optimize it using memoization.
#
# Expected Output:
#   minCoins(47, [1, 5, , 10, 25]) 



#   WORK!!!

# iterative solution:
def minCoinsIterative(N, coins):
    s = 0                       # intialize the sum of coins to  zero
    index = len(coins) - 1      # loop the coins list in reverse
    while (N > 0):              # exit when N is 0 or less
        if (coins[index] > N):
            index -= 1          # if the largest element in coins is bigger than N will see the next
        else:
            N -= coins[index]   # esle we will substract the element form N and repeat
            s += 1
    return s
# complexity:
#   Time Complexity: O(N) in the worst case
#   Space Complexity: O(1) (constant)


# recursive solution:
def minCoins(N, coins):
    if (N == 0):                                    # return 0 when n = 0
        return 0
    if (coins[len(coins) - 1] > N):                 # if coins biggerst element in coins is bigger will see next one
        return minCoinsMemo(N, coins[:len(coins) - 1])
    else:
        N -= coins[len(coins) - 1]                  # remove the element from
        return 1 + minCoins(N, coins)               # return the function with the new N
# complexity:
#   Time Complexity: O(2^N) (exponential) in the worst case
#   Space Complexity: O(N) due to the recursive call stack


# Optimize the function using memoization (dynamic programming)
def minCoinsMemo(N, coins, memo={}):
    if N == 0:
        return 0  # Base case: no coins needed
    if N < 0:
        return float('inf')  # Invalid case (can't make negative amounts)
    if N in memo:
        return memo[N]  # Return already computed result

    min_count = float('inf')
    for coin in coins:  # Try every coin
        res = minCoinsMemo(N - coin, coins, memo)
        if res != float('inf'):
            min_count = min(min_count, 1 + res)

    memo[N] = min_count  # Store result in memo
    return min_count if min_count != float('inf') else -1  # Return -1 if no solution exists
# complexity:
#   Time Complexity: O(N * M) where N is the amount and M is the number of coins
#   Space Complexity: O(N) due to the memoization array 



# test the function
coins = [1, 5, 10, 25]

print('test the itrative function')
print(minCoinsIterative(47, coins))

print('test the recursive function' )
print(minCoinsMemo(47, coins))




