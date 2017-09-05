# TopN

Write a program, topN, that given an arbitrarily large file and a number, N, containing individual numbers on each line (e.g. 200Gb file), will output the largest N numbers, highest first. Tell me about the run time/space complexity of it, and whether you think there's room for improvement in your approach.

## Improvements

Quicksort is intended to have a much lower average runtime, however after implementing a heapsort, the built-in python heapq.nlargest, and a quicksort; the heapq.nlargest has the lowest average runtime.
