#!~/.pyenv/shims/python2.7.13
# User specific shebang line. Change to your Python interpreter dir

# Attribution:
# Heapsort: http://stevehanov.ca/blog/index.php?id=122

# Heapsort documentation: https://docs.python.org/3.5/library/heapq.html#heapq.nlargest

import heapq
import random
import time

def createArray():
  array = range(10 * 1000 * 1000)
  random.shuffle(array)
  return array

# Worst case runtime = O(n)
# Best case runtime = O(1)
# Average runtime = O(n)
def linearSort(bigArray, k):
    return sorted(bigArray, reverse=True)[:k]

# Worst case runtime = O(n log n)
# Best case runtime = O(n log n)
# Average runtime = O(n log n)
def heapSort(bigArray, k):
    heap = []

    # Note: below is for illustration. It can be replaced by heapq.nlargest(k, bigArray)

    for item in bigArray:

        # If we have not yet found k items, or the current item is larger than
        # the smallest item on the heap,

        if len(heap) < k or item > heap[0]:

            # If the heap is full, remove the smallest element on the heap.

            if len(heap) == k: heapq.heappop(heap)

            # add the current element as the new smallest.
            heapq.heappush(heap, item)

    return heap

def main():

    N = 10

    start = time.time()
    bigArray = createArray()
    print "Creating array took %g s" % (time.time() - start)

    start = time.time()
    print linearSort(bigArray, N)
    print "Linear sort took %g s" % (time.time() - start)

    start = time.time()
    print heapSort(bigArray, N)
    print "Heapsort took %g s" % (time.time() - start)

    start = time.time()
    print heapq.nlargest(N, bigArray)
    print "Built-in heapq.nlargest took %g s" % (time.time() - start)

if __name__ == "__main__":
    main()
