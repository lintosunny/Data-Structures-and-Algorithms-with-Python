# Quicksort is one of the fastest sorting algorithms.
# The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element,
# and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

def partition(array, low, high):
  """
  Partitions sub-array for quick sort.
  Receives a sub-array, moves values around, swaps the pivot element into the sub-array

  Args:
    array: The list representing the array to be partitioned.
    low: The starting index of the sub-array to partition (inclusive).
    high: The ending index of the sub-array to partition (exclusive).

  Returns:
    The index where the next split in sub-arrays happens.
  """
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  """
  method that calls itself (recursion) if the sub-array has a size larger than 1

  Args: 
    array: The list representing the array to be sorted.
    low: The optional starting index of the sub-array to sort (inclusive, defaults to 0).
    high: The optional ending index of the sub-array to sort (exclusive, defaults to the last element).

  Returns:
    None (sorts the array in-place)
  """
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
