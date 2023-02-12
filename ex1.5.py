import timeit
import matplotlib.pyplot as plt


"""
Original code used to calculate the nth term of the 
fibonacci sequence
"""

def original_func(n):
    if n == 0 or n == 1:
        return n
    else: 
        return original_func(n-1) + original_func(n-2)


"""
Improved code using memoization to improve performance. 
"""
def func2(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = func2(n-1, memo) + func2(n-2, memo)
    return memo[n]

"""
Plotting
"""
ints = []
original = []
improved = []
memory = {}


for x in range(0,36):
    ints.append(x)

for n in range(0, 36):
    elapsed_time = timeit.timeit(lambda : func2(n, memory), number = 5)
    improved.append(elapsed_time)
    memory = {}

for n in range(0, 36):
    elapsed_time = timeit.timeit(lambda : original_func(n), number = 5)
    original.append(elapsed_time)

x = ints
y1 = original
y2 = improved

plt.figure(1)
plt.plot(x, y1, label = "Original")
plt.plot(x, y2, label = "Improved")
plt.xlabel('Integer')
plt.ylabel('Time in Seconds')
plt.title('Timing Analysis for Original and Improved Functions')
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x, y2)
plt.ylabel('Time in Seconds')
plt.title('Timing Analysis for the Improved Functions')
plt.legend()
plt.show()
