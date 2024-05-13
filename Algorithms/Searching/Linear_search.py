# Algorithm searches through an array and returns the index of the value it searches for.
# if the array is not sorted then use this. if sorted then use binary search.
# A big difference between sorting algorithms and searching algorithms is that sorting algorithms modify the array, but searching algorithm leave the array unchanged.

def linear_search(arr, target_val):
  """ Search a sorted/unsorted array to find the index of the target value.

  Args:
    arr: The sorted/unsorted array to search.
    target_val: The value to search for

  Returns:
    the index of the target_val in the array if found, otherwise "target not found"
  """

  for i in range(len(arr)):
    arr[i] == target_val
    return i
  else:
    return -1

arr = [3, 7, 2, 9, 5]
target_val = 9

result = linear_search(arr, target_val)

if result != -1:
  print(f"Value {target_val} is in index {result}")
else:
  print(f"value {taget_val} not found.")
