# A dict is a collection of *key pairs*.
# A dict is unordered.
# A dict is changeable and is indexed.
# It has a key: value.
# The key is ALWAYS a STRING.

student_one = {
    "name": "Acelle",
    "course": "BSCS",
    "age": 18
}

student_two = { 
    "name": "Regina",
    "course": "BSCS",
    "age": 18
}

# Reading a dict:
# Print the whole dictionary:
print(student_one)
print(student_two)

# Reading dictionary items:
# This can be achieved by using the KEY.
print(student_one["name"])
print(student_one["course"])
print(student_one["age"])

# Using the get method:
print(student_two.get("name"))
print(student_two.get("course"))
print(student_two.get("age"))

# Assigning dictionary items:
print(f"Original dict: {student_one}")
student_one["name"] = "Badeng"
print(f"Edited dict: {student_one}")

# Length of a dict:
# Determines the number of key pairs.
print(len(student_one))

# Adding an item to a dictionary:
# Just add a non-existing attribute to the list.
student_one["gender"] = "Kabadingan"            # Adds the "gender": "Kabadingan" to the dictionary.
print(student_one)
print(student_two)

# Deleting a value from the list using the pop method:
deleted_value = student_one.pop("name")
print(f"Popped: {deleted_value}, New dict: {student_one}")

# Deleting a value from the list using the popitem method:
# This does not take any parameter and removes the LAST entry in the dict.
popped_item = student_one.popitem()             # Returns a tuple version of the popped key pair.
print(f"Popped item: {popped_item}, New dict: {student_one}")

# Deleting a value from the dict using 'del' keyword:
del student_one["course"]
print(f"New dict: {student_one}")

# Deleting all values from a dict using clear method:
print(f"Student one before clear: {student_one}")
student_one.clear()
print(f"Student one after clear: {student_one}")

# Copying a dictionary:
student_three = student_two.copy()
print(student_two)
print(student_three)

# Getting all keys inside a dict:
# Returns a list that contains all the keys inside the dict.
print(student_two.keys())

# Getting all values inside a dict:
# Returns a list that contains all the values inside the dict.
print(student_two.values())

# Getting all key pairs inside a dict:
print(student_two.items())

# LIST OF DICTIONARIES
#   - are dictionaries inside a list.
comp_005 = {
    "description": "discrete_structures_2",
    "units": 3.0,
    "grade_status": "P"
}

comp_006 = {
    "description": "data_structures_and_algorithms",
    "units": 3.0,
    "grade_status": "P"
}

subjects = [comp_005, comp_006]
print(subjects)

# Accessing individual values inside a list of dicts using square brackets:
print(subjects[0]["description"])

# Accessing individual values inside a list of dicts using get method:
print(subjects[1].get("description"))

# Nested dicts:

# 1. Inserting a dict inside another dict through a variable:
person_one_attributes = {
    "height": 158,
    "weight": 45,
}

person_one = {
    "name": "Acelle",
    "course": "BSCS",
    "age": 18,
    "attributes": person_one_attributes
}

# 2. Inserting a dict inside another dict through direct initialization:
person_two = {
    "name": "Regina",
    "course": "BSCS",
    "age": 18,
    "attributes": {
        "height": 158,
        "weight": 46
    }
}

print(person_one)
print(person_two)

# Getting values inside a nested dict using square brackets:
print(person_one["attributes"]["height"])

# Getting values inside a nested dict using get method:
print(person_two.get("attributes").get("weight"))

# Getting a dict inside a dict:
print(person_one["attributes"])

# Updating multiple values inside a dict using the update() method:
student = {
    "name": "Acelle",
    "age": 18,
    "courses": [
        "Math",
        "CompSci"
    ]
}
print(f"Current dict: {student}")

# This takes a dictionary as a parameter if we want to edit/add multiple keys inside a dict.
student.update({
    "name": "Regina",
    "phone": "09159442848"
})
print(f"Updated dict: {student}")

# Looping through a dict:
# Gets the keys inside the dict:
random_numbers = {
    "favorite": 8,
    "love": 6,
    "memorable": 18,
}

print("Here are the keys inside random_numbers:")
for key in random_numbers:
    print(key)

# Gets the keys and values inside the dict using items() method:
print("Here are the keys and values inside random_numbers:")
for key, value in random_numbers.items():
    print(f"Key: {key}")
    print(f"Value: {value}")