'''
Selection sort: This algorithm finds the smallest element in an unsorted part of the array and swaps it with the first element of that part. It repeats this process until the entire array is sorted. The time complexity of selection sort is O(n^2) in all cases.

'''
# Define a function to perform selection sort on an array
def selection_sort(array):
  # Get the length of the array
  n = len(array)
  # Loop over the array n times
  for i in range(n):
    # Find the index of the smallest element in the unsorted part of the array
    min_index = i
    for j in range(i+1, n):
      if array[j] < array[min_index]:
        min_index = j
    # Swap the smallest element with the first element of the unsorted part
    array[i], array[min_index] = array[min_index], array[i]
  # Return the sorted array
  return array

# Example: Sort an array of numbers using selection sort.
# Array can also be taken from the user. 
# To do that,
# i) Create a empty list 
# ii) Get the length of the array from the user.
# iii) Using a for/while loop append the elements to the list. 
# iv) Make a function call to sort the elements.
array = [5, 3, 8, 2, 9, 1]
print("Unsorted array:", array)
sorted_array = selection_sort(array)
print("Sorted array:", sorted_array)

'''
Output:

Unsorted array: [5, 3, 8, 2, 9, 1]
Sorted array: [1, 2, 3, 5, 8, 9]

'''
