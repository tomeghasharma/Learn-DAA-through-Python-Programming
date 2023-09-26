'''
Heap sort: This algorithm builds a binary heap from the array, repeatedly extracts the maximum element from the heap and places it at the end of the sorted part of the array, and then reduces the size of the heap by one. The time complexity of heap sort is O(n log n) in all cases.

'''

# Define a function to heapify a subtree rooted at a given index in an array
def heapify(array, n, i):
  # Assume the current index is the largest element in the subtree
  largest = i
  # Find the left child index of the current index
  left = 2 * i + 1
  # Find the right child index of the current index
  right = 2 * i + 2
  # Compare the current element with its left child and update the largest index if the left child is larger
  if left < n and array[left] > array[largest]:
    largest = left
  # Compare the current element with its right child and update the largest index if the right child is larger
  if right < n and array[right] > array[largest]:
    largest = right
  # If the largest index is not the same as the current index, swap them and recursively heapify the affected subtree
  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    heapify(array, n, largest)

# Define a function to perform heap sort on an array
def heap_sort(array):
  # Get the length of the array
  n = len(array)
  # Build a max heap from the array by heapifying each subtree from bottom to top
  for i in range(n//2 - 1, -1, -1):
    heapify(array, n, i)
  # Extract each element from the heap and place it at the end of the sorted part of the array
  for i in range(n-1, 0, -1):
    # Swap the root element (maximum) with the last element of the unsorted part of the array
    array[0], array[i] = array[i], array[0]
    # Reduce the size of the heap by one
    n -= 1
    # Heapify the root element to maintain the max heap property
    heapify(array, n, 0)
  # Return the sorted array
  return array

# Example: Sort an array of numbers using heap sort.
# Array can also be taken from the user. 
# To do that,
# i) Create a empty list 
# ii) Get the length of the array from the user.
# iii) Using a for/while loop append the elements to the list. 
# iv) Make a function call to sort the elements.
array = [5, 3, 8, 2, 9, 1]
print("Unsorted array:", array)
sorted_array = heap_sort(array)
print("Sorted array:", sorted_array)


'''
Output:

Unsorted array: [5, 3, 8, 2, 9, 1]
Sorted array: [1, 2, 3, 5, 8, 9]

'''