# String Manipulation:
message = "Hello Bading"

# Length:
print(len(message))

# Substring:
print(message[0:5])             # First digit is inclusive, last digit is not.
print(message[:5])              # Same as the above code, shortcut.
print(message[6:])              # Starting from an arbitrary index that is not equal to 0.

# Lowercase:
print(message.lower())

# Uppercase:
print(message.upper())

# Occurence Count:
print(message.count("l"))       # There are two occurences of letter L from the message.

# Find:
print(message.find("Bading"))   # Returns the index of a character/substring.
print(message.find("World"))    # Returns -1 if there's no occurence of the char/substring.

# Replace:
print(message.replace("Bading", "World"))
print(message.replace("l", "r"))

# Concatenation (format):
greeting = "Hi"
name = "Acelle"
message = "{}, {}. How are you?".format(greeting, name)
print(message)

# Concatenation (f-string):
# Use this! Note: You can even manipulate strings inside curly brackets.
greeting = "Hello"
name = "Regina"
message = f"{greeting}, {name.upper()}. How are you?"
print(message)

# See all available methods:
print(dir(message))             # Prints all methods for STRINGS because "message" variable is a string.
print(help(str))                # Information for strings.