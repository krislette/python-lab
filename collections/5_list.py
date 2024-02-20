# A list is an ADVANCED DATA TYPE.
# It is a READ and WRITE collection of variables.
# A list is MUTABLE.
# A list is denoted by square brackets [].
courses = ["History", "Math", "Physics", "CompSci"]

# Print the entire list:
print(courses)

# Length:
print(len(courses))

# Specified Index (Positive Index):
print(courses[3])

# Specifiec Index (Negative Index):
print(courses[-1])

# Get certain values:
print(courses[0:2])             # First index is inclusive, second index is not.
print(courses[:2])              # Same with the above code, shortcut.
print(courses[2:])              # Starting from a specified index other than zero.

# Appending to a list:
courses.append("Art")
print(courses)

# Inserting to a list:
courses.insert(2, "Chemistry")
print(courses)

# Inserting a list inside another list:
added_courses = ["Science", "Education"]
courses.insert(0, added_courses)
print(courses)

# Combining lists (extends method):
added_courses = ["Accountancy", "Engineering"]
courses.extend(added_courses)
print(courses)

# Combining lists (+ operator):
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

# Removing items from a list (specific value name):
courses.remove("Accountancy")
print(courses)

# Removing items from a list (last item):
popped = courses.pop()          # Pop method returns the removed value (stack).
print(courses)
print(f"Removed course: {popped}")

# Removing items from a list (specified index):
popped = courses.pop(0)                  # An index can be specified inside pop method.
print(courses)
print(f"Removed courses: {popped}")

# Note: These methods alters the ORIGINAL list.
# List reversal:
courses.reverse()
print(courses)

# List sorting:
courses.sort()
print(courses)

# Sorted and reversed:
courses.sort(reverse=True)
print(courses)

# Methods that alters the COPY of the list.
# List sorting:
courses = ["History", "Math", "Physics", "CompSci"]
sorted_list = sorted(courses)           # Returns a sorted COPY of the list.
print(f"Original List: {courses}")
print(f"Sorted List: {sorted_list}")

# Copying a list:
courses_copy = courses.copy()
print(f"Original List: {courses}")
print(f"Copied List: {courses_copy}")

# Getting maximum/minimum value from a list:
numbers = [18, 8, 1, 6, 14, 4, 2, 3]
print(f"Maximum number from {numbers} is {max(numbers)}")
print(f"Minimum number from {numbers} is {min(numbers)}")

# Getting the sum of an entire list:
print(f"Sum of {numbers} is {sum(numbers)}")

# Finding index of a value:
print(numbers.index(8))

# Looping in a list:
print("CompSci" in courses)

# Joining values in a list:
course_str = ", ".join(courses)             # Returns a string value of the joined list values.
print(course_str)

# Splitting a string with a certain character:
course_list = course_str.split(", ")
print(course_list)

# Deleting a value from the list using del keyword:
del course_list[1]
print(course_list)

# Deleting the whole list:
del course_list
# print(course_list) <- This will produce an error since "course_list" no longer exists.

# Clearing all values inside the list:
courses.clear()
print(courses)                              # The list still exists but is now empty.