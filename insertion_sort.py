"""
INSERTION SORT

Description:
Remembers an element, right-shifts everything greater than the given element once,
and places said element in the correct position. The array is thus split into two;
a sorted and an unsorted part. This is done for all elements.

Time complexity: O(n^2)
The iteration happens in O(n), and the shifting of elements in O(n) (worst case).
"""

import numpy as np

array = np.random.randint(0, 10, size=5)
print("Unsorted: ", array)

def insertion_sort():
	for i in range(1, len(array)): # Iterate over all elements but first
		current = array[i] # Remember

		j = i - 1
		while j >= 0 and array[j] > current: # Right-shift greater elements of sorted part
			array[j+1] = array[j]
			j -= 1

		array[j+1] = current # Place

insertion_sort()
print("Sorted: ", array)