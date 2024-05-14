# Comparing elements from index 0 to n and moving the larger element to the right side

my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if my_array[j] > my_array[j+1]:
      my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
      swapped = True
    if not swapped:
      break

print(f"Original Array: {my_array}")
print(f"Sorted Array: {my_array}")

