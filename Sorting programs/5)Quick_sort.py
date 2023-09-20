'''
Quick sort: This algorithm chooses a pivot element from the array, partitions the array into two subarrays such that all elements less than the pivot are in the left subarray and all elements greater than or equal to the pivot are in the right subarray, and then recursively sorts each subarray. The time complexity of quick sort is O(n log n) in the best and average case, and O(n^2) in the worst case when the array is already sorted or nearly sorted.

'''

# Define a function to partition an array around a pivot element
def partition(array, low, high):
  # Choose the last element as the pivot
  pivot = array[high]
  # Initialize a pointer to track the position of the pivot in the sorted part of the array
  i = low - 1
  # Loop over the array from the low index to the high index
  for j in range(low, high):
    # Compare each element with the pivot and swap it with the element at the pointer if it is smaller or equal to the pivot
    if array[j] <= pivot:
      # Increment the pointer
      i += 1
      # Swap the elements
      array[i], array[j] = array[j], array[i]
  # Swap the pivot with the element at the pointer + 1 position
  array[i+1], array[high] = array[high], array[i+1]
  # Return the index of the pivot in the sorted part of the array
  return i + 1

# Define a function to perform quick sort on an array
def quick_sort(array, low, high):
  # Base case: If the low index is greater than or equal to the high index, there is nothing to sort
  if low >= high:
    return
  # Recursive case: Partition the array around a pivot element, and then sort each subarray using quick sort
  else:
    # Find the index of the pivot using the partition function
    pivot_index = partition(array, low, high)
    # Sort the left subarray using quick sort
    quick_sort(array, low, pivot_index - 1)
    # Sort the right subarray using quick sort
    quick_sort(array, pivot_index + 1, high)

# Example: Sort an array of numbers using quick sort.
# Array can also be taken from the user. 
# To do that,
# i) Create a empty list 
# ii) Get the length of the array from the user.
# iii) Using a for/while loop append the elements to the list. 
# iv) Make a function call to sort the elements.
array = [5, 3, 8, 2, 9, 1]
print("Unsorted array:", array)
# Call the quick sort function with the low index as 0 and the high index as n-1, where n is the length of the array
quick_sort(array, 0, len(array) - 1)
print("Sorted array:", array)


'''
Output:

Unsorted array: [5, 3, 8, 2, 9, 1]
Sorted array: [1, 2, 3, 5, 8, 9]

'''