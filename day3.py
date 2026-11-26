#DAY 3 — STRINGS, LIST OPERATIONS, AND TUPLES

#Topic 1 — Strings: Indexing, Slicing, Concatenation, and replace()
""". From the word "Python", display the first character, the last
    character, and the number of characters."""
word = "Python"

# Display first character
print(word[0])

# Display last character
print(word[-1])

# Display total number of characters
print(len(word))

"""16. Take a slice of "Python" that gives "yth" and display it."""
word = "Python"

print(word[1:4])

"""17. Store "Raju" and "Kumar" separately. Join them with one space
    and display the full name."""

first_name = "Raju"
last_name = "Kumar"

full_name = first_name + " " + last_name

print(full_name)

"""18. Start with "Raju Kumer". Use replace() to correct the surname to
    "Kumar". Save the result separately and display both strings."""
name = "Raju Kumer"

corrected_name = name.replace("Kumer", "Kumar")

print(name)
print(corrected_name)
"""19. In the text "red red blue", replace every "red" with
    "green". Display the new text."""

text = "red red blue"

new_text = text.replace("red", "green")

print(new_text)


"""Topic 2 — List CRUD: Create, Read, Update, and Delete"""
#Create and add
"""20. Create a list containing Raju and Ram. Add Arun at the end
    and display the list."""

names = ["Raju", "Ram"]

names.append("Arun")

print(names)

"""21. Create a list containing Raju, Ram, and Arun. Insert Anita
    immediately before Ram and display the list."""

names = ["Raju", "Ram", "Arun"]

names.insert(1, "Anita")

print(names)
"""22. Start with a list containing Raju and Ram. Add Anita and Arun
    as separate items using one call to extend(). Display the list."""
names = ["Raju", "Ram"]

names.extend(["Anita", "Arun"])

print(names)

"""23. Find the index of the first Ram and count how many times Ram appears.
Python Code:"""
names = ["Ram", "Anita", "Ram", "Arun"]

# Find the index of the first Ram
print(names.index("Ram"))

# Count how many times Ram appears
print(names.count("Ram"))

"""24. Store 70, 85, 90, and 75 in a list. Display the second mark, a slice containing the first two marks, and the list's length."""

marks = [70, 85, 90, 75]

# Display the second mark
print(marks[1])

# Display the first two marks
print(marks[0:2])

# Display the total number of marks
print(len(marks))


#Update
"""25. Create a list containing Raju, Ram, and Anita. Replace Ram
    with Ramesh using its position. Display the list and its length."""
names = ["Raju", "Ram", "Anita"]

# Replace Ram with Ramesh
names[1] = "Ramesh"

# Display updated list
print(names)

# Display list length
print(len(names))

"""26. Put 80, 65, 90, and 75 in a list. Sort the marks from lowest
    to highest and display the list."""
marks = [80, 65, 90, 75]

# Sort marks in ascending order
marks.sort()

print(marks)

"""27. Create a list containing 80, 65, and 90 in that order. Reverse
    its current order and display the list."""
marks = [80, 65, 90]

# Reverse the current order
marks.reverse()

print(marks)

#Delete
"""28. Create a list containing Ram, Anita, Ram, and Arun. Remove the
    first Ram by value and display the remaining names."""
names = ["Ram", "Anita", "Ram", "Arun"]

# Remove the first occurrence of Ram
names.remove("Ram")

print(names)

"""29. Create a list containing Raju, Ram, and Anita. Use pop() to
    remove the item at index 1. Display the removed item and the list."""
names = ["Raju", "Ram", "Anita"]

# Remove item at index 1
removed_item = names.pop(1)

# Display removed item
print(removed_item)

# Display updated list
print(names)

"""30. Create a list containing Raju, Ram, and Anita. Use pop() with
    no index. Display the removed item and the remaining list."""

names = ["Raju", "Ram", "Anita"]

# Remove the last item
removed_item = names.pop()

# Display removed item
print(removed_item)

# Display remaining list
print(names)

"""31. Create a list containing Raju, Ram, Anita, and Arun. Use one
    del statement with a slice to delete the first two names.
    Display the remaining list."""

names = ["Raju", "Ram", "Anita", "Arun"]

# Delete the first two names
del names[0:2]

print(names)

"""32. Create a list with three names. Empty it using clear(), then
    display the list and its length."""
names = ["Raju", "Ram", "Anita"]

# Remove all elements from the list
names.clear()

# Display the empty list
print(names)

# Display the length
print(len(names))

"""Topic 3 — Tuples: Creation, Reading, and Immutability"""
"""33. Store 1920 and 1080 in a tuple. Display the type, the first
    value, the last value, and the length."""
resolution = (1920, 1080)

print(type(resolution))
print(resolution[0])
print(resolution[-1])
print(len(resolution))


"""34. Create a tuple containing 80, 90, 80, and 75. Use a slice to
    display the last two scores as a tuple."""
scores = (80, 90, 80, 75)

print(scores[-2:])

"""35. Use a tuple containing 80, 90, 80, and 75. Count how often
    80 appears and find the index of its first occurrence."""
numbers = (80, 90, 80, 75)

print("Count of 80:", numbers.count(80))
print("Index of first occurrence of 80:", numbers.index(80))


"""36. Create a tuple containing only the score 80. Display the
    tuple and its type."""
score = (80,)

print("Tuple:", score)
print("Type:", type(score))

"""37. Start with a tuple containing 70, 85, and 90. Create a new
    tuple with the first score corrected to 75 and the other
    scores in the same order. Display both tuples."""
scores = (70, 85, 90)

new_scores = (75,) + scores[1:]

print("Original tuple:", scores)
print("Updated tuple:", new_scores)