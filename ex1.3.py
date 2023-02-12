
"""
Code using memoization to improve performance. Calculates the 
nth term in the fibonacci sequence. 
"""

def func2(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = func2(n-1, memo) + func2(n-2, memo)
    return memo[n]



