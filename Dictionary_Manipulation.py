import timeit
import sys

# Task 1: Merge Two Dictionaries
def merge_dicts(dict1, dict2):
    """Merge two dictionaries, preserving the values of common keys from dict2."""
    merged = dict1.copy()  # Create a copy of dict1 to avoid mutating the original
    merged.update(dict2)   # Update with dict2, which will overwrite dict1's values for common keys
    return merged

# Task 2: Find the Intersection of Two Dictionaries
def intersect_dicts(dict1, dict2):
    """Find the intersection of two dictionaries: keys common to both with their values."""
    intersection = {key: dict1[key] for key in dict1 if key in dict2}
    return intersection

# Task 3: Count the Frequency of Each Unique Word in a List
def count_word_frequencies(words):
    """Count the frequency of each unique word in a list using a dictionary."""
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Timing and Memory Usage
def measure_performance():
    # Task 1: Timing
    def time_task1():
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merge_dicts(dict1, dict2)
    
    time_task1_duration = timeit.timeit(time_task1, number=1000)
    print(f"Task 1 (merge_dicts) time: {time_task1_duration:.5f} seconds")
    
    # Task 2: Timing
    def time_task2():
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        intersect_dicts(dict1, dict2)
    
    time_task2_duration = timeit.timeit(time_task2, number=1000)
    print(f"Task 2 (intersect_dicts) time: {time_task2_duration:.5f} seconds")
    
    # Task 3: Timing
    def time_task3():
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
        count_word_frequencies(words)
    
    time_task3_duration = timeit.timeit(time_task3, number=1000)
    print(f"Task 3 (count_word_frequencies) time: {time_task3_duration:.5f} seconds")

    # Memory Usage
    # Task 1
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = merge_dicts(dict1, dict2)
    print(f"Task 1 (merge_dicts) memory usage: {sys.getsizeof(merged_dict)} bytes")
    
    # Task 2
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    intersection_dict = intersect_dicts(dict1, dict2)
    print(f"Task 2 (intersect_dicts) memory usage: {sys.getsizeof(intersection_dict)} bytes")
    
    # Task 3
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    frequency_dict = count_word_frequencies(words)
    print(f"Task 3 (count_word_frequencies) memory usage: {sys.getsizeof(frequency_dict)} bytes")

# Execute performance measurements
measure_performance()
