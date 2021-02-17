"""
INSERTION SORT

Description:
Remembers an element, right-shifts everything greater than the given element once,
and places said element in the correct position. The array is thus split into two;
a sorted and an unsorted part (the invariant). This is done for all elements.

Worst case running time: Theta(n^2)
The iteration happens in Theta(n), and the shifting of elements in Theta(n).
"""

import numpy as np

A = np.random.randint(0, 10, size=5)
print("Unsorted: ", A)

for i in range(1, len(A)): # Iterate over all elements but first
	key = A[i] # Remember

	j = i - 1
	while j >= 0 and A[j] > key: # Right-shift greater elements of sorted part
		A[j+1] = A[j]
		j -= 1

	A[j+1] = key # Place

print("Sorted: ", A)