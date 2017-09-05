#!~/.pyenv/shims/python2.7.13
# User specific shebang line. Change to your Python interpreter dir

# Attribution:
# Quicksort: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python

# Heapsort documentation: https://docs.python.org/3.5/library/heapq.html#heapq.nlargest

import heapq
import random
import time

def createArray():
  array = range(10 * 1000 * 1000)
  random.shuffle(array)
  return array

# Worst case runtime = O(n^2)
# Best case runtime = O(n log n)
# Average runtime = O(n log n)
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def main():

    N = 10

    start = time.time()
    bigArray = createArray()
    print "Creating array took %g s" % (time.time() - start)

    start = time.time()
    print sorted(quickSort(bigArray), reverse=True)[:N]
    print "Quicksort took %g s" % (time.time() - start)

if __name__ == "__main__":
    main()
