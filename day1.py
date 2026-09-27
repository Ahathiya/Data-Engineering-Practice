"""A practical introduction to Python variables and built-in data types."""

# A variable is a name referring to an object. Python infers its type, so no
# declaration is required. Names are case-sensitive and should be descriptive.
name = "Alice"
age = 25
height = 5.8
is_student = True
print(name, age, height, is_student)
print("Types:", type(name), type(age), type(height), type(is_student))

# Python is dynamically typed: a name can later refer to an object of another type.
value = 10
print("Before:", value, type(value))
value = "ten"
print("After:", value, type(value))

# Common scalar (single-value) types
integer_number = 42                 # int: whole numbers
decimal_number = 3.14               # float: decimal numbers
complex_number = 2 + 3j             # complex: real and imaginary parts
text = "Hello, Python!"             # str: Unicode text
enabled = True                      # bool: True or False
nothing = None                      # NoneType: absence of a value
print(integer_number, decimal_number, complex_number, text, enabled, nothing)

# Operators work according to the values' types.
print("Arithmetic:", 10 + 3, 10 - 3, 10 * 3, 10 / 3, 10 // 3, 10 % 3, 2 ** 3)
print("Comparisons:", age >= 18, age == 25, age != 30)
print("Logical:", is_student and age < 30, not enabled)

# Strings are immutable sequences; indexing starts at zero and slicing excludes stop.
message = "Hello, Python!"
print(message[0], message[7:13], message.upper(), len(message))
print(f"{name} is {age} years old")  # f-strings insert variable values

# Collection types: list is ordered and mutable.
numbers = [1, 2, 3]
numbers.append(4)
numbers[0] = 10
print("List:", numbers, numbers[1:3])

# Tuple is ordered and immutable (useful for fixed groups of values).
point = (10, 20)
x_coordinate, y_coordinate = point  # unpacking
print("Tuple:", point, x_coordinate, y_coordinate)

# Set stores unique, unordered values and supports set operations.
unique_numbers = {1, 2, 2, 3}
unique_numbers.add(4)
print("Set:", unique_numbers, {1, 2} | {2, 3}, {1, 2} & {2, 3})

# Dictionary maps unique keys to values; it is mutable.
student = {"name": "Bob", "age": 21, "course": "Python"}
student["age"] = 22
print("Dictionary:", student)
print(student.get("name"), student.keys(), student.values())

# Mutable versus immutable: lists can change; strings, numbers, and tuples cannot.
# A variable assignment does not copy an object; use .copy() when needed.
original = [1, 2]
copied = original.copy()
copied.append(3)
print("Original:", original, "Copied:", copied)

# Type conversion creates a value of another type. Invalid conversions raise errors.
integer_from_text = int("100")
float_from_text = float("2.5")
text_from_number = str(100)
print(integer_from_text, float_from_text, text_from_number)

# Multiple assignment, swapping, and a constant-like convention.
a, b, c = 1, 2, 3
a, b = b, a
PI = 3.14159  # Uppercase signals that this name should not be reassigned.
print("Values:", a, b, c, "PI:", PI)

# Useful introspection and naming rules.
print("Is age an int?", isinstance(age, int))
print("Object identity (not value equality):", age is age)
# Names may contain letters, digits, and underscores, but cannot start with a digit.
# Avoid keywords (such as class or for), and prefer snake_case for variables.