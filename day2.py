
"""Display the Python type of each value: 25, 25.0, the text "25",
and the Boolean value True."""
print(type(25))
print(type(25.0))
print(type("25"))
print(type(True))

"""Create a complex number with real part 10 and imaginary part 5.
   Display its type, its real part, and its imaginary part."""
num = 10 + 5j

print(type(num))
print(num.real)
print(num.imag)

#3. Display the types of the Boolean value False and the text "False".
print(type(False))
print(type("False"))

"""4. Give a variable the number 10 and display its type. Give the same
   variable the text "Ten" and display its type again."""
a = 10
print(type(a))

a = "Ten"
print(type(a))

#Topic 2 — Boolean Values and Comparison Operators
student1 = 75
student2 = 60

print(student1 == student2)

#6. Two files are 8 MB and 5 MB. Display whether their sizes are different.
file1 = 8
file2 = 5

print(file1 != file2)


"""7. Ravi is 20 and Anita is 22. Display whether Ravi is younger than Anita
   and whether Anita is older than Ravi."""
ravi = 20
anita = 22

print(ravi < anita)
print(anita > ravi)

""" A student scored 40 and the pass mark is 40. Display whether the
   score is greater than or equal to the pass mark."""

score = 40
pass_mark = 40

print(score >= pass_mark)


"""9. A bag weighs 15 kg and the limit is 15 kg. Display whether the bag's
   weight is less than or equal to the limit."""

bag_weight = 15
limit = 15

print(bag_weight <= limit)

#Topic 3 — Use these names in order for questions 10–14:


#10. Store the names in a list and display them in the given order.Order, Indexing, Slicing, and Length
names = ["Raju", "Ram", "Krishna", "Arun", "John"]

print(names)

#Display the third name using a positive index.
names = ["Raju", "Ram", "Krishna", "Arun", "John"]

print(names[2])
#12. Display the second-last name using a negative index.
names = ["Raju", "Ram", "Krishna", "Arun", "John"]

print(names[-2])

"""13. Use one slice to display the first three names, then another
    slice to display the last two names."""
names = ["Raju", "Ram", "Krishna", "Arun", "John"]

print(names[0:3])
print(names[3:5])
"""14. Display the total number of names. Then display the first name
    using indexing and a one-item list containing it using slicing.
    Show the type of both results."""

names = ["Raju", "Ram", "Krishna", "Arun", "John"]

# Display total number of names
print(len(names))

# Display first name using indexing
print(names[0])
print(type(names[0]))

# Display first name using slicing
print(names[0:1])
print(type(names[0:1]))