import timeit
import sys

# Task 1: Create a List of Squares Using List Comprehension
def squares_list(n):
    """Generate a list of squares of numbers from 1 to n."""
    return [i ** 2 for i in range(1, n + 1)]

# Task 2: Reverse a Sublist within a List
def reverse_sublist(lst, i, j):
    """Reverse the elements of lst from index i to j inclusive."""
    if i < 0 or j >= len(lst) or i > j:
        raise ValueError("Invalid indices")
    lst[i:j + 1] = lst[i:j + 1][::-1]
    return lst

# Task 3: Merge Two Sorted Lists
def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into a single sorted list."""
    sorted_list = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    
    # Append any remaining elements
    sorted_list.extend(list1[i:])
    sorted_list.extend(list2[j:])
    
    return sorted_list

# Timing and Memory Usage

def measure_performance():
    # Task 1: Timing
    def time_task1():
        squares_list(1000)
    
    time_task1_duration = timeit.timeit(time_task1, number=100)
    print(f"Task 1 (squares_list) time: {time_task1_duration:.5f} seconds")
    
    # Task 2: Timing
    def time_task2():
        lst = list(range(1000))
        reverse_sublist(lst.copy(), 100, 200)
    
    time_task2_duration = timeit.timeit(time_task2, number=100)
    print(f"Task 2 (reverse_sublist) time: {time_task2_duration:.5f} seconds")
    
    # Task 3: Timing
    def time_task3():
        list1 = list(range(1000))
        list2 = list(range(1000, 2000))
        merge_sorted_lists(list1, list2)
    
    time_task3_duration = timeit.timeit(time_task3, number=100)
    print(f"Task 3 (merge_sorted_lists) time: {time_task3_duration:.5f} seconds")

    # Memory Usage
    # Task 1
    squares = squares_list(1000)
    print(f"Task 1 (squares_list) memory usage: {sys.getsizeof(squares)} bytes")
    
    # Task 2
    lst = list(range(1000))
    reverse_sublist(lst, 100, 200)
    print(f"Task 2 (reverse_sublist) memory usage: {sys.getsizeof(lst)} bytes")
    
    # Task 3
    list1 = list(range(1000))
    list2 = list(range(1000, 2000))
    merged_list = merge_sorted_lists(list1, list2)
    print(f"Task 3 (merge_sorted_lists) memory usage: {sys.getsizeof(merged_list)} bytes")

# Execute performance measurements
measure_performance()
