import time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# User input
numbers = []
print("Enter 10 numbers, each followed by the Enter key: ")
for i in range(10):
    numbers.append(int(input()))

# Sorting the list
start_time = time.time()
sorted_list = quick_sort(numbers)
end_time = time.time()

# Printing the sorted list
print("Sorted list: ", sorted_list)
print("Time taken to sort: ", end_time - start_time, "seconds")