'''
Bubble sort: This algorithm compares each pair of adjacent elements in an array and swaps them if they are in the wrong order. It repeats this process until the array is sorted. The time complexity of bubble sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted

'''
# Define a function to perform bubble sort on an array
def bubble_sort(array):
  # Get the length of the array
  n = len(array)
  # Loop over the array n-1 times
  for i in range(n-1):
    # Initialize a flag to check if any swap occurred in this iteration
    swapped = False
    # Loop over the unsorted part of the array
    for j in range(n-1-i):
      # Compare each pair of adjacent elements and swap them if they are in the wrong order
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        # Set the flag to True to indicate that a swap occurred
        swapped = True
    # If no swap occurred in this iteration, then the array is already sorted and we can break out of the loop
    if not swapped:
      break
  # Return the sorted array
  return array

# Example: Sort an array of numbers using bubble sort
# Array can also be taken from the user. 
# To do that,
# i) Create a empty list 
# ii) Get the length of the array from the user.
# iii) Using a for/while loop append the elements to the list. 
# iv) Make a function call to sort the elements.
array = [5, 3, 8, 2, 9, 1]
print("Unsorted array:", array)
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)

'''
Output:

Unsorted array: [5, 3, 8, 2, 9, 1]
Sorted array: [1, 2, 3, 5, 8, 9]

'''

