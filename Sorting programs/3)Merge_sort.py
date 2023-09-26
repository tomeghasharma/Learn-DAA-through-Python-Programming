'''
Merge sort: This algorithm divides the array into two halves, recursively sorts each half, and then merges them back together in a sorted order. The time complexity of merge sort is O(n log n) in all cases.

'''
# Define a function to merge two sorted arrays into one sorted array
def merge(array1, array2):
  # Initialize an empty array to store the merged result
  result = []
  # Initialize two pointers to track the current index of each array
  i = 0 # Pointer for array1
  j = 0 # Pointer for array2
  # Loop until one of the arrays is exhausted
  while i < len(array1) and j < len(array2):
    # Compare the current elements of each array and append the smaller one to the result
    if array1[i] < array2[j]:
      result.append(array1[i])
      i += 1 # Increment the pointer for array1
    else:
      result.append(array2[j])
      j += 1 # Increment the pointer for array2
  # Append the remaining elements of the non-exhausted array to the result
  if i < len(array1):
    result.extend(array1[i:])
  if j < len(array2):
    result.extend(array2[j:])
  # Return the merged result
  return result

# Define a function to perform merge sort on an array
def merge_sort(array):
  # Get the length of the array
  n = len(array)
  # Base case: If the array has one or zero elements, it is already sorted
  if n <= 1:
    return array
  # Recursive case: Divide the array into two halves, sort each half, and then merge them
  else:
    # Find the middle index of the array
    mid = n // 2
    # Sort the left half of the array using merge sort
    left = merge_sort(array[:mid])
    # Sort the right half of the array using merge sort
    right = merge_sort(array[mid:])
    # Merge the sorted halves using the merge function
    return merge(left, right)

# Example: Sort an array of numbers using merge sort
# Array can also be taken from the user. 
# To do that,
# i) Create a empty list 
# ii) Get the length of the array from the user.
# iii) Using a for/while loop append the elements to the list. 
# iv) Make a function call to sort the elements.
array = [5, 3, 8, 2, 9, 1]
print("Unsorted array:", array)
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)



'''
Output:

Unsorted array: [5, 3, 8, 2, 9, 1]
Sorted array: [1, 2, 3, 5, 8, 9]

'''
