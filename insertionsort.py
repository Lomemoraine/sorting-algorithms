def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# User input
numbers = []
print("Enter 10 numbers, each followed by the Enter key: ")
for i in range(10):
    numbers.append(int(input()))
# Sorting the list
sorted_list = insertion_sort(numbers)

# Printing the sorted list
print("Sorted list: ", sorted_list)