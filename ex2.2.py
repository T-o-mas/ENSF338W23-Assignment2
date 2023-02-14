from urllib.request import urlopen
import json
import timeit
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = urlopen(url)
data_json = json.loads(response.read())


x = []
y = []

for i in range(0, len(data_json)):
    x.append(i)
    arr = list(data_json[i])
    elapsed_time = timeit.timeit(lambda : func2(arr, 0, len(arr)-1), number = 100)
    y.append(elapsed_time)

plt.plot(x, y)
plt.xlabel('Arrays')
plt.ylabel('Time in Seconds')
plt.title('Timing Analysis for the QuickSort')
plt.show()


