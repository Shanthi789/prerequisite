def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    if not s.isnumeric():
        return (s[::-1])
    else:
        return ("Not a string")


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
rstr1 = string_reverse("Hello World")
print(rstr1)
rstr2 = string_reverse("Python")
print(rstr2)
