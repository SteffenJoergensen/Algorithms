import numpy as np
import math

A = np.array([2, 3, 10, 8, 1, 14, 13, 5, 7, 6, 3, 16, 11, 9, 1, 4, 13, 5, 7, 16, 1, 4, 13, 5])
print(A)

def insertion_sort(A):
    for i in range(1, len(A)):
    	key = A[i]

    	j = i - 1
    	while j >= 0 and A[j] > key:
    		A[j+1] = A[j]
    		j -= 1

    	A[j+1] = key

def partition(A, high):
    pivot = A[high]

    i = -1
    for j in range(0, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]

    return i + 1

def heapify(A, i):
    left = i * 2
    right = i * 2 + 1
    largest = i

    if len(A) > left and A[left] > A[largest]:
        largest = left
    if len(A) > right and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, largest)

def heap_sort(A):
    i = len(A) // 2
    for i in range(i, -1, -1):
        heapify(A, i)

def introsort(A, depth):
    if len(A) <= 16:
        insertion_sort(A)
    elif depth == 0:
        heap_sort(A)
    else:
        index = partition(A, len(A) - 1)

        introsort(A[:index-1], depth - 1)
        introsort(A[index+1:], depth - 1)

depth = 2 * math.floor(math.log(len(A)))
introsort(A, depth)
print(A)