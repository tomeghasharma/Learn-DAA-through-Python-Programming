'''
- Insertion sort: This algorithm iterates over the array and inserts each element into its correct position in a sorted part of the array. It repeats this process until the entire array is sorted. The time complexity of insertion sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted or nearly sorted.

'''
# Define a function to perform insertion sort on an array
def insertion_sort(array):
  # Get the length of the array
  n = len(array)
  # Loop over the array from the second element to the last element
  for i in range(1, n):
    # Store the current element in a temporary variable
    temp = array[i]
    # Initialize a pointer to track the position of the current element in the sorted part of the array
    j = i - 1
    # Loop backwards over the sorted part of the array until we find the correct position for the current element or reach the beginning of the array
    while j >= 0 and array[j] > temp:
      # Shift each element that is larger than the current element to the right by one position
      array[j+1] = array[j]
      # Run this line to track the output: print(array[:])
      # Decrement the pointer
      j -= 1
    # Insert the current element into its correct position in the sorted part of the array
    array[j+1] = temp
  # Return the sorted array
  return array

# Example: Sort an array of numbers using insertion sort.
# Array can also be taken from the user. 
# To do that,
# i) Create a empty list 
# ii) Get the length of the array from the user.
# iii) Using a for/while loop append the elements to the list. 
# iv) Make a function call to sort the elements.
array = [5, 3, 8, 2, 9, 1]
print("Unsorted array:", array)
sorted_array = insertion_sort(array)
print("Sorted array:", sorted_array)

'''
Output:

Unsorted array: [5, 3, 8, 2, 9, 1]
Sorted array: [1, 2, 3, 5, 8, 9]

'''
