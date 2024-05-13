# Algorithm searches through a sorted array and returns the index of the value it searches for.
# The binary search algorithm checks the center value first. If the target value is lower, it searches the left side and vice versa. This repeats until it finds the target value.

def binary_search(arr, target_val):
  """Performs a binary search on a sorted array to find the index of the target value.

  Args:
        arr: The sorted array to search.
        target_val: The value to search for.

  Returns:
        The index of the target value in the array if found, otherwise "target not found".
  """

  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (right + left) // 2

    if arr[mid] == target_val:
      return mid

    elif arr[mid] < target_val:
      left = mid + 1
      
    else:
      right = mid - 1

  return -1

my_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
my_target = 15

result = binary_search(my_array, my_target)

if result != -1:
    print(f"Value {my_target} found at index {result}")
else:
    print("Target not found in array.")
