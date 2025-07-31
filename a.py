# 1. Creating lists
numbers = [5, 3, 1, 4, 2]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# 2. Accessing items
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

# 3. Modifying items
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# 4. Adding items
fruits.append("orange")
fruits.insert(1, "kiwi")
print("After adding items:", fruits)

# 5. Removing items
fruits.remove("apple")
fruits.pop()
print("After removing items:", fruits)

# 6. Length of list
print("Number of fruits:", len(fruits))

# 7. Looping through a list
print("Fruit list:")
for fruit in fruits:
    print("-", fruit)

# 8. Check if item exists
if "cherry" in fruits:
    print("Cherry is in the list!")

# 9. Slicing
print("First 3 numbers:", numbers[:3])
print("Last 2 numbers:", numbers[-2:])

# 10. Functions on list
numbers.sort()
print("Sorted numbers:", numbers)

numbers.reverse()
print("Reversed numbers:", numbers)

print("Max number:", max(numbers))
print("Min number:", min(numbers))
print("Sum of numbers:", sum(numbers))

# 11. Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Element at row 2, column 3:", matrix[1][2])

# 12. List comprehension (bonus)
squares = [x**2 for x in range(1, 6)]
print("Squares from 1 to 5:", squares)
