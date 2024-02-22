# A set is a collection of variables that is PARTIALLY WRITABLE.
# That is because you can add (insert) in it, but you cannot edit it.
# A set is UNORDERED and UNINDEXED.
# A set is denoted by curly braces {}.
# Bawal basahin isa-isa, pwede lang basahin as a WHOLE.
even_numbers = {2, 4, 6, 8, 10}
print(even_numbers)

# Length of set:
print(len(even_numbers))

# Adding items to the set (based on the element's hash value):
even_numbers.add(12)
print(even_numbers)

# Adding multiple items to a set (using list):
even_numbers.update([12, 14, 16, 18, 20])               # 12 already exists therefor it isn't added anymore.
print(even_numbers)

# Removing an item from the set (based on the value):
names = {"Acelle", "Krislette", "Rosales"}
print(names)
names.remove("Krislette")
print(names)
# names.remove("Lacuña") <- This will produce an error because the string doesn't exist.

# Removing an item from the set (even if it exists or not):
foods = {"Strawberry", "Chocolate", "Chicken"}
foods.discard("Bread") # <- This won't produce an error because discard allows removal of non-existent value from the set.
print(foods)

# Removing an item from the set (using pop):
things = {"Notebook", "Laptop", "Pen"}
popped = things.pop() # <- This removes the "first" item in the set (although factually speaking, it is unordered).
print(things)
print(f"Removed item: {popped}")

# Deleting all of the values in the set:
things.clear()
print(things)

# Creating a copy of a set using .copy() function (same with lists).

# Union set:
set_one = {1, 2, 3, 4, 5}
print(f"First set: {set_one}")
set_two = {6, 7, 8, 9, 10}
print(f"Second set: {set_two}")
union_set = set_one.union(set_two)
print(f"Union set: {union_set}")

# Difference set (order matters):
set_one = {1, 2, 3, 4, 5}
set_two = {3, 4}
set_one_diff = set_one.difference(set_two)
print(set_one_diff)
set_two_diff = set_two.difference(set_one)
print(set_two_diff)

# Intersection set:
intersection_set = set_one.intersection(set_two)
print(intersection_set)

# Symmetrical difference:
# Removes the common elements between two sets.
set_one = {1, 2, 3, 4, 5}
set_two = {3, 4, 5, 6, 7}
symmetric_diff_set = set_one.symmetric_difference(set_two)
print(symmetric_diff_set)

# Disjoint set:
# Returns a boolean whether two sets have an intersection or not.
print(set_one.isdisjoint(set_two)) # <- This retuns False because set_one and set_two have intersections.
set_one = {1, 2, 3, 4, 5}
set_two = {6, 7, 8, 9, 10}
print(set_one.isdisjoint(set_two)) # <- This returns True because set_one and set_two have no intersections.

# Subset (order matters):
# Returns a boolean whether whether the left set is contained in the right set.
set_one = {1, 2, 3, 4, 5}
set_two = {3, 4}
print(set_one.issubset(set_two)) # <- This returns False because set_one is not a subset of set_two.
print(set_two.issubset(set_one)) # <- This returns True because set_two is a subset of set_one.

# Superset (order matters):
# Returns a boolean whether the right set is contained in the left set.
print(set_one.issuperset(set_two)) # <- This returns True because set_one is a superset of set_two.
print(set_two.issuperset(set_one)) # <- This returns False because set_two is not a superset of set_one.

# Casting sets:
# 1. Set to list:
my_set = {"Hajamyeon", "Neoreul", "Saranghago", "Issdaneun", "Mariya"}
print(f"Set of strings: {my_set}")
my_list = list(my_set)
print(f"List of strings: {my_list}")

# From this point, you can manipulate a list, and then typecast it back into a set.
# List to set:
my_list[0] = 1
modified_set = set(my_list)
print(modified_set)

# Set to tuple:
my_tuple = tuple(modified_set)
print(my_tuple)

# Declaring empty data collections:
# Empty lists:
empty_list = []
empty_list = list()

# Empty tuples:
empty_tuple = ()
empty_tuple = tuple()

# Empty sets:
empty_set = {} # <- This isn't correct because it is an empty DICT.
empty_set = set() # <- This is the correct way to initialize an emppty set.