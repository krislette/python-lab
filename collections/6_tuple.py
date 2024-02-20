# A tuple is like a list, but IMMUTABLE.
# A tuple READ only.
# A tuple is denoteed by parentheses.

# Do's and don'ts in tuples:
#       1. Can be READ.
#       2. Can be COMBINED.
#       3. Can be DELETED COMPLETELY.
#       4. Can't be ASSIGNED.
#       1. Can't be DELETED ONE BY ONE.

courses = ("History", "Math", "Physics", "CompSci")
print(courses)

# The lines of code below will produce an error because tuples are immutable.
# courses[1] = "Art"
# print(courses)

# Converting list to tuple:
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

# Converting tuple to list:
some_tuple = (5, 6, 7, 8, 9)
print(some_tuple)
some_list = list(some_tuple)
print(some_list)