# Write a Python program to implement quicksort to sort a list of numbers.

def quickSort(arr):
    if(len(arr) <= 1):
        return arr
    
    pivot = arr[len(arr) // 2] # Choose the middle element as pivot
    left = [x for x in arr if (x < pivot)]
    right = [x for x in arr if (x > pivot)]
    middle = [x for x in arr if (x == pivot)]

    return quickSort(left) + middle + quickSort(right)


arr = [50,40,77,65,84,92,4,45]
sorted_arr = quickSort(arr)
print("Sorted: ",sorted_arr)

