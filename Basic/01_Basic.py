# The original list
num_List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Index:    0   1   2   3   4   5   6   7   8   9

# [:] - Creates and prints a shallow copy of the entire list.
print(num_List[:])
# Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# [start:end] - Prints elements from index 2 up to (but not including) index 5.
print(num_List[2:5])
# Output: [30, 40, 50]

# [start:] - Prints elements from index 3 to the very end of the list.
print(num_List[3:])
# Output: [40, 50, 60, 70, 80, 90, 100]

# [:end] - Prints elements from the start (index 0) up to (but not including) index 6.
print(num_List[:6])
# Output: [10, 20, 30, 40, 50, 60]

# [start:end:step] - Prints elements from index 0 to 7 (exclusive), taking every 2nd element.
print(num_List[0:7:2])
# Output: [10, 30, 50, 70] (Starts at 10, skips 20, includes 30, skips 40, etc.)

# [start:end:step] - Prints elements from index 0 to 7 (exclusive), taking every 3rd element.
print(num_List[0:7:3])
# Output: [10, 40, 70] (Starts at 10, skips 20/30, includes 40, skips 50/60, includes 70)