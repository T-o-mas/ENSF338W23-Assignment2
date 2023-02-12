
"""
Code using memoization to improve performance. Calculates the 
nth term in the fibonacci sequence. 
"""

def func(n, memo=[]):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = func(n-1, memo) + func(n-2, memo)
    return memo[n]

